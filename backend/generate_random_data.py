import asyncio
import json
from datetime import datetime
import random

from app.general.models import District, GeneralStats


async def generate_random_data():
    data = []
    districts = await District.get_all(filter=District.district_code != None)
    for random_district in districts:
        data.append({
            "district_code": random_district.district_code,
            "stats": [{
                "info": {
                    "SOIL_TEMPERATURE": {
                        "value": round(random.uniform(10, 30), 2),
                        "unit": "Celsius"
                    },
                    "GROUNDWATER_LEVEL": {
                        "value": round(random.uniform(1, 5), 2),
                        "unit": "meters"
                    },
                    "PRESENCE_OF_PESTS": {
                        "value": round(random.uniform(0, 100), 2),
                        "unit": "%"
                    },
                    "PRODUCTIVITY": {
                        "value": round(random.uniform(60, 100), 2),
                        "unit": "%"
                    },
                    "VEGETATION_CONDITION": {
                        "value": round(random.uniform(50, 100), 2),
                        "unit": "%"
                    }
                },
                "date": datetime.now().isoformat(),
                "result": round(random.uniform(60, 100), 2)
            } for i in range(0, 5)]
        })
    file_path = 'data/stats/uzb.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


async def main():
    await generate_random_data()


if __name__ == "__main__":
    asyncio.run(main())
