from flask import Flask, request, jsonify, render_template, redirect
app = Flask(__name__)


@app.route('/')
def toinedx():
    return redirect('/index.html')


@app.route('/index.html')
def index():
    return render_template('/index.html')


@app.route('/test', methods=["POST"])
def calculate():
    params = request.form if request.form else request.json
    print(params)
    a = params.get("a", 0)
    b = params.get("b", 0)
    c = a + b
    res = {"result": c}
    return jsonify(content_type='application/json;charset=utf-8',
                   reason='success',
                   charset='utf-8',
                   status='200',
                   content=res)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            threaded=True,
            debug=True,
            port=8081)
