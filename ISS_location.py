import requests
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="iss_tracker")

try:
    data = requests.get('http://api.open-notify.org/iss-now.json').json()
    lat, lon = float(data['iss_position']['latitude']), float(data['iss_position']['longitude'])
    
    location = geolocator.reverse(f"{lat}, {lon}", language='ru')
    country = location.raw['address']['country'] if location else "Где-то над океанами"

    print(f"--- Где же сейчас МКС? ---")
    print(f"Широта: {abs(lat):.2f}° {'северная' if lat >= 0 else 'южная'}")
    print(f"Долгота: {abs(lon):.2f}° {'восточная' if lon >= 0 else 'западная'}")
    print(f"Местоположение: {country}")
    
except Exception as e:
    print("Не удалось получить данные о положении МКС")