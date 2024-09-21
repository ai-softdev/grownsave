import datetime

from fastapi import APIRouter
from sqlalchemy import String, and_

from app.general.models import Country, Region, District, GeneralStats
from app.repository.tools import get_list_data

router = APIRouter(prefix="/general", tags=["general"])


@router.get('/country')
async def get_country_list(query: str = '', lang: str = 'en', page: int = 1, limit: int = 15):
    return await get_list_data(Country,
                               page=page,
                               limit=limit,
                               includes=['regions'],
                               filter=Country.names.op("->>")(lang).cast(String).icontains(query))


@router.get('/country/{id}')
async def get_country_detail(id: int):
    country = await Country.find_one_or_fail(filter=Country.id == id, includes=['regions'])
    return {
        'data': country,
    }


@router.get('/district/{region_id}')
async def get_district_detail(region_id: int, start_date: datetime.date, end_date: datetime.date):
    districts = await District.get_with_stats(filter=and_(
        District.region_id == region_id,
        GeneralStats.date.between(start_date, end_date)
    ), )
    return {
        'data': districts,
    }
