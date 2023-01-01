from app import app
from flask import request


@app.route('/api/create-url', method=['GET', 'POST'])
def api_create_url():
    if request.method == 'POST':
        pass
    return {'error': 300}