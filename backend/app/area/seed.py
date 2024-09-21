import datetime
import random

from app.area.models import Area, AreaSeason, SoilIndicator, SoilIndicatorStats, SatelliteStats
from app.payment.enums import OrderStatus
from app.payment.models import Order
from app.repository.tools import random_datetime, random_date
from app.subscription.models import Plan
from app.users.auth import get_hashed_password
from app.users.models import User, Role


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


def generate_satellite_data():
    return {
        "humidity": {"value": random.uniform(20.0, 90.0), "unit": "%"},  # Влажность в процентах
        "thermal_radiation": {"value": random.uniform(100, 400), "unit": "W/m^2"},
        # Тепловое излучение в ваттах на квадратный метр
        "visible_light": {"value": random.uniform(0.1, 1.0), "unit": "relative"},
        # Интенсивность видимого света (относительная величина)
        "soil_type": {"value": random.choice(["clay", "sand", "loam", "peat", "chalk"]), "unit": "type"},  # Тип почвы
        "pollution": {"value": random.uniform(0.0, 100.0), "unit": "index"},  # Индекс загрязнения
        "wind": {"value": random.uniform(0, 100), "unit": "km/h"},  # Скорость ветра в км/ч
        "rain": {"value": random.choice([True, False]), "unit": "boolean"},  # Наличие дождя (да/нет)
        "temperature": {"value": random.uniform(20.0, 40.0), "unit": "Celsius"}  # Температура в градусах Цельсия
    }


def generate_advanced_satellite_data():
    return {
        "windy_zones": {"value": random.choice(["high", "medium", "low"]), "unit": "level"},  # Уровень ветра
        "sunny_patches": {"value": random.choice(["frequent", "occasional", "rare"]), "unit": "frequency"},
        # Частота солнечного света
        "most_humid_zones": {"value": random.choice(["swampy", "coastal", "rainforest"]), "unit": "type"}
        # Типы наиболее влажных зон
    }


def generate_agricultural_advice():
    # Искусственные данные для примера
    conditions = [
        {
            "condition": "high temperature and sun",
            "advice": "Ideal conditions for heat-loving crops.",
            "crops": "Tomatoes, peppers, eggplants"
        },
        {
            "condition": "high humidity and swampy",
            "advice": "Wet conditions suitable for rice.",
            "crops": "Rice"
        },
        {
            "condition": "high wind",
            "advice": "Strong wind may damage tall plants.",
            "crops": "Potatoes, carrots, cabbage"
        },
        {
            "condition": "moderate conditions",
            "advice": "Standard conditions for temperate crops.",
            "crops": "Wheat, barley, corn"
        }
    ]

    selected_advice = random.choice(conditions)
    return {
        "personal_advice": selected_advice["advice"],
        "what_to_grow": selected_advice["crops"]
    }


class Seeder:
    @staticmethod
    async def run():
        print('area seed')
        await Plan.first_or_create(filter=Plan.system_name == 'start',
                                   name="Базовый",
                                   price=5,
                                   system_name="start",
                                   with_ai=False,
                                   with_indicator=False,
                                   )
        await Plan.first_or_create(filter=Plan.system_name == 'advanced',
                                   name="Продвинутый",
                                   price=15,
                                   system_name="advanced",
                                   with_ai=True,
                                   with_indicator=False,
                                   )
        pro_plan = await Plan.first_or_create(filter=Plan.system_name == 'pro',
                                   name="Профессиональный",
                                   price=25,
                                   system_name="pro",
                                   with_ai=True,
                                   with_indicator=False,
                                   )
        user_role = await Role.first_or_create(
            filter=Role.system_name == 'user', system_name="user")
        user_1 = await User.first_or_create(filter=User.email == 'oktanc71@yandex.com',
                                            role_id=user_role.id,
                                            email='oktanc71@yandex.com',
                                            name="Asad",
                                            lastname="Oktamov",
                                            phone="+998937198242",
                                            hashed_password=get_hashed_password("oktanc71@yandex.com"))
        await Order.first_or_create(
            filter=Order.transaction_id == 'test_transaction',
            transaction_id="test_transaction",
            amount=25,
            status=OrderStatus.completed,
            user_id=user_1.id,
            plan_id=pro_plan.id,
            created_at=datetime.datetime.now()
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
            area_id=area_1.id
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
                soil_indicator_id=indicator_1.id,
                info=generate_soil_data(),
                area_season_id=area_season_1.id,
                result=generate_crop_data()
            ))
        for i in range(20):
            satellite_stats.append(SatelliteStats(
                date=random_date(f"{season_start_1}", f"{season_end_1}"),
                area_season_id=area_season_1.id,
                result=generate_agricultural_advice(),
                info={
                    'default': generate_satellite_data(),
                    'premium': generate_advanced_satellite_data()
                },
            ))
        await SoilIndicatorStats.insert(soil_indicator_stats)
        await SatelliteStats.insert(satellite_stats)
        print("area seed done")