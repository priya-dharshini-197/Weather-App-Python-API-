import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)
data = response.json()

temperature = data["current_condition"][0]["temp_C"]

print(f"Temperature in {city} is {temperature}°C")
