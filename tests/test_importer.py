import os
import unittest

from woidb.db import connect, Session
from woidb.importers.woi import import_csv
from woidb.models import Base, Team


class TestImporter(unittest.TestCase):
    def setUp(self):
        self.engine = connect('sqlite://')
        Session.configure(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_team(self):
        import_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'teamcolors.csv'), self.session)
        teams = self.session.query(Team).all()
        self.assertEqual(32, len(teams))
