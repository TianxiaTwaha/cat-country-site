from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "maomao123654site"

USER_NAME = "cat"
USER_PWD = "123456"

articles = []


@app.route("/login", methods=["GET", "POST"])
def login():
    err = ""
    if request.method == "POST":
        uname = request.form.get("username")
        pwd = request.form.get("password")
        if uname == USER_NAME and pwd == USER_PWD:
            session["is_login"] = True
            return redirect(url_for("index"))
        else:
            err = "账号或密码错误！"
    return render_template("login.html", error=err)


@app.route("/")
def index():
    if not session.get("is_login"):
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/get_articles")
def get_articles():
    return jsonify(articles)


@app.route("/publish", methods=["POST"])
def publish():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    content = (data.get("content") or "").strip()
    if not title or not content:
        return jsonify({"status": "error", "msg": "标题和内容不能为空"})

    articles.insert(0, {
        "title": title,
        "content": content,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
