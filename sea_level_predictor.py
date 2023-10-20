import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year'] #using the Year column as the x-axis 
    y = df['CSIRO Adjusted Sea Level'] #CSIRO Adjusted Sea Level column as the y-axis
    plt.scatter(x, y, c='DarkBlue')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
  
    x_values = range(1880, 2051) #Make the line go through the year 2050 to predict the sea level rise in 2050
    y_values = [(slope * year) + intercept for year in x_values]
  
    plt.plot(x_values, y_values, color='red', label=f'All Data: y = {slope:.2f}x + {intercept:.2f}')

    # Create second line of best fit
    second_data = df[df['Year'] >= 2000]
    x2 = second_data['Year'] #using the Year column as the x-axis 
    y2 = second_data['CSIRO Adjusted Sea Level'] #CSIRO Adjusted Sea Level column as the y-axis
  
    slope_second, intercept_second, _, _, _ = linregress(x2, y2)
  
    x_values_second = range(2000, 2051) #predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000
    y_values_second = [(slope_second * year) + intercept_second for year in x_values_second]
  
    plt.plot(x_values_second, y_values_second, color='green', label=f'Recent Data: y = {slope_second:.2f}x + {intercept_second:.2f}')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()