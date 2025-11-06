# 1

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello Bhuva! App auto-deployed via Ansible + GitHub Actions."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8004)

