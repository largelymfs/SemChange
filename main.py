# -*- coding:utf-8 -*-
from flask import Flask, render_template, request
from model import MSWord2Vec as word2vec
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

numbers = {0 : "zero",
           1 : "one",
           2 : "two",
           3 : "three",
           4 : "four",
           5 : "five",
           6 : "six"}

app = Flask(__name__)
app.DEBUG = True
#model = word2vec("../Data/vector_nyt-0.1.txt", "../Data/cluster_nyt-0.1.txt")
model = word2vec("./../Data/vector_rmrb-0.1.txt", "../Data/cluster_rmrb-0.1.txt", "./../Data/freq_demo.txt")
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
    global numbers
    if request.method=='POST':
        word = request.form['word']
        word = word.strip()
        word = str(word)
        result = search_result_oneword(word)
    else:
        result = []

    return render_template("oneword.html", itemlists = result, number = numbers[len(result)]+" column row")


if __name__=="__main__":
	app.run(host = "166.111.5.226", threaded = True)
