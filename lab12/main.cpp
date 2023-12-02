import json

def load_data(File):
    try:
        with open(File, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None

def save_data_to_file(data, File):
    with open(File, 'w') as file:
        json.dump(data, file, indent=2)

def print_json(File):
    data = load_data(File)
    if data:
        print(json.dumps(data, indent=2))
    else:
        print("File not found or empty.")

def add_entry(json_file, new_entry):
    data = load_data(json_file)
    if data:
        data.append(new_entry)
        save_data_to_file(data, json_file)
        print("Entry added successfully.")
    else:
        print("File not found or empty.")

def delete_entry(json_file, entry_to_delete):
  data = load_data(json_file)
  if data:
      data = [entry for entry in data if entry != entry_to_delete]
      save_data_to_file(data, json_file)
      print("Entry deleted successfully.")
  else:
      print("File not found or empty.")

def search_by_name(json_file, country_name):
    data = load_data(json_file)
    if data:
        results = [entry for entry in data if entry.get("name") == country_name]
        if results:
            print("Search results:")
            print(json.dumps(results, indent=2))
        else:
            print(f"No matching entries found for country: {country_name}")
    else:
        print("File not found or empty.")

def countries_in_region(json_file):
    data = load_data(json_file)
    if data:
        countries_in_africa_asia = [entry['name'] for entry in data if entry['region'] in ['Africa', 'Asia']]
        if countries_in_africa_asia:
            print(f"Countries in Africa or Asia: {', '.join(countries_in_africa_asia)}")
        else:
            print("No countries found in Africa or Asia.")
    else:
        print("File not found or empty.")

def main_menu():
    print("1. View JSON file")
    print("2. Add new entry")
    print("3. Delete entry")
    print("4. Search by country name")
    print("5. Countries in Africa or Asia")
    print("6. Exit")

json_file = "countries.json"

# Load initial data
countries_data = [
    {"name": "Ukraine", "area": 603500, "population": 41879916, "region": "Europe"},
    {"name": "Austria", "area": 83871, "population": 8800000, "region": "Europe"},
    {"name": "Bulgaria", "area": 110879, "population": 7100000, "region": "Europe"},
    {"name": "Сhina", "area": 9598100, "population": 1735735724, "region": "Africa"},
    {"name": "Gabon", "area": 267667, "population": 2000000, "region": "Africa"},
    {"name": "Spain", "area": 505370, "population": 46600000, "region": "Europe"},
    {"name": "Egypt", "area": 1001450, "population": 93400000, "region": "Africa"},
    {"name": "Cuba", "area": 110860, "population": 11300000, "region": "North America"},
    {"name": "Morocco", "area": 446550, "population": 35100000, "region": "Africa"},
    {"name": "Germany", "area": 357121, "population": 83100000, "region": "Europe"},
]
save_data_to_file(countries_data, json_file)

while True:
    # Display the menu
    main_menu()

    # Get user choice
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print_json(json_file)
    elif choice == "2":
        new_entry = {
            "name": input("Enter country name: "),
            "area": int(input("Enter area: ")),
            "population": int(input("Enter population: ")),
            "region": input("Enter region: "),
        }
        add_entry(json_file, new_entry)
    elif choice == "3":
      entry_name = input("Enter the name of the entry to delete: ")
      entry_to_delete = next((entry for entry in countries_data if entry['name'] == 
      entry_name), None)
      if entry_to_delete:
          delete_entry(json_file, entry_to_delete)
      else:
          print("Entry not found.")
    elif choice == "4":
        country_name = input("Enter country name: ")
        search_by_name(json_file, country_name)
    elif choice == "5":
        countries_in_region(json_file)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
