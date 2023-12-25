# Function to safely get a list of cities from user input
def get_city_list():
    cities_input = input("Please enter the list of cities (comma-separated): ")
    return cities_input.split(", ")

# Prompt the user for input
country = input("Please enter the country visited: ")  # Add country name
visits = int(input("Please enter the number of visits: "))  # Number of visits
list_of_cities = get_city_list()  # Create list from formatted string

# Existing travel log data
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# to be added to the travel_log.
def add_new_country(name, number, cities):
    # Create a dictionary for the new country
    new_country = {"country": name, "visits": number, "cities": cities}
    # Append the new country to the travel_log list
    travel_log.append(new_country)

# Call the function to add the user-inputted country to the travel_log
add_new_country(name=country, number=visits, cities=list_of_cities)
# Print the updated travel_log
print(travel_log)

# Display information about the last added country
last_country = travel_log[-1]
print(f"I've been to {last_country['country']} {last_country['visits']} times.")
print(f"My favorite city was {last_country['cities'][0]}.")