from fastapi import FastAPI
from controllers.vehicle_controller import vehicle_router

app = FastAPI()

app.include_router(vehicle_router)
