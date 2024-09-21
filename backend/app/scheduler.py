import asyncio
import threading
from datetime import datetime, date

from sqlalchemy import and_

from app.area.models import AreaSeason, SoilIndicatorStats, SatelliteStats
from app.area.seed import generate_soil_data
from app.general.models import District, GeneralStats
from app.payment.models import Order
from app.request import request
from app.subscription.tools import has_subscription
from app.users.models import User


async def analyze(function_to_start):

    thread = threading.Thread(target=asyncio.run, args=(function_to_start(), ), daemon=True)
    thread.start()

async def analyze_regions_data():
    disctricts = await District.get_all()

    districts_list = []
    for district in disctricts:
        districts_list.append(district.id)

    disctricts_response = await request.post(url='https://ai-grownsave.ai-softdev.com/region', data=districts_list)

    for disctrict in disctricts_response:
        await GeneralStats.create(
            disctrict_id=disctrict['id'],
            info=disctrict['info'],
            result=disctrict['result'],
            date=disctrict['date']
        )


async def analyze_area_data():
    users = await User.get_all(includes=['areas'])


    for user in users:

        body = {}

        order = await has_subscription(user, raise_exception=False)
        if order:
            plan = order.plan

            for area in user['areas']:

                area_season = await AreaSeason.first(filter=AreaSeason.area_id == area.id,
                                                     includes=['area', 'soil_indicator_stats', 'satellite_stats'])

                body['id'] = area_season['id']
                body['culture_name'] = area_season['id']
                body['coordinates'] = area_season['coordinates']
                body['with_ai'] = plan.with_ai
                body['with_indicator'] = plan.with_indicator

                if plan.with_indicator:
                    '''
                    Taking data from soil indicator
                    
                    '''
                    soil_indicator_data = generate_soil_data()
                    body['soil_data'] = soil_indicator_data
                else:
                    body['soil_data'] = None

                area_response: dict = await request.post(url='https://ai-grownsave.ai-softdev.com/region', data=body)


                ''' We will get this info only if user is subscribed'''
                if plan.with_indicator:
                    await SoilIndicatorStats.create(
                        area_season_id=area_season['id'],
                        info=area_response['soil_data'],
                        datetime=datetime.now()
                    )

                ''' We will get the info anyway. If user is subscribed - the info will be completed '''
                await SatelliteStats.create(
                    area_season_id=area_season['id'],
                    info=area_response['satellite_data'],
                    datetime=date.today()
                )




