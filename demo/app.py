from flask import (
    Flask,
    render_template,
    request,
)

from demo.api.manager import ApiManager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    api = ApiManager()
    results = api.search(keyword)

    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
