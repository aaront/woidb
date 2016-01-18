from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import woidb.config
import woidb.models

Session = sessionmaker()


def connect(connect_string, config_path=None):
    if connect_string is None:
        conf, cfg_path = woidb.config.read_db(config_path)
        if conf is None:
            raise IOError('Couldn\'t read config file in "{0}"'.format(cfg_path))
    return create_engine(connect_string)


@contextmanager
def create_session(connect_string, config_path=None):
    Session.configure(bind=connect(connect_string, config_path))
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
