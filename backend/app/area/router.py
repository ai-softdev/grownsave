from fastapi import APIRouter, Depends
from sqlalchemy import and_

from app.area.models import Area, AreaSeason
from app.area.schemas import SAreaList, SAreaDetail, SAreaSeasonDetail, SAreaCreate, SArea, SAreaSeasonCreate, \
    SAreaSeason, SAreaSeasonCreateResponse

from app.repository.tools import get_list_data
from app.subscription.tools import has_subscription
from app.users.dependencies import get_current_user
from app.users.models import User

router = APIRouter(prefix="/area", tags=["area"])


@router.get('/list')
async def get_areas_list(page: int = 1, limit: int = 10, user: User = Depends(get_current_user)) -> SAreaList:
    return await get_list_data(Area, page, limit, Area.user_id == user.id)


@router.get('/{area_id}')
async def get_area(area_id: int, user: User = Depends(get_current_user)) -> SAreaDetail:
    area = await Area.find_one_or_fail(filter=and_(Area.id == area_id,
                                                   Area.user_id == user.id),
                                       includes=['seasons', 'soil_indicators'])
    return area



@router.post('/create')
async def create_area(data: SAreaCreate, user: User = Depends(get_current_user)) -> SArea:

    await has_subscription(user)

    area = await Area.create(
        name=data.name,
        user_id=user.id,
        coordinates=data.coordinates
    )

    return area


@router.post('/area_season/create')
async def create_area_season(data: SAreaSeasonCreate,
                             user: User = Depends(get_current_user)) -> SAreaSeasonCreateResponse:

    await has_subscription(user)

    await Area.find_one_or_fail(and_(Area.id == data.area_id,
                                     Area.user_id == user.id))

    area_season = await AreaSeason.create(**data.dict(), includes=['area'])

    return area_season
@router.get('/area_season/{area_season_id}')
async def get_area_season(area_season_id: int, user: User = Depends(get_current_user)) -> SAreaSeasonDetail:
    area_season = await AreaSeason.find_one_or_fail(filter=and_(AreaSeason.id == area_season_id,
                                                                Area.user_id == user.id),
                                                    includes=['area', 'soil_indicator_stats', 'satellite_stats'])

    return area_season





