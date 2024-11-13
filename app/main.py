from fastapi import FastAPI
from controllers.vehicle_controller import vehicle_router
from controllers.user_controller import user_router
from controllers.auth_controller import auth_router
from app.controllers.failure_controller import failure_router

app = FastAPI()

app.include_router(vehicle_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(failure_router)
