country = input("Please Enter The country visited") # Add country name
visits = int(input("Please Enter The Number of Visits")) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

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
# Existing travel log data
# to be added to the travel_log. 
def add_new_country(name, number, cities):
    # Create a dictionary for the new country
    new_country = dict()
    new_country["country"] = name
    new_country["visits"] = number
    new_country["cities"] = cities
    # Append the new country to the travel_log list
    travel_log.append(new_country)

# Call the function to add the user-inputted country to the travel_log
add_new_country(name = country, number = visits, cities = list_of_cities)

# Display information about the last added country
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")