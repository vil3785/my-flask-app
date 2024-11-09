from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == '__main__':
    # 运行 Flask 应用，设置 host='0.0.0.0' 以便可以从外部网络访问
    app.run(host='0.0.0.0', port=5000)