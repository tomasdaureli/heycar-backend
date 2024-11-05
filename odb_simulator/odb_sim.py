import os
import random
import json
import requests
import time
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")

def generate_status():
    status_options = ["OK", "DANGER", "CHECK"]

    data = {

        "engine_status": random.choice(status_options),
        "battery_status": random.choice(status_options),
        "brakes_status": random.choice(status_options),
        "tires_status": random.choice(status_options),
        "oil_status": random.choice(status_options),
        "temperature_status": random.choice(status_options),
        "front_light_status": random.choice(status_options),
        "rear_light_status": random.choice(status_options)

    }

    return data


def generate_random_car_status (interval_seconds,vehicle_Id):

    url =  f"{API_URL}/vehicles/{vehicle_Id}/actual-status"

    while True:
        data = generate_status()
        try:
            response = requests.post(url, json=data)
            print("Estado: ", response.json())
        except requests.exceptions.RequestException as e:
            print("Error al enviar:", e)
        
        time.sleep(interval_seconds)



generate_random_car_status (5,1)