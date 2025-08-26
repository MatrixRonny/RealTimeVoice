from mimetypes import init
from typing import Optional, TypeVar
from dataclasses import dataclass

T = TypeVar('T', bound=object)

@dataclass
class ConfigOptions:
    OPENAI_API_KEY: Optional[str] = None
    SERVER_HOST: str = 'localhost'
    SERVER_PORT: int = 5555

optional_config_keys: list = [ 'SERVER_HOST', 'SERVER_PORT' ]

from utility.configuration import update_configuration

def read_configuration() -> ConfigOptions:
    from utility.configuration import read_configuration
    return read_configuration(ConfigOptions, optional_config_keys)
