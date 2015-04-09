from flask import Flask



app = Flask(__name__)
app.DEBUG = True

@app.route("/")
def hello():
        return "hello world"

if __name__=="__main__":
    app.run(host = "166.111.5.226")

