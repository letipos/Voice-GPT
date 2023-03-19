import configparser

config = configparser.ConfigParser()
config_file = 'config.example'

config.add_section('API')
config.set('API', 'key', 'your-api-key')
config.set('API', 'secret', 'your-api-secret')
with open(config_file, 'w') as f:
    config.write(f)
