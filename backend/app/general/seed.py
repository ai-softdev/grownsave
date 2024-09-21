import json
import os
from datetime import datetime

from sqlalchemy import func, String

from app.general.models import Country, Region, District, GeneralStats
from sqlalchemy import text

DATA_DIR = 'data/countries/'


async def load_countries_data():
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.json'):
            filepath = os.path.join(DATA_DIR, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                country_names = data.get('names')
                country = await Country.first_or_create(
                    filter=Country.names.op("->>")("en").cast(String) == country_names['en'],
                    names=country_names
                )
                for region_data in data.get('regions', []):
                    region_names = region_data.get('names')
                    region = await Region.first_or_create(
                        filter=Region.names.op("->>")("en").cast(String) == region_names['en'],
                        names=region_names,
                        country_id=country.id,
                        code=region_data.get('code')
                    )
                    for district_data in region_data.get('districts', []):
                        district_name = district_data.get('name')
                        coordinates = district_data.get('coordinates')
                        await District.first_or_create(
                            filter=District.names.op("->>")("en").cast(String) == district_name['en'],
                            names=district_name,
                            region_id=region.id,
                            coordinates=coordinates,
                            district_code=district_data.get('district_code')

                        )


async def load_districts_data():
    with open('data/stats/uzb.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        insert_data = []
        for district in data:
            stats = district.get('stats')
            for stat in stats:
                dist = await District.find_one_or_fail(
                    filter=District.district_code == district.get('district_code'))
                insert_data.append(
                    GeneralStats(
                        district_id=dist.id,
                        info=stat.get('info'),
                        date=datetime.strptime(stat.get('date').replace('T', ' ').split('.')[0], '%Y-%m-%d %H:%M:%S'),
                        result=stat.get('result'),
                    )
                )
        await GeneralStats.insert(insert_data)


class Seeder:
    @staticmethod
    async def run():
        await load_countries_data()
        await load_districts_data()
