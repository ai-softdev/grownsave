from sqlalchemy import Column, JSON, Integer, ForeignKey, String, DateTime, func, Enum
from sqlalchemy.orm import Mapped, relationship

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


class GeneralStats(Base):
    district_id = Column(ForeignKey('districts.id', ondelete='cascade'))
    district = relationship(District, back_populates='stats')
    info = Column(JSON)
    date = Column(DateTime, default=func.now())
    type = Column(Enum(StatsTypes))
