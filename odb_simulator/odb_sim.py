import random
import json
import requests
import time

vehicle_Id = 1
url =  f"http://127.0.0.1:8000/vehicles/{vehicle_Id}/actual-status"

status_options = ["OK", "DANGER", "CHECK"]

def generate_status():
    return {
        "engine_status": random.choice(status_options),
        "battery_status": random.choice(status_options),
        "brakes_status": random.choice(status_options),
        "tires_status": random.choice(status_options),
        "oil_status": random.choice(status_options),
        "temperature_status": random.choice(status_options),
        "front_light_status": random.choice(status_options),
        "rear_light_status": random.choice(status_options)
    }


def generate_random_car_status (interval_seconds,vehicle_Id):

    url =  f"http://127.0.0.1:8000/vehicles/{vehicle_Id}/actual-status"

    while True:
        status = generate_status()
        with open("vehicle_status.json", "w") as f:
            json.dump(status, f, indent=4)

        try:
            response = requests.post(url, json=status)
            response.raise_for_status() 
            print("Estado:", status)
        except requests.exceptions.RequestException as e:
            print("Error al enviar el estado:", e)
        
        time.sleep(interval_seconds)
