def get_weather(destination):

    weather_data = {
        "Goa": "30°C, Sunny",
        "Kerala": "28°C, Humid",
        "Kashmir": "18°C, Pleasant",
        "Manali": "15°C, Cool",
        "Shimla": "17°C, Pleasant",
        "Jaipur": "35°C, Hot",
        "Udaipur": "33°C, Sunny",
        "Varanasi": "32°C, Warm"
    }

    return weather_data.get(
        destination,
        "Weather data unavailable"
    )