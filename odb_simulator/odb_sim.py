import os
import random
import json
import time
from deep_translator import GoogleTranslator

from dotenv import load_dotenv
import requests

load_dotenv()
API_URL = os.getenv("API_URL")
VEHICLE_ID = os.getenv("VEHICLE_ID")
INTERVAL_SECONDS = int(os.getenv("INTERVAL_SECONDS", 5))

if not API_URL or not VEHICLE_ID:
    raise ValueError("API_URL y VEHICLE_ID deben estar configurados en el archivo .env")

with open('app/obd-trouble-codes.json') as f:
    odb_codes = json.load(f)

status_options = ["OK", "CHECK"]

def get_obd_code(component):
    status = random.choice(status_options)
    
    if status == "OK":
        return {"obd_code": "N/A", "translated_message": "No Aplica"}
    elif status in ["CHECK"]:
        for error in odb_codes:
            if component.lower() in error["message"].lower():
                # Traducción real usando deep-translator
                translated_message = GoogleTranslator(source='en', target='es').translate(error["message"])
                return {"obd_code": error["obd_code"], "translated_message": translated_message}
        return {"obd_code": "CODE_NOT_FOUND", "translated_message": "Código No Encontrado"}
    else:
        return {"obd_code": "N/A", "translated_message": "No Aplica"}

# OUTPUT EXAMPLE
# "obd_code":,
# "translated_message":,
# "status":
#
def generate_status():
    data = {
        "km": random.randint(10000, 100000),
        "engine_status": {
            **get_obd_code("engine"),
            "status": random.choice(status_options)
        },
        "battery_status": {
            **get_obd_code("battery"),
            "status": "DANGER"  # Siempre DANGER
        },
        "brakes_status": {
            **get_obd_code("brakes"),
            "status": random.choice(status_options)
        },
        "tires_status": {
            **get_obd_code("tires"),
            "status": random.choice(status_options)
        },
        "oil_status": {
            **get_obd_code("oil"),
            "status": random.choice(status_options)
        },
        "temperature_status": {
            **get_obd_code("temperature"),
            "status": random.choice(status_options)
        },
        "front_light_status": {
            **get_obd_code("front light"),
            "status": random.choice(status_options)
        },
        "rear_light_status": {
            **get_obd_code("rear light"),
            "status": random.choice(status_options)
        },
    }

    return data

def odb_sim_status(interval_seconds, vehicle_id):
     
    url = f"{API_URL}/vehicles/{vehicle_id}/actual-status"

    while True:
        data = generate_status()
        try:
            response = requests.put(url, json=data)
            if response.status_code == 200:
                print("Estado enviado correctamente:", json.dumps(data, ensure_ascii=False, indent=2))
            else:
                print(f"Error al enviar: {response.status_code}, Response: {response.text}")
        except requests.exceptions.RequestException as e:
            print("Error al enviar:", e)

        time.sleep(int(interval_seconds))


odb_sim_status(INTERVAL_SECONDS, VEHICLE_ID)
