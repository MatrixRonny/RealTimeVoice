"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Response, render_template, jsonify, session
from RealTimeVoice import app
import os
import requests

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

    openai_api_key = os.environ.get('OPENAI_API_KEY')
    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': 'gpt-4o-realtime-preview-2025-06-03',
        'voice': 'verse'
    }

    # POST request to OpenAI API and return the session token.
    r = requests.post(
        'https://api.openai.com/v1/realtime/sessions',
        headers=headers,
        json=payload
    )
    data = r.json()
    session_token = data.client_secret.value
    return Response(session_token, mimetype='text/plain')

