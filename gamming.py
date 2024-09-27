import numpy as np
import matplotlib.pyplot as plt
import random

# Simulation parameters
total_area = 10000  # total area of the terrain in square meters
wind_speed = 20  # wind speed in km/h
flammability = 0.6  # flammability rate of vegetation (0 to 1)
humidity = 0.3  # soil humidity (0 to 1)
simulation_time = 30  # time in seconds

# Function that simulates fire spread
def simulate_fire_spread(wind_speed, flammability, humidity, simulation_time):
    # Effect of wind and humidity on the spread rate
    spread_rate = wind_speed * flammability * (1 - humidity)
    
    # Area burned per second
    area_per_second = spread_rate * 10  # arbitrary adjustment factor to scale the results
    
    # Calculate the burned area after 30 seconds
    burned_area = area_per_second * simulation_time
    
    return burned_area

# Function to visualize the spreading fire
def plot_fire(burned_area):
    # Create a grid to simulate the burned area
    grid_size = int(np.sqrt(total_area))
    terrain = np.zeros((grid_size, grid_size))
    
    # Randomly select points on the grid to simulate fire spread
    for _ in range(int(burned_area)):
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        terrain[x, y] = 1  # Mark the cell as burned
    
    # Plot the burned area
    plt.imshow(terrain, cmap='hot', interpolation='nearest')
    plt.title(f'Fire Spread Simulation: Burned Area = {burned_area:.2f} m²')
    plt.show()

# Run the simulation
burned_area = simulate_fire_spread(wind_speed, flammability, humidity, simulation_time)
print(f"Burned Area after {simulation_time} seconds: {burned_area:.2f} square meters")

# Plot the result
plot_fire(burned_area)
