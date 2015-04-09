# -*- coding:utf-8 -*-
from flask import Flask, render_template, request
from model import MSWord2Vec as word2vec
import sys
reload(sys)
sys.setdefaultencoding("utf-8")



app = Flask(__name__)
app.DEBUG = True
#model = word2vec("../Data/vector_nyt-0.1.txt", "../Data/cluster_nyt-0.1.txt")
model = word2vec("./../Data/vector_rmrb-0.1.txt", "../Data/cluster_rmrb-0.1.txt")
def search_result_oneword(word):
    global model
    return model.compute_kNN(word, 10)

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
        print type(word), word
        word = str(word)
        print type(word), word
        result = search_result_oneword(word)
        print result
    else:
        result = None
    return render_template("oneword.html")


if __name__=="__main__":
	app.run(host = "166.111.5.226")
