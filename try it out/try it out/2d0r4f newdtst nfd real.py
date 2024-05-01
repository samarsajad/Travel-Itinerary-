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


def generate_travel_plan(destination, num_days, budget, interest):
    dataset_path = r"C:\Users\jenit\OneDrive\Desktop\btech\Winter sem 24\P.E - 2\Review 3 Start\Latest places_some missing coordinates\finalll 1.csv"
    places_dataset = pd.read_csv(dataset_path, encoding='latin1')

    places_dataset = places_dataset[(places_dataset['City'].str.lower() == destination.lower()) &
                                    (places_dataset['Interest'].str.lower() == interest.lower())]

    start_lat = 28.6139
    start_long = 77.2090

    places_dataset['distance'] = places_dataset.apply(
        lambda row: calculate_distance(start_lat, start_long, row['Latitude'], row['Longitude']), axis=1)

    affordable_places = places_dataset[places_dataset['Entrance Fee in INR'] <= budget]
    affordable_places = affordable_places.sort_values(by=['distance', 'Entrance Fee in INR'])

    travel_plan = f"Travel plan for {num_days} days to {destination} with interest in {interest} within a budget of INR {budget}:\n\n"

    places_available = len(affordable_places)
    for day in range(num_days):
        travel_plan += f"Day {day + 1}:\n"
        daily_destinations = affordable_places.iloc[day * 2: (day + 1) * 2]  # Select 2 destinations for each day
        if len(daily_destinations) == 0:
            travel_plan += "Sorry, we are out of destinations for this day.\n"
            continue
        travel_plan += "Morning Destination:\n"
        for _, row in daily_destinations.iloc[:1].iterrows():
            travel_plan += f"{row['Name']} - \n"
            travel_plan += f"Google rating: {row['Google review rating']}\n"
            travel_plan += f"Entrance Fee: {row['Entrance Fee in INR']} INR\n"
            travel_plan += f"Distance: {row['distance']:.2f} km\n\n"
        travel_plan += "Evening Destination:\n"
        for _, row in daily_destinations.iloc[1:].iterrows():
            travel_plan += f"{row['Name']} - \n"
            travel_plan += f"Google rating: {row['Google review rating']}\n"
            travel_plan += f"Entrance Fee: {row['Entrance Fee in INR']} INR\n"
            travel_plan += f"Distance: {row['distance']:.2f} km\n\n"

    if places_available < num_days * 2:
        days_without_places = (num_days * 2) - places_available
        travel_plan += f"Sorry, we are out of destinations for {days_without_places} days.\n"

    return travel_plan


def main():
    destination = input("Enter the City: ")
    interest = input("Enter your Interest: ")
    num_days = int(input("Enter number of days of the plan: "))
    budget = float(input("Enter your total budget for entrance fees in INR: "))
    plan = generate_travel_plan(destination, num_days, budget, interest)
    print(plan)


if __name__ == "__main__":
    main()
