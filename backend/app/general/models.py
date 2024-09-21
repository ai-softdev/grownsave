from sqlalchemy import Column, JSON, Integer, ForeignKey, String, DateTime, func, Enum, Float, select
from sqlalchemy.orm import Mapped, relationship, joinedload, contains_eager

from app.database import async_session_maker
from app.general.enums import StatsTypes
from app.repository.base import Base


class Country(Base):
    names = Column(JSON)
    regions = relationship("Region", back_populates='country')


class Region(Base):
    names = Column(JSON)
    country_id = Column(ForeignKey('countries.id', ondelete='cascade'))
    country = relationship(Country, back_populates='regions')
    districts = relationship("District", back_populates='region')


class District(Base):
    names = Column(JSON)
    system_name = Column(String)
    region_id = Column(ForeignKey('regions.id', ondelete='cascade'))
    region = relationship(Region, back_populates='districts')
    coordinates = Column(JSON)
    stats = relationship("GeneralStats", back_populates='district')

    @classmethod
    async def get_with_stats(cls, filter=None):
        async with async_session_maker() as session:
            query = select(cls).join(cls.stats).options(contains_eager(cls.stats))
            if filter is not None:
                query = query.filter(filter)
            result = await session.execute(query)
            return result.unique().scalars().all()


class GeneralStats(Base):
    district_id = Column(ForeignKey('districts.id', ondelete='cascade'))
    district = relationship(District, back_populates='stats')
    info = Column(JSON)
    date = Column(DateTime)
    result = Column(Float)
