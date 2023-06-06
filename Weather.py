import requests


class Weather:
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city

    def get_city_coord(self):
        payload = {
            'q': self.city, 
            'appid': self.api_key
        }
        url = 'https://api.openweathermap.org/data/2.5/weather'
        
        req = requests.get(url, params=payload).json()

        return {'lon': req['coord']['lon'], 'lat': req['coord']['lat']}

    def get_weather_data(self):
        coordinates = self.get_city_coord()
        payload = {
            'lat': coordinates['lat'],
            'lon': coordinates['lon'], 
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ru'
        }
        url = 'https://api.openweathermap.org/data/2.5/weather'

        req = requests.get(url, params=payload).json()

        return req
    
    def get_weather(self):
        weather_data = self.get_weather_data()
        weather_answer = weather_data["weather"][0]["description"]
        weather_answer += "\nТемпература: " + str(weather_data["main"]["temp"]) + " гр. Цельсия"
        weather_answer += "\nОщущается как: " + str(weather_data["main"]["feels_like"]) + " гр. Цельсия"
        weather_answer += "\nВлажность: " + str(weather_data["main"]["humidity"]) + " мм. рт. ст."
        weather_answer += "\nВысота над уровнем моря: " + str(weather_data["main"]["sea_level"]) + " м"
        return weather_answer
    