"""
This script runs the RealTimeVoice application using a development server.
"""

from os import environ
from FlaskWebsite import app

from settings import ConfigOptions, read_configuration, update_configuration

if __name__ == '__main__':
    try:
        config = read_configuration()
        update_configuration(ConfigOptions, config)
        HOST = environ.get('SERVER_HOST', config.SERVER_HOST)
        PORT = int(environ.get('SERVER_PORT', config.SERVER_PORT))
    except Exception as e:
        print()
        print(f"Error reading configuration: {e}")
        exit(1)

    app.run(HOST, PORT)