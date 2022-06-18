import requests
import json

api_key = '' # agregar key de openweathermap
ciudad = input('Ingresa la ciudad de la que quieres saber la temperatura: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'

peticion = requests.get(url)
datos = json.loads(peticion.content)

print(f'Temperatura mínima: {datos["main"]["temp_min"]}ºC')
print(f'Temperatura máxima: {datos["main"]["temp_max"]}ºC')


