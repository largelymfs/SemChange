# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, Markup
from model import MSWord2Vec as word2vec
from prob import Prob
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

colors = {  0   :   "blue",
            1   :   "orange",
            2   :   "green",
            3   :   "yellow",
            4   :   "red"
            }


app = Flask(__name__)
app.DEBUG = True
#model = word2vec("../Data/vector_nyt-0.1.txt", "../Data/cluster_nyt-0.1.txt")
model = word2vec("./../Data/vector_rmrb-0.1.txt", "../Data/cluster_rmrb-0.1.txt", "./../Data/freq_demo.txt")
#model = word2vec("./../NewData/rmrb.vector-0.1.txt","./../NewData/rmrb.vector-0.1.txt","./../Data/freq_demo.txt")
prob = Prob("./../Data/rmrb.prob.afterextend")
#prob = Prob("./../NewData/rmrb.prob.all")

def search_result_oneword(word):
    global model
    return model.compute_kNN(word)

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
    global numbers, colors
    if request.method=='POST':
        word = request.form['word']
        word = word.strip()
        word = str(word)
        result, _  = search_result_oneword(word)
        result_old = result
        result_new = []
        for i, result_item in enumerate(result_old):
            maps = {"data" : result_item, "message": '''ui '''+colors[i] + ''' message'''}
            result_new.append(maps)
        TSV_String = prob.search(word)
    else:
        result_new = []
        TSV_String = prob.search("$$$")
    return render_template("oneword.html", itemlists = result_new, number = numbers[len(result_new)]+" column row", TSV_String = TSV_String)


if __name__=="__main__":
	app.run(host = "166.111.5.226", threaded = True)
