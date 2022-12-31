from app import app
from flask import render_template, request

from app.modules import content_tools
from app.modules import urls_tools


@app.route('/')
def index_page():
    return render_template('index_page.html', content_data=content_tools.get_content())


@app.route('/short-url', methods=['GET', 'POST'])
def short_url_handler():
    if request.method == 'POST':
        url = request.form.get('url')
        urls_tools.add_url(url)

        return ''
