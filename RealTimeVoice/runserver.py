"""
This script runs the RealTimeVoice application using a development server.
"""

from os import environ
from RealTimeVoice import app

from config_dev import *

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    if(environ.get('OPENAI_API_KEY') is None or environ.get('OPENAI_API_KEY') == ''):
        raise ValueError("OPENAI_API_KEY environment variable is not set or is empty.")

    app.run(HOST, PORT)
