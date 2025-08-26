import os
from typing import Type, TypeVar
from os import environ
from configobj import ConfigObj

T = TypeVar('T', bound=object)

def set_environment_variable(key: str, value: str):
    if(os.name == 'nt'):
        command = f'setx {key} "{value}"'
    else:
        command = f'export {key}="{value}"'
    os.system(command)

# Prompt the user to input the configuration item and ask whether to save it as environment variable.
def request_config_item(key: str):
    value: str
    try:
        print(f"Provide value for {key}: ", end="")
        value = input().strip()
        if value is None or value == "":
            raise ValueError(f"No value provided for {key}.")
    except KeyboardInterrupt:
        raise ValueError(f"No value provided for {key}.")

    save_to_env = input(f"Save {key} as environment variable? (y/n): ").strip().lower()
    if save_to_env.startswith('y'):
        set_environment_variable(key, value)

    return value

# Read configuration from multiple sources with precedence and build global config_options dictionary.
def read_configuration(config_cls: Type[T], optional_config_keys: list[str]) -> T:
    common_config_keys: list = [item for item in config_cls.__annotations__.keys() if item not in optional_config_keys]

    config: dict = {}

    # Read configuration from environment variables
    for key in config_cls.__annotations__.keys():
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
    except (FileNotFoundError, KeyError):
        pass

    # Prompt for any missing configuration items
    config_options: T = config_cls(**config)
    for key in config_cls.__annotations__.keys():
        if getattr(config_options, key) in [None, '']:
            setattr(config_options, key, request_config_item(key))

    return config_options

# Assign configuration from @dataclass object to same class.
def update_configuration(config_cls: Type[T], config: T) -> None:
    for key in config_cls.__annotations__.keys():
        setattr(config_cls, key, getattr(config, key))