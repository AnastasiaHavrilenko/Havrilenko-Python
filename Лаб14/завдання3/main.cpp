import numpy as np
import matplotlib.pyplot as plt

# Data for Ukraine
labels = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
ukraine_values = [2778.4, 2791.8, 2844.8, 2998.0, 3151.1, 3246.0, 3399.5, 3528.3, 3534.4, 3228.0, 3549.8, 3662.4, 3640.6, 3600.2, 3418.6, 3419.0]

# Calculate percentages
total_ukraine = sum(ukraine_values)
percent_ukraine = [(value / total_ukraine) * 100 for value in ukraine_values]

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))

# Plot pie chart
colors = plt.cm.Paired(np.linspace(0, 1, len(labels)))  # Use np.linspace for values between 0 and 1
ax.pie(percent_ukraine, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)

# Add a title
ax.set_title('Indicator Values Distribution in Ukraine Over the Years')

# Show the pie chart
plt.show()
