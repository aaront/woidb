
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, Date, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'
    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    position = Column(String(length=2))
    shoots = Column(String(length=1))
    birth_date = Column(Date)
    height = Column(Integer)
    weight = Column(Integer)

    def __repr__(self):
        return '<Player(name=\'{}, {}\' id={})>'.format(self.last_name, self.first_name, self.id)


class Team(Base):
    __tablename__ = 'teams'
    id = Column(String, primary_key=True)
    color = Column(String)
    color2 = Column(String)
    teamname = Column(String)
    city = Column(String)
    games = relationship('Game')

    def __repr__(self):
        return '<Team(id={})>'.format(self.teamname)


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    season = Column(String)
    status = Column(Integer)
    awayteam = Column(String, ForeignKey('teams.id'))
    hometeam = Column(String, ForeignKey('teams.id'))
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

    def __repr__(self):
        return '<Game(away={}, home={}, date={})>'.format(self.awayteam, self.hometeam, self.date)


