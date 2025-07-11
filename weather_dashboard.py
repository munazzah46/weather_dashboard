import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Your OpenWeatherMap API key
API_KEY = 'e7eb6912a180290b7418dd8e5b1d5890'  # replace this with your real key

# List of cities you want data for
cities = ['London', 'New York', 'Delhi', 'Tokyo']

# Empty list to store temperatures
temps = []

# Fetch weather data for each city
for city in cities:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    print(f"Data for {city}: {data}")  # print the data to see what API returns

    # check if 'main' key exists in the data
    if 'main' in data:
        temp = data['main']['temp']
        temps.append(temp)
    else:
        print(f"Could not get temperature for {city}")
        temps.append(None)

# Draw a bar chart
sns.set(style='whitegrid')
plt.figure(figsize=(8,6))
sns.barplot(x=cities, y=temps, palette='coolwarm')
plt.title('Current Temperature in Cities')
plt.ylabel('Temperature (°C)')
plt.xlabel('City')
plt.show()