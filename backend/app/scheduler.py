import asyncio
import threading

from app.general.models import District


async def analyze_regions_data():

    thread = threading.Thread(target=asyncio.run, args=(analyze(), ), daemon=True)
    thread.start()

async def analyze():
    disctricts = await District.get_all()

    districts_list = []
    # for district in disctricts:
    #     district
