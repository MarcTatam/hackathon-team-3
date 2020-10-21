import requests
import json
def kelvin_to_celsius(kelvin:int)->int:
    '''Converts the arguement kelvin to celsius'''
    return kelvin - 273.15
def config_reader()->dict:
    ''' Reads config.txt for api keys
    Note marker will have to add their own openweathermap api key to config.json
    
    '''
    try:
        config = open("config.json", "r")
    except OSError:
        log("Error opening config.json, likely not found")
    keys = json.load(config)
    config.close()
    return keys

def weather_request_forecast()->dict:
    '''gets weather data from weather api. Works as of 21/10/2020'''
    keys = config_reader()
    try:
        forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=7290675&APPID={}'.format(keys["weather_key"]))
        print("Weather Api request successful")
    except:
        print("Weather Api request failed")
    if forecast.status_code != 200:
        raise ValueError("weather_request_forecast")
    return forecast.json()


forecast_weather = weather_request_forecast()
#print(forecast_weather)
weather_interested = [forecast_weather['list'][0]["main"]["temp"],forecast_weather['list'][0]["main"]["temp_min"],forecast_weather['list'][0]["main"]["temp_max"],forecast_weather['list'][0]["main"]["feels_like"],forecast_weather['list'][0]["rain"]["3h"]]
#print(weather_interested)

def temp_assessment(temp:float)->str:
    '''Assesses the temperature and outputs a relevant string on what to wear'''
    if temp < 0:
        return "It's very cold, I'd wear lots of clothing"
    elif 0 < temp and temp <= 10:
        return "It's quite chilly, I'd recommend a jumper"
    elif 10 < temp and temp <= 20:
        return "It's fairly warm, long sleave top reccommended"
    elif 20 < temp:
        return "It's very warm, you should be fine in a t-shirt"

def rain_assessment(rain: float)->str:
    '''Assesses the expected rainfall and whether to brina coat or not'''
    if rain == 0:
        return "No rain forecast"
    elif 0 < rain and rain < 3:
        return "Some drizzle expected"
    elif 3 <= rain and rain < 12:
        return "Light to moderate rain expected, may need to bring a coat"
    elif 12 <= rain and rain < 24:
        return "Heavy rain expected, bring a coat"
    elif 24 <= rain:
        return "Very heavy rain expected, is it worth going?"

def what_to_wear(weather:list)->str:
    '''outputs whether or not one should wear a coat'''
    return_string = "Forecast weather is: "
    temp = kelvin_to_celsius(float(weather[0]))
    temp_low = kelvin_to_celsius(float(weather[1]))
    temp_high = kelvin_to_celsius(float(weather[2]))
    feels_like = kelvin_to_celsius(float(weather[3]))
    rain = float(weather[4])
    return_string = return_string + "\nTemperature: " + str(round(temp, 2)) + "°C with a high of " + str(round(temp_high, 2)) + "°C and a low of " + str(round(temp_low,2)) + "°C. It feels like " + str(round(feels_like,2)) + "°C. \n"
    return_string = return_string + str(round(rain,2)) + "mm of rain expected\n"
    return_string = return_string + temp_assessment(temp) + "\n"
    return_string = return_string + rain_assessment(rain)
    return return_string

if __name__ == "__main__":
    print(what_to_wear(weather_interested))
    