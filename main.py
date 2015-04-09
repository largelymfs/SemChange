from flask import Flask, render_template



app = Flask(__name__)
app.DEBUG = True

@app.route("/")
def hello():
    return render_template("index.html")
if __name__=="__main__":
    app.run(host = "166.111.5.226")

