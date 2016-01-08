
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, Date, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Team(Base):
    __tablename__ = 'teams'
    id = Column(String, primary_key=True)
    color = Column(String)
    color2 = Column(String)
    teamname = Column(String)
    city = Column(String)
    games = relationship('Game')


class Game(Base):
    __tablename__ = 'games'
    id = Column(String, primary_key=True)
    season = Column(String)
    status = Column(Integer)
    awayteam = Column(String, ForeignKey('teams.id'))
    hometeam = Column(String)
    awayscore = Column(Integer)
    homescore = Column(Integer)
    date = Column(Date)
    game_start = Column(Time)
    game_end = Column(Time)
    periods = Column(Integer)
    awaycorsi = Column(Integer)
    homecorsi = Column(Integer)
    awayafteraway = Column(Boolean)
    awayafterhome = Column(Boolean)
    homeafteraway = Column(Boolean)
    homeafterhome = Column(Boolean)


