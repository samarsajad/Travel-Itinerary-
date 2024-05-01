import pandas as pd
from geopy.distance import geodesic


def calculate_distance(source_lat, source_long, dest_lat, dest_long):
    if pd.notnull(dest_lat) and pd.notnull(dest_long):
        source_coords = (source_lat, source_long)
        dest_coords = (dest_lat, dest_long)
        distance = geodesic(source_coords, dest_coords).kilometers
        return distance
    else:
        return float('inf')  # Return infinity if destination coordinates are missing


def generate_travel_plan(destination, num_days, budget):
    dataset_path = r"C:\Users\jenit\OneDrive\Desktop\btech\Winter sem 24\P.E - 2\Review 3 Start\FINAL RESTRO DATASET.csv"
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
        day_restaurants = restaurants_dataset.iloc[day * 3: (day + 1) * 3]  # Select 3 restaurants for each day
        if len(day_restaurants) == 0:
            travel_plan += "Sorry, we are out of restaurants for this scheduled day.\n"
            continue

        # Categorize the restaurants for morning, afternoon, and dinner
        morning_restaurant = day_restaurants.iloc[0]
        afternoon_restaurant = day_restaurants.iloc[1] if len(day_restaurants) >= 2 else None
        dinner_restaurant = day_restaurants.iloc[2] if len(day_restaurants) == 3 else None

        # Add morning restaurant
        travel_plan += "Morning:\n"
        travel_plan += f"{morning_restaurant['name']} - \n"
        travel_plan += f"Address: {morning_restaurant['address']}\n"
        travel_plan += f"Cuisine: {morning_restaurant['cuisine']}\n"
        travel_plan += f"Rating: {morning_restaurant['rating']}\n"
        travel_plan += f"Cost: {morning_restaurant['cost']} INR\n"
        travel_plan += f"Distance: {morning_restaurant['distance']:.2f} km\n\n"

        # Add afternoon restaurant
        if afternoon_restaurant is not None:
            travel_plan += "Afternoon:\n"
            travel_plan += f"{afternoon_restaurant['name']} - \n"
            travel_plan += f"Address: {afternoon_restaurant['address']}\n"
            travel_plan += f"Cuisine: {afternoon_restaurant['cuisine']}\n"
            travel_plan += f"Rating: {afternoon_restaurant['rating']}\n"
            travel_plan += f"Cost: {afternoon_restaurant['cost']} INR\n"
            travel_plan += f"Distance: {afternoon_restaurant['distance']:.2f} km\n\n"

        # Add dinner restaurant
        if dinner_restaurant is not None:
            travel_plan += "Dinner:\n"
            travel_plan += f"{dinner_restaurant['name']} - \n"
            travel_plan += f"Address: {dinner_restaurant['address']}\n"
            travel_plan += f"Cuisine: {dinner_restaurant['cuisine']}\n"
            travel_plan += f"Rating: {dinner_restaurant['rating']}\n"
            travel_plan += f"Cost: {dinner_restaurant['cost']} INR\n"
            travel_plan += f"Distance: {dinner_restaurant['distance']:.2f} km\n\n"

    return travel_plan


def main():
    destination = input("Enter the City: ")
    num_days = int(input("Enter number of days of the plan: "))
    budget = float(input("Enter your total budget for dining in INR: "))
    plan = generate_travel_plan(destination, num_days, budget)
    print(plan)


if __name__ == "__main__":
    main()
