from app import app
from flask import render_template

from app.modules import content_tools


@app.route('/')
def index_page():
    return render_template('index_page.html', content_data=content_tools.get_content())
