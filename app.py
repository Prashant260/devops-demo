from flask import Flask

app = Flask(__name__)

@app.routes("/")
def hello():
    return "hello from devops_engineer"

app.run(host="0.0.0.0", port:5000 )
