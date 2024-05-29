from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World! This is a secure webpage."


if __name__ == "__main__":
    app.run(ssl_context=("cert.pem", "key.pem"), debug=True)
