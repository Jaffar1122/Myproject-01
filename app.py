from flask import Flask

app = Flask("myproject")

@app.route("/")
def home():
    return "Hello, this is my Flask app deployed on Kubernetes!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

