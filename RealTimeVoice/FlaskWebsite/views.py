"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Response, render_template, jsonify, session
from FlaskWebsite import app
import os
import requests

from config_dev import OPENAI_API_KEY

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/get-token')
def get_token():
    """Retrieve ephemeral session token from OpenAI."""

    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'instructions': 'You are a chatty real-time voice assistant that does not mind talking about anything. You only know and discuss in English.',
        'model': 'gpt-4o-realtime-preview-2025-06-03',
        'voice': 'verse',
        'input_audio_transcription': {
            'language': 'en',
            'model': 'whisper-1'
        }
    }

    # POST request to OpenAI API and return the session token.
    r = requests.post(
        'https://api.openai.com/v1/realtime/sessions',
        headers=headers,
        json=payload
    )
    data = r.json()
    session_token = data['client_secret']['value']
    return Response(session_token, mimetype='text/plain')

@app.route('/realtime-voice')
def realtime_voice():
    return render_template('realtime-voice.html')
