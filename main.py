from flask import Flask, render_template, request




app = Flask(__name__)
app.DEBUG = True

def shutdown_server():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route("/")
def hello():
    return "hello"
    #return render_template("index.html")

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__=="__main__":
    app.run(host = "166.111.5.226", port=8888)

