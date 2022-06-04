from recom import search , search_by_keyword , listt
from flask import Flask,render_template ,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Flim.html")

@app.route("/result" , methods=["POST","GET"])
def res():
    if request.method =="POST":
        title,genre,rating,releas,pr,nr,nur,img = search(request.form["movie_name"], int(request.form["numbers"]),int(request.form["rate"]))
        x = zip(title,genre,rating,releas,pr,nr,nur,img)
        return render_template("result.html", x = x)

    return render_template("Flim.html")


@app.route("/keyword", methods=["POST","GET"])
def key():
    if request.method =="POST":
        title,genre,rating,releas,pr,nr,nur,img = search_by_keyword(request.form["keyw"], int(request.form["numbers"]), int(request.form["rate"]))
        x = zip(title,genre,rating,releas,pr,nr,nur,img)
        return render_template("keyresult.html", x = x)
    return render_template("keyword.html")


@app.route("/list")
def listtt():
    title,genre,rating,releas,pr,nr,nur,img = listt()
    x = zip(title,genre,rating,releas,pr,nr,nur,img)
    return render_template("list.html",x = x)


if __name__ == "__main__":
    app.run(debug=True)