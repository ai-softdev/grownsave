import asyncio
import threading

from app.general.models import District, GeneralStats
from app.request import request


async def analyze_regions_data():

    thread = threading.Thread(target=asyncio.run, args=(analyze(), ), daemon=True)
    thread.start()

async def analyze():
    disctricts = await District.get_all()

    districts_list = []
    for district in disctricts:
        districts_list.append(district.id)

    disctricts_response = await request.post('https://ai-grownsave.ai-softdev.com/region', data=districts_list)

    for disctrict in disctricts_response:
        await GeneralStats.create(
            disctrict_id=disctrict['id'],
            info=disctrict['info'],
            result=disctrict['result'],

        )
