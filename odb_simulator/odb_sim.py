import os
import random
import json
import requests
import time
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")
VEHICLE_ID = os.getenv("VEHICLE_ID")
INTERVAL_SECONDS = os.getenv("INTERVAL_SECONDS")

with open('app\obd-trouble-codes.json') as f:
    odb_codes = json.load(f)

status_options = ["OK", "CHECK"]

def get_obd_code(component):
    status = random.choice(status_options)
    
    if status == "OK":
        return "N/A"
    elif status in ["CHECK"]:
        for error in odb_codes:
            if component.lower() in error["message"].lower():
                return error["obd_code"]
        return "CODE_NOT_FOUND"
    else:
        return "N/A"

def generate_status():

    data = {
        "km": random.randint(10000, 100000),
        "engine_status": {
            "obd_code":  get_obd_code("engine"),
            "status":  random.choice(status_options)
        },
        "battery_status": {
            "obd_code":  get_obd_code("battery"),
            "status": "DANGER"
        }, #Solo este danger
        "brakes_status": {
            "obd_code":  get_obd_code("brakes"),
            "status":  random.choice(status_options)
        },
        "tires_status": {
            "obd_code":  get_obd_code("tires"),
            "status":  random.choice(status_options)
        },
        "oil_status": {
            "obd_code":  get_obd_code("oil"),
            "status":  random.choice(status_options)
        },
        "temperature_status": {
            "obd_code":  get_obd_code("temperature"),
            "status":  random.choice(status_options)
        },
        "front_light_status": {
            "obd_code":  get_obd_code("front light"),
            "status":  random.choice(status_options)
        },
        "rear_light_status": {
            "obd_code":  get_obd_code("rear light"),
            "status":  random.choice(status_options)
        },
    }

    return data


def generate_random_car_status(interval_seconds, vehicle_id):

    url = f"{API_URL}/vehicles/{vehicle_id}/actual-status"

    while True:
        data = generate_status()
        try:
            response = requests.put(url, json=data)
            if response.status_code == 200:
                print("Estado: ", data)
            else:
                print(f"Error: {response.status_code}, Response: {response.text}")
        except requests.exceptions.RequestException as e:
            print("Error al enviar:", e)

        time.sleep(int(interval_seconds))


generate_random_car_status(INTERVAL_SECONDS, VEHICLE_ID)
