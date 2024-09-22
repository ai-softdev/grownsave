import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.admin.auth import authentication_backend
from app.database import engine
from app.scheduler import analyze_regions_data, analyze, analyze_area_data
from app.users.router import router as router_user
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import sentry_sdk
from sqladmin import Admin

def on_startup():
    scheduler = AsyncIOScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(analyze, trigger='cron', hour=8, minute=0, kwargs={'function_to_start': analyze_regions_data})
    scheduler.add_job(analyze, trigger='cron', hour=8, minute=0, kwargs={'function_to_start': analyze_area_data})

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


REQUEST_COUNT = Counter('request_count', 'Общее количество запросов')

@app.middleware("http")
async def count_requests(request, call_next):
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

sentry_sdk.init(
    dsn="https://f26f82a30fc4366b8db8e4e40097b742@o4507994811334656.ingest.de.sentry.io/4507994812645456",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
