import datetime as dt
import requests


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = '8841be9a1c7492b92c5244bb326e9673' 
user_city = input("Enter your city: ")

URL = BASE_URL + "appid=" +API_KEY +"&q=" + user_city
response = requests.get(URL).json()

if response['cod'] == '404':
    print("No City Found!! \nTry Again")

else:

    def kelvin_to_celsuis_fahrenheit(kelvin):
        celsuis = kelvin + 273.15
        fahrenheit = celsuis*(9/5) + 32
        return celsuis, fahrenheit


    temp_kelvin = response['main']['temp']
    temp_celsuis,temp_fahrenheit = kelvin_to_celsuis_fahrenheit(temp_kelvin)
    feels_like_kelvin =response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit  = kelvin_to_celsuis_fahrenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


    print(f"temperature in {user_city } is {temp_celsuis:.2f}°C or {temp_fahrenheit}°F")
    print(f"Temperature in {user_city } feels like {feels_like_celsius}°C or {feels_like_fahrenheit}°F")
    print(f"Humidity in {user_city }: {humidity}%")
    print(f"Wind Speed in {user_city }: {wind_speed}m/s")
    print(f"General Weather in {user_city}: {description}")
    print(f"sun rises in {user_city } at {sunrise_time} local time")
    print(f"sun sets in {user_city } at {sunset_time} local time")