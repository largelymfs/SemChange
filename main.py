from flask import Flask, render_template, request
from model import MSWord2Vec as word2vec




app = Flask(__name__)
app.DEBUG = True
model = word2vec("../Data/vector_nyt-0.1.txt", "../Data/cluster_nyt-0.1.txt")

def search_result_oneword(word):
    return None

def shutdown_server():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route("/")
def hello():
    #return "hello"
    return render_template("index.html")

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@app.route('/oneword', methods=["POST", "GET"])
def oneword():
    if request.method=='POST':
        word = request.form['word']
        result = search_result_oneword(word)
    else:
        result = None
    return render_template("oneword.html")


if __name__=="__main__":
	app.run(host = "166.111.5.226")
