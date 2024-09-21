import datetime
import random

from app.area.models import Area, AreaSeason, SoilIndicator, SoilIndicatorStats, SatelliteStats
from app.repository.tools import random_datetime, random_date
from app.users.models import User


def generate_soil_data():
    return {
        "N": {"value": random.randint(5, 15), "unit": "mg/kg"},  # предполагаемый диапазон для азота
        "P": {"value": random.randint(3, 8), "unit": "mg/kg"},  # предполагаемый диапазон для фосфора
        "K": {"value": random.randint(10, 20), "unit": "mg/kg"},  # предполагаемый диапазон для калия
        "temperature": {"value": random.uniform(10, 35), "unit": "Celsius"},  # диапазон температур
        "humidity": {"value": random.randint(30, 60), "unit": "%"},  # диапазон влажности
        "ph": {"value": random.uniform(5.0, 8.0), "unit": "pH level"}  # диапазон уровня pH
    }


def generate_crop_data():
    crops = ["corn", "strawberry", "wheat", "rice", "potato", "tomato"]
    crop_data = []

    for crop in crops:
        crop_info = {
            "label": crop,
            "percent": random.randint(30, 100)
        }
        crop_data.append(crop_info)
    return crop_data


class Seeder:
    @staticmethod
    async def run():
        print('area seed')
        user_1 = await User.find_one_or_fail(
            filter=User.email == 'oktanc71@yandex.com'
        )
        area_1 = await Area.first_or_create(
            filter=Area.name == 'test area',
            name='test area',
            coordinates=["41.297611", "69.111707"],
            user_id=user_1.id
        )
        season_start_1 = random_date('2024-04-20', '2024-05-20')
        season_end_1 = random_date('2024-08-20', '2024-09-20')
        area_season_1 = await AreaSeason.first_or_create(
            filter=AreaSeason.start_date == datetime.date(2024, 5, 21),
            start_date=season_start_1,
            end_date=season_end_1,
            culture_name='corn',
        )
        indicator_1 = await SoilIndicator.first_or_create(
            filter=SoilIndicator.device_id == 'device_1',
            device_id="device_1",
            created_at=datetime.date(2024, 5, 25),
            area_id=area_1.id
        )
        soil_indicator_stats = []
        satellite_stats = []
        for i in range((season_end_1 - season_start_1).days):
            soil_indicator_stats.append(SoilIndicatorStats(
                datetime=random_datetime(season_start_1, season_end_1),
                soil_indicator_id=indicator_1,
                info=generate_soil_data(),
                area_season_id=area_season_1.id,
                result=generate_crop_data()
            ))
            satellite_stats.append(SatelliteStats(
                date=random_date(season_start_1, season_end_1),
                area_season_id=area_season_1.id,
                result='',
            ))
        await SoilIndicatorStats.insert(soil_indicator_stats)
        await SatelliteStats.insert(satellite_stats)
