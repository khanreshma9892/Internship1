import requests
import matplotlib.pyplot as plt

# Latitude and longitude of Mumbai
lat = 19.0760
lon = 72.8777

# Open-Meteo API URL
url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    f"&daily=temperature_2m_max&timezone=Asia%2FKolkata"
)

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Extract dates and max temperatures
    dates = data['daily']['time']
    temps = data['daily']['temperature_2m_max']

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(dates, temps, marker='o', color='orange')
    plt.title("5-Day Max Temperature Forecast for Mumbai")
    plt.xlabel("Date")
    plt.ylabel("Max Temp (°C)")
    plt.xticks(rotation=45)  # Rotate date labels for clarity
    plt.grid(True)
    plt.tight_layout()       # Adjust layout to avoid label cutoff
    plt.show()

else:
    print(f"Failed to fetch data: {response.status_code}")
