from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def dashboard():
    flash("hello")
    flash("invalid password")
    flash("error")
    return render_template("dotcombubble.html")


if __name__ == '_main_':
    app.run()
