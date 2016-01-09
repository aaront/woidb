import csv
import os.path

import woidb.db as db
import woidb.models as models


def _importer(file_path):
    name = os.path.basename(file_path)
    if name == 'games.csv':
        return _load_game
    if name == 'roster.unique.csv':
        return _load_player
    if name == 'teamcolors.csv':
        return _load_team
    return None


def import_csv(file_path):
    if not os.path.exists(file_path):
        raise IOError('File "{}" does not exist'.format(file_path))

    importer = _importer(file_path)
    if importer is None:
        return
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        with db.create_session() as session:
            for row in reader:
                importer(session, row)


def _load_team(session, row):
    team = models.Team(id=row['team'], name=row['TeamName'], city=row['SchedTeamName'],
                       color=row['color'], color2=row['color2'])
    session.merge(team)
    pass


def _load_game(session, row):
    pass


def _load_player(session, row):
    pass
