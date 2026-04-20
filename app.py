from flask import Flask

import os

app = Flask(__name__)

@app.route('/')
def hello():
    build_id = os.getenv('BUILD_ID', 'Local')
    return f"<h1>Hello, world from flask!</h1><p>Deploy via jenkins webhook. Build  ID: {build_id}</p><p>checking the workflow</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

