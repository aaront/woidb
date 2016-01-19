import csv
import os.path

from dateutil.parser import parse

import woidb.models as models


def _get_team_name(shortname):
    if shortname is 'PHX':
        return 'ARZ'
    if shortname is 'ATL':
        return 'WPG'
    return shortname


def _get_tz_infos():
    tz_infos = {
        'EST': -5,
        'ET': -5,
        'EDT': -4,
        'CST': -6,
        'CT': -6,
        'CDT': -5,
        'MT': -7,
        'MST': -7,
        'MDT': -6,
        'PST': -8,
        'PT': -8,
        'PDT': -7
    }
    for info in tz_infos:
        tz_infos[info] *= 3600
    return tz_infos


def _importer(file_path):
    name = os.path.basename(file_path)
    if name == 'games.csv':
        return _load_game
    if name == 'roster.unique.csv':
        return _load_player
    if name == 'teamcolors.csv':
        return _load_team
    return None


def import_csv(file_path, session):
    if not os.path.exists(file_path):
        raise IOError('File "{}" does not exist'.format(file_path))

    importer = _importer(file_path)
    if importer is None:
        return
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            importer(session, row)


def _load_team(session, row):
    team = models.Team(id=int(row['']), name=row['team'], full_name=row['TeamName'],
                       city=row['SchedTeamName'], color=row['color'], color2=row['color2'])
    session.merge(team)


def _load_game(session, row):
    if not row['date']:
        return
    id = int(row['season'] + row['gcode'])
    season = int(str(row['season'])[0:4])
    awayteam = session.query(models.Team).filter_by(name=_get_team_name(row['awayteam'])).first()
    hometeam = session.query(models.Team).filter_by(name=_get_team_name(row['hometeam'])).first()
    start_time = row['game.start'] if row['game.start'] != 'NA' else ''
    end_time = row['game.end'] if row['game.end'] != 'NA' else ''
    game_start = parse('{} {}'.format(row['date'], start_time), tzinfos=_get_tz_infos())
    game_end = parse('{} {}'.format(row['date'], end_time), tzinfos=_get_tz_infos())
    duration = None
    if end_time:
        duration = game_end - game_start
    awayafteraway = bool(int(row['awayafteraway']))
    awayafterhome = bool(int(row['awayafterhome']))
    homeafteraway = bool(int(row['homeafteraway']))
    homeafterhome = bool(int(row['homeafterhome']))
    game = models.Game(id=id, season=season, status=int(row['status']), away_team=awayteam.id, home_team=hometeam.id,
                       away_score=int(row['awayscore']), home_score=int(row['homescore']),
                       datetime=game_start, duration=duration, periods=int(row['periods']),
                       away_after_away=awayafteraway, away_after_home=awayafterhome,
                       home_after_away=homeafteraway, home_after_home=homeafterhome)
    session.merge(game)


def _load_player(session, row):
    pass
