import os
try:
    import ConfigParser as configparser
except ImportError:
    import configparser


def _config(config_path):
    if not config_path:
        config_path = os.path.join(os.path.expanduser('~'), '.woidb.ini')
    conf = configparser.ConfigParser()
    conf.read(config_path)
    return conf, config_path


def read_db(config_path=None):
    conf, config_path = _config(config_path)
    try:
        return conf.get('db', 'connect'), config_path
    except configparser.NoSectionError:
        return None, config_path
    except configparser.NoOptionError:
        return None, config_path


def save_db(connection, config_path=None):
    conf, config_path = _config(config_path)
    if 'db' not in conf.sections():
        conf.add_section('db')
    conf.set('db', 'connect', connection if connection else '')
    with open(config_path, 'w') as config_file:
        conf.write(config_file)
