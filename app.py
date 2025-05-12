import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    user_ip = request.remote_addr
    return f"<h2>Ваша IP-адреса: {user_ip}</h2>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
