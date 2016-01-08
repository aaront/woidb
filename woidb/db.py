import os
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

from sqlalchemy import create_engine

import woidb.models


def config(config_path):
    if not config_path:
        config_path = os.path.join(os.path.expanduser('~'), '.woidb.ini')
    conf = configparser.ConfigParser()
    conf.read(config_path)
    try:
        database = conf.get('db', 'database')
        user = conf.get('db', 'user')
        password = conf.get('db', 'password')
        host = conf.get('db', 'host')
        port = conf.get('db', 'port')

        return dict(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        ), config_path
    except configparser.NoSectionError:
        return None, config_path
    except configparser.NoOptionError:
        return None, config_path


def connect(database=None, user=None, password=None, host=None, port=None, config_path=None):
    if database is None:
        conf, cfg_path = config(config_path)
        if conf is None:
            raise IOError('Couldn\'t read config file in "{0}"'.format(cfg_path))
        database, user, password = conf['database'], conf['user'], conf['password']
        host, port = conf['host'], conf['port']
    if host is None:
        host = 'localhost'
    if port is None:
        port = 5432
    return create_engine('postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, database))


def init(database=None, user=None, password=None, host=None, port=None):
    engine = connect(database, user, password, host, port)
    woidb.models.Base.metadata.create_all(engine)