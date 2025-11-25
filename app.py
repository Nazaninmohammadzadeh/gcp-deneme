import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Cloud Run'ın otomatik olarak sağladığı PORT değişkenini okur
    # Eğer bu değişken yoksa, lokalde test için 8080 portunu kullanır
    port = int(os.environ.get('PORT', 8080))
    return f"Merhaba CI/CD! Otomasyon çalışıyor! Port: {port} V4"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))