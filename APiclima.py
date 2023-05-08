import requests

def get_temperature(city, api_key):
    # Construir la URL de la petición
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    # Obtener el JSON de la respuesta
    data = response.json()
    # Obtener la temperatura máxima y mínima en grados Celsius
    temp_min = data["main"]["temp_min"] - 273.15
    temp_max = data["main"]["temp_max"] - 273.15
    return temp_min, temp_max

city = input("dime tu ciudad: ")

api_key = "45387017cc98ea858f1d3faeb4a5042c"

temp_min, temp_max = get_temperature(city, api_key)

print(f"Temperatura mínima en {city}: {temp_min:.2f}°C")
print(f"Temperatura máxima en {city}: {temp_max:.2f}°C")
