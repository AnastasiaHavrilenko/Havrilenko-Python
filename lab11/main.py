import csv
import os

# Part 1: Read and display the contents of the CSV file

file_path = "baza.csv"

try:
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        print("Series Name | Country Name | 2016 [YR2016]")
        for row in reader:
            print(f"{row['Series Name']} | {row['Country Name']} | {row['2016 [YR2016]']}")

except FileNotFoundError:
    print(f"File {file_path} not found!")

# Part 2: Search for data based on user input and save the results in a new CSV file

flag = False
indicator = input("\nEnter a value to find indicators greater than: ")

while not indicator.replace('.', '').isdigit():
    indicator = input("Please enter a valid numeric value: ")

try:
    with open(file_path, "r", encoding="utf-8") as csvfile, open("new_baza.csv", "w", encoding="utf-8", newline='') as csvfile2:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()

        print("\nSeries Name | Country Name | 2016 [YR2016]")
        for row in reader:
            if row["2016 [YR2016]"].replace('.', '').isdigit() and float(row["2016 [YR2016]"]) > float(indicator):
                flag = True
                print(f"{row['Series Name']} | {row['Country Name']} | {row['2016 [YR2016]']}")
                writer.writerow(row)

except FileNotFoundError:
    print(f"File {file_path} not found!")

# Display a message if no data is found
if not flag:
    print(f"\nNo indicators greater than {indicator} found.")
