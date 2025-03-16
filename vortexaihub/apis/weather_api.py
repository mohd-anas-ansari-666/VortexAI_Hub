import requests
from vortexaihub.config import OPENWEATHER_API_KEY, DEFAULT_LOCATION
from vortexaihub.utils.text_processors import extract_location

def get_weather(query):
    """
    Get weather information for a location
    
    Args:
        query (str): The user's input query
        
    Returns:
        str: Weather information response
    """
    # Extract location from query
    location = extract_location(query) or DEFAULT_LOCATION
    
    try:
        # Call OpenWeather API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            condition = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            weather_info = (
                f"Weather in {location}:\n"
                f"Temperature: {temp}°C\n"
                f"Conditions: {condition}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
            return weather_info
        else:
            return f"Sorry, I couldn't retrieve weather information for {location}. Please try another location."
    
    except Exception as e:
        return f"Error retrieving weather data: {str(e)}"