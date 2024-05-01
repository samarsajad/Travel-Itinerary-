import pandas as pd
from geopy.distance import geodesic
import os


def calculate_distance(source_lat, source_long, dest_lat, dest_long):
    if pd.notnull(dest_lat) and pd.notnull(dest_long):
        source_coords = (source_lat, source_long)
        dest_coords = (dest_lat, dest_long)
        distance = geodesic(source_coords, dest_coords).kilometers
        return distance
    else:
        return float('inf')  # Return infinity if destination coordinates are missing


def generate_travel_plan(destination, num_days, budget):
    
    current_dir = os.path.dirname(__file__)
    dataset_path = os.path.join(current_dir, "FINAL RESTRO DATASET.csv")
    restaurants_dataset = pd.read_csv(dataset_path)

    restaurants_dataset = restaurants_dataset[restaurants_dataset['city'].str.lower() == destination.lower()]
    restaurants_dataset = restaurants_dataset[restaurants_dataset['cost'] <= budget]

    start_lat = 28.6139
    start_long = 77.2090

    restaurants_dataset['distance'] = restaurants_dataset.apply(
        lambda row: calculate_distance(start_lat, start_long, row['Latitude'], row['Longitude']), axis=1)

    travel_plan = f"Travel plan for {num_days} days to {destination} within a budget of INR {budget}:\n\n"

    for day in range(num_days):
        travel_plan += f"Day {day + 1}:\n"
        day_restaurants = restaurants_dataset.iloc[day * 2: (day + 1) * 2]  # Select 2 restaurants for each day
        if len(day_restaurants) == 0:
            travel_plan += "Sorry, we are out of restaurants for this scheduled day.\n"
            continue
        brunch, dinner = day_restaurants.iloc[0], day_restaurants.iloc[1]
        travel_plan += "Brunch:\n"
        travel_plan += f"{brunch['name']} - \n"
        travel_plan += f"Address: {brunch['address']}\n"
        travel_plan += f"Cuisine: {brunch['cuisine']}\n"
        travel_plan += f"Rating: {brunch['rating']}\n"
        travel_plan += f"Cost: {brunch['cost']} INR\n"
        travel_plan += f"Distance: {brunch['distance']:.2f} km\n\n"
        travel_plan += "Dinner:\n"
        travel_plan += f"{dinner['name']} - \n"
        travel_plan += f"Address: {dinner['address']}\n"
        travel_plan += f"Cuisine: {dinner['cuisine']}\n"
        travel_plan += f"Rating: {dinner['rating']}\n"
        travel_plan += f"Cost: {dinner['cost']} INR\n"
        travel_plan += f"Distance: {dinner['distance']:.2f} km\n\n"

    return travel_plan


def main():
    destination = input("Enter the City: ")
    num_days = int(input("Enter number of days of the plan: "))
    budget = float(input("Enter your total budget for dining in INR: "))
    plan = generate_travel_plan(destination, num_days, budget)
    print(plan)


if __name__ == "__main__":
    main()
