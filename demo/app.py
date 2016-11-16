from flask import (
    Flask,
    render_template,
    request,
)

from demo.api.clients.base import DumbCache
from demo.api.manager import ApiManager

app = Flask(__name__)
api_cache = DumbCache()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    return render_template('results.html', keyword=keyword)


@app.route('/results', methods=['POST'])
def get_results():
    keyword = request.form.get('keyword')
    api = ApiManager(api_cache)
    results = api.search(keyword)
    return render_template('results_content.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
