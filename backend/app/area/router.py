from fastapi import APIRouter, Depends
from sqlalchemy import and_

from app.area.models import Area, AreaSeason
from app.area.schemas import SAreaList, SAreaDetail, SAreaSeasonDetail
from app.repository.tools import get_list_data
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
                                       includes=['seasons'])
    return area


@router.get('/area_season/{area_season_id}')
async def get_area_season(area_season_id: int, user: User = Depends(get_current_user)) -> SAreaSeasonDetail:
    area_season = await AreaSeason.find_one_or_none(filter=and_(AreaSeason.id == area_season_id,
                                                                Area.user_id == user.id), includes=['area'])
    return area_season



