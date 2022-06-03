from recom import search , search_by_keyword
from flask import Flask,render_template ,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Flim.html")

@app.route("/result" , methods=["POST","GET"])
def res():
    if request.method =="POST":
        title,genre,rating,releas,pr,nr,nur = search(request.form["movie_name"], int(request.form["numbers"]),int(request.form["rate"]))
        x = zip(title,genre,rating,releas,pr,nr,nur)
        return render_template("result.html", x = x)

    return render_template("Flim.html")


@app.route("/keyword", methods=["POST","GET"])
def key():
    if request.method =="POST":
        title,genre,rating,releas,pr,nr,nur = search_by_keyword(request.form["keyw"], int(request.form["numbers"]), int(request.form["rate"]))
        x = zip(title,genre,rating,releas,pr,nr,nur)
        return render_template("keyresult.html", x = x)
    return render_template("keyword.html")

if __name__ == "__main__":
    app.run(debug=True)