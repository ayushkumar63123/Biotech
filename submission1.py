from gtts import gTTS
from playsound import playsound
import sys


def speak(filename, text):
    tts = gTTS(text, lang='en')
    tts.save(filename + '.mp3')
    playsound(filename + '.mp3')


speak('Hello! Welcome to this biotech app!', '111')

def airqualityindex(o3, no2, pm):
    import requests

    url = "https://carbonfootprint1.p.rapidapi.com/AirQualityHealthIndex"

    querystring = {"O3": o3, "NO2": no2, "PM": pm}

    headers = {
        'x-rapidapi-key': "c9a50d71bbmsh986ce6928856767p1381e8jsn95185302faab",
        'x-rapidapi-host': "carbonfootprint1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

o3 = int(input("Enter the ppm quantity of o3: "))
no2 = int(input("Enter the ppm quantity of no2: "))
pm = int(input("Enter the ppm quantity of pm: "))
print('Air Quality Health Index:-')
airqualityindex(o3, no2, pm)
