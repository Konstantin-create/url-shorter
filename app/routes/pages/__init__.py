from app import app
from flask import render_template, request, redirect

from app.modules import content_tools
from app.modules import urls_tools


@app.route('/')
def index_page():
    return render_template('index_page.html', content_data=content_tools.get_content())


@app.route('/about/<string:short_url>')
def about_page(short_url: str):
    url = urls_tools.get_url_by_short_url(short_url)
    return render_template(
        'about_page.html',
        content_data=content_tools.get_content(),
        server_ip=request.host_url,
        url=url
    )


@app.route('/short-url', methods=['GET', 'POST'])
def short_url_handler():
    if request.method == 'POST':
        url = request.form.get('url')
        url_obj = urls_tools.add_url(url)

        return redirect(f'/about/{url_obj.short_url}')
