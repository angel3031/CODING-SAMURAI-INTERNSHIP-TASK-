import requests

def get_weather(city, api_key):
    try:
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        
        response = requests.get(url)
        data = response.json()
        
       
        if response.status_code == 200:
            city_name = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            weather = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            print(f"\nWeather in {city_name}, {country}:")
            print(f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)")
            print(f"☁ Condition: {weather.capitalize()}")
            print(f"💧 Humidity: {humidity}%")
            print(f"🌬 Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: {data['message'].capitalize()}")
    except Exception as e:
        print("⚠ Something went wrong:", str(e))


if __name__ == "__main__":
    API_KEY = "34f454975652c74c4afb9f22309020ef"  
    city = input("Enter city name: ")
    get_weather(city, API_KEY)
