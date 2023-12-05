import numpy as np
import matplotlib.pyplot as plt

# Data
years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])
poland_values = np.array([3256.2, 3260.0, 3208.4, 3324.5, 3416.1, 3437.3, 3585.0, 3661.6, 3725.7, 3590.8, 3797.1, 3879.5, 3899.2, 3938.3, 3971.8, 3972.0])
ukraine_values = np.array([2778.4, 2791.8, 2844.8, 2998.0, 3151.1, 3246.0, 3399.5, 3528.3, 3534.4, 3228.0, 3549.8, 3662.4, 3640.6, 3600.2, 3418.6, 3419.0])

# Get user input for the country
country = input("Enter the country (Poland or Ukraine): ")

# Check if the entered country is valid
if country.lower() not in ['poland', 'ukraine']:
    print("Invalid country input. Please enter 'Poland' or 'Ukraine'.")
else:
    # Plotting
    plt.figure(figsize=(10, 6))  # Set the figure size

    if country.lower() == 'poland':
        plt.bar(years, poland_values, color='b', label='Poland')
    elif country.lower() == 'ukraine':
        plt.bar(years, ukraine_values, color='r', label='Ukraine')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Indicator Value')
    plt.title(f'Indicator Values Over the Years - {country.capitalize()}')
    plt.legend()  # Show legend

    # Show the plot
    plt.grid(True)
    plt.show()
