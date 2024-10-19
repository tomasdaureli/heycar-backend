from fastapi import FastAPI
from controllers.vehicle_controller import vehicle_router
from controllers.user_controller import user_router

app = FastAPI()

app.include_router(vehicle_router)
app.include_router(user_router)
