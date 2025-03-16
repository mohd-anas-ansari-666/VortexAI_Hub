import requests
from vortexaihub.config import OPENWEATHER_API_KEY, DEFAULT_LOCATION
from vortexaihub.utils.text_processors import extract_location

def get_aqi(query):
    """
    Get air quality information for a location
    
    Args:
        query (str): The user's input query
        
    Returns:
        str: Air quality information response
    """
    # Extract location from query
    location = extract_location(query) or DEFAULT_LOCATION
    
    try:
        # Call OpenWeather Air Pollution API
        # First get coordinates for the location
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={OPENWEATHER_API_KEY}"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()
        
        if not geo_data:
            return f"Sorry, I couldn't find coordinates for {location}."
        
        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']
        
        # Now get air quality data
        aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
        aqi_response = requests.get(aqi_url)
        aqi_data = aqi_response.json()
        
        if aqi_response.status_code == 200:
            aqi = aqi_data['list'][0]['main']['aqi']
            components = aqi_data['list'][0]['components']
            
            # AQI scale: 1 = Good, 2 = Fair, 3 = Moderate, 4 = Poor, 5 = Very Poor
            aqi_labels = {
                1: "Good",
                2: "Fair",
                3: "Moderate",
                4: "Poor",
                5: "Very Poor"
            }
            
            aqi_info = (
                f"Air Quality in {location}:\n"
                f"AQI: {aqi_labels.get(aqi, 'Unknown')} ({aqi}/5)\n"
                f"PM2.5: {components.get('pm2_5', 'N/A')} μg/m³\n"
                f"PM10: {components.get('pm10', 'N/A')} μg/m³\n"
                f"NO2: {components.get('no2', 'N/A')} μg/m³\n"
                f"SO2: {components.get('so2', 'N/A')} μg/m³\n"
                f"CO: {components.get('co', 'N/A')} μg/m³"
            )
            return aqi_info
        else:
            return f"Sorry, I couldn't retrieve air quality information for {location}."
    
    except Exception as e:
        return f"Error retrieving air quality data: {str(e)}"