from typing import List

from sqlalchemy import Column, ForeignKey, String, JSON, DateTime, Date, Boolean, select, desc
from sqlalchemy.orm import relationship, contains_eager

from app.database import async_session_maker
from app.repository.base import Base


class Area(Base):
    user = relationship("User", back_populates="areas")
    user_id = Column(ForeignKey('users.id', ondelete='cascade'))
    name = Column(String)
    coordinates = Column(JSON)
    seasons = relationship('AreaSeason', back_populates='area')
    soil_indicators = relationship("SoilIndicator", back_populates="area")


class AreaSeason(Base):
    culture_name = Column(String)
    area_id = Column(ForeignKey('areas.id', ondelete='cascade'))
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    area = relationship('Area', back_populates='seasons')
    soil_indicator_stats = relationship('SoilIndicatorStats', back_populates='area_season')
    satellite_stats = relationship('SatelliteStats')


    @classmethod
    async def first(cls, filter, includes: List[str] = None):
        async with async_session_maker() as session:

            query = select(cls).filter(filter).order_by(cls.area_id, cls.start_date.desc()).limit(1)
            if includes:
                for include in includes:
                    query = query.options(cls.build_joinedload(include))

            result = await session.execute(query)
            return result.unique().scalars().all()


class SoilIndicator(Base):
    created_at = Column(Date)
    area_id = Column(ForeignKey('areas.id', ondelete='cascade'))
    device_id = Column(String)
    working_status = Column(Boolean, default=True)
    area = relationship("Area", back_populates="soil_indicators")


class SoilIndicatorStats(Base):
    datetime = Column(DateTime)
    soil_indicator_id = Column(ForeignKey('soilindicators.id'), )
    info = Column(JSON, nullable=False)
    area_season_id = Column(ForeignKey('areaseasons.id', ondelete='CASCADE'))
    area_season = relationship('AreaSeason', back_populates='soil_indicator_stats')
    result = Column(JSON)

    @classmethod
    async def first(cls, filter, includes: List[str] = None):
        async with async_session_maker() as session:

            query = select(cls).filter(filter).order_by(cls.area_season_id, cls.datetime.desc()).limit(1)
            if includes:
                for include in includes:
                    query = query.options(cls.build_joinedload(include))

            result = await session.execute(query)
            return result.unique().scalars().all()


class SatelliteStats(Base):
    date = Column(Date, nullable=False)
    area_season_id = Column(ForeignKey('areaseasons.id'))
    result = Column(JSON)
    info = Column(JSON)
