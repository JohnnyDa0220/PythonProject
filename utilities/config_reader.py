import configparser

def get_config():
    conf = configparser.ConfigParser()
    conf.read(r'config/configproperties.ini')
    return conf

def get_properties(section, value):
    config = get_config()
    data = config[section][value]
    return data