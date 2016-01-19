
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'
    id = Column(SmallInteger, primary_key=True)
    name = Column(String, index=True)
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
    id = Column(SmallInteger, primary_key=True)
    name = Column(String)
    full_name = Column(String)
    city = Column(String)
    color = Column(String)
    color2 = Column(String)

    def __repr__(self):
        return '<Team(id={})>'.format(self.id)


class Game(Base):
    __tablename__ = 'games'
    id = Column(BigInteger, primary_key=True)
    season = Column(SmallInteger)
    status = Column(SmallInteger)
    away_team = Column(SmallInteger, ForeignKey('teams.id'))
    home_team = Column(SmallInteger, ForeignKey('teams.id'))
    away_score = Column(Integer)
    home_score = Column(Integer)
    datetime = Column(DateTime, index=True)
    duration = Column(Time)
    periods = Column(Integer)
    away_after_away = Column(Boolean)
    away_after_home = Column(Boolean)
    home_after_away = Column(Boolean)
    home_after_home = Column(Boolean)

    def __repr__(self):
        return '<Game(away={}, home={}, date={})>'.format(self.awayteam, self.hometeam, self.date)


class GameEvent(Base):
    __tablename__ = 'gameevents'
    id = Column(BigInteger, primary_key=True)
    game = Column(Integer, ForeignKey('games.id'))
    event_type = Column(SmallInteger)
    team = Column(SmallInteger, ForeignKey('teams.id'))
    elapsed = Column(Float)
    away_player1 = Column(SmallInteger, ForeignKey('players.id'))
    away_player2 = Column(SmallInteger, ForeignKey('players.id'))
    away_player3 = Column(SmallInteger, ForeignKey('players.id'))
    away_player4 = Column(SmallInteger, ForeignKey('players.id'))
    away_player5 = Column(SmallInteger, ForeignKey('players.id'))
    home_player1 = Column(SmallInteger, ForeignKey('players.id'))
    home_player2 = Column(SmallInteger, ForeignKey('players.id'))
    home_player3 = Column(SmallInteger, ForeignKey('players.id'))
    home_player4 = Column(SmallInteger, ForeignKey('players.id'))
    home_player5 = Column(SmallInteger, ForeignKey('players.id'))
    player1 = Column(SmallInteger, ForeignKey('players.id'))
    player2 = Column(SmallInteger, ForeignKey('players.id'))
    player3 = Column(SmallInteger, ForeignKey('players.id'))
    home_zone = Column(SmallInteger)
    home_score = Column(SmallInteger)
    away_score = Column(SmallInteger)
    duration = Column(Interval)
    away_goalie = Column(SmallInteger, ForeignKey('players.id'))
    home_goalie = Column(SmallInteger, ForeignKey('players.id'))
    distance = Column(Float)
    shot_feature = Column(SmallInteger)
    x_coord = Column(SmallInteger)
    y_coord = Column(SmallInteger)

    def __repr__(self):
        return '<GameEvent(type={}, team={})>'.format(self.event_type, self.team)
