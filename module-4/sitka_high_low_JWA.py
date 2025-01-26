import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Open the CSV file and read the data
def read_weather_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high temperatures, and low temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])
            highs.append(high)
            lows.append(low)

    return dates, highs, lows

# Plotting data
def plot_data(dates, temps, title, ylabel, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel(ylabel, fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# Main function
def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = read_weather_data(filename)

    while True:
        # Display menu
        print("\nWeather Data Viewer")
        print("1. High Temperatures")
        print("2. Low Temperatures")
        print("3. Exit")

        # Get the user input
        choice = input("Select an option (1-3): ")

        if choice == '1':
            plot_data(dates, highs, "Daily High Temperatures - 2018", "Temperature (F)", "red")
        elif choice == '2':
            plot_data(dates, lows, "Daily Low Temperatures - 2018", "Temperature (F)", "blue")
        elif choice == '3':
            print("Thank you for using the Weather Data Viewer. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
