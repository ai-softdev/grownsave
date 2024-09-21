import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.admin.auth import authentication_backend
from app.database import engine
from app.scheduler import analyze_regions_data, analyze, analyze_area_data
from app.users.router import router as router_user

from sqladmin import Admin

def on_startup():
    scheduler = AsyncIOScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(analyze, trigger='date', hour=8, minute=0, kwargs={'function_to_start': analyze_regions_data})
    scheduler.add_job(analyze, trigger='date', hour=8, minute=0, kwargs={'function_to_start': analyze_area_data})

    scheduler.start()

app = FastAPI(on_startup=on_startup())
app.include_router(router_user)
app.mount('/media', StaticFiles(directory='media'), name='media')
admin = Admin(app, engine=engine, authentication_backend=authentication_backend)
origins = [
    "http:localhost:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.general.router import router as router_general
app.include_router(router_general)
from app.area.router import router as router_area
app.include_router(router_area)
from app.subscription.router import router as router_subscribe
app.include_router(router_subscribe)
from app.payment.router import router as router_payment
app.include_router(router_payment)


