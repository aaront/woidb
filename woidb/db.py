from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import woidb.config
import woidb.models

Session = sessionmaker()


def connect(database=None, user=None, password=None, host=None, port=None, config_path=None):
    if database is None:
        conf, cfg_path = woidb.config.read_db(config_path)
        if conf is None:
            raise IOError('Couldn\'t read config file in "{0}"'.format(cfg_path))
        database, user, password = conf['database'], conf['user'], conf['password']
        host, port = conf['host'], conf['port']
    if not host:
        host = 'localhost'
    if not port:
        port = 5432
    return create_engine('postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, database))


@contextmanager
def create_session(database=None, user=None, password=None, host=None, port=None, config_path=None):
    Session.configure(bind=connect(database, user, password, host, port, config_path))
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def init(database=None, user=None, password=None, host=None, port=None):
    engine = connect(database, user, password, host, port)
    woidb.models.Base.metadata.create_all(engine)