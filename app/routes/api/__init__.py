from app import app
from flask import request
from app.modules.urls_tools import *


@app.route('/api/create-url', method=['GET', 'POST'])
def api_create_url():
    if request.method == 'POST':
        data = request.get_json()
        if 'url' not in data or not data['url']:
            return {'short_url': '', 'error': 300}
        return {'short_url': add_url(data['url']).short_url, 'error': 100}
    return {'short_url': '', 'error': 200}


@app.route('/api/check-short-url', methods=['GET', 'POST'])
def api_check_short_url():
    if request.method == 'POST':
        data = request.get_json()

        if 'url' not in data or not data['short_url']:
            return {'valid': False, 'error': 300}
        url = get_url_by_short_url(data['short_url']).url

        if url:
            return {'valid': True, 'error': 100}

        return {'valid': False, 'error': 100}
    return {'valid': False, 'error': 200}
