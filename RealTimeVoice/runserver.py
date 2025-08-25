"""
This script runs the RealTimeVoice application using a development server.
"""

import array
from os import environ
from typing import Optional

import configobj
from flask import Config
from FlaskWebsite import app
from configobj import ConfigObj
from dataclasses import dataclass

@dataclass
class ConfigOptions:
    OPENAI_API_KEY: Optional[str] = None
    SERVER_HOST: str = 'localhost'
    SERVER_PORT: int = 5555

CONFIG_OPTIONS: ConfigOptions = ConfigOptions()
optional_config_keys: list = [ 'SERVER_HOST', 'SERVER_PORT' ]

# Prompt the user to input the configuration item and ask whether to save it as environment variable.
def request_config_item(key: str):
    print(f"Provide value for {key}: ", end="")
    value = input().strip()

    if value is None or value == "":
        raise ValueError(f"No value provided for {key}.")

    save_to_env = input(f"Save {key} as environment variable? (y/n): ").strip().lower()
    if save_to_env.startswith('y'):
        environ[key] = value

    return value

# Read configuration from multiple sources with precedence and build global config_options dictionary.
def read_configuration(): # type: ignore
    common_config_keys: list = [item for item in ConfigOptions.__annotations__.keys() if item not in optional_config_keys]

    config: dict = {}

    # Read configuration from environment variables
    for key in ConfigOptions.__annotations__.keys():
        value = environ.get(key)
        if value is not None:
            config[key] = value

    # Override with configuration from mandatory setup.cfg
    config_reader: ConfigObj = ConfigObj('setup.cfg')
    config.update(config_reader['settings'])

    # Override with configuration from optional setup_dev.cfg
    try:
        dev_config_reader: ConfigObj = ConfigObj('setup_dev.cfg')
        config.update(dev_config_reader['settings'])
    except FileNotFoundError:
        pass

    for key in ConfigOptions.__annotations__.keys():
        if CONFIG_OPTIONS.__dict__[key] is None:
            CONFIG_OPTIONS.__dict__[key] = request_config_item(key)

    return CONFIG_OPTIONS

if __name__ == '__main__':
    config: ConfigOptions = read_configuration()
    HOST = environ.get('SERVER_HOST', config.SERVER_HOST)
    PORT = int(environ.get('SERVER_PORT', config.SERVER_PORT))

    if(config.OPENAI_API_KEY is None or config.OPENAI_API_KEY == ""):
        raise ValueError("OPENAI_API_KEY environment variable is not set or is empty.")

    app.run(HOST, PORT)