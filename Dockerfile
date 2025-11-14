# 1. Adım: Temel Python imajını al
FROM python:3.11-slim

# 2. Adım: Çalışma dizinini ayarla
WORKDIR /app

# 3. Adım: Kütüphane listesini kopyala ve kur
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 4. Adım: Tüm uygulama kodunu kopyala
COPY . .

# 5. Adım: Cloud Run'ın kullanacağı portu belirt
# Bu port, app.py içindeki PORT değişkeni ile aynı olmalı
ENV PORT 8080

# 6. Adım: Konteyner çalıştığında hangi komutun çalışacağını belirt
# '0.0.0.0' tüm IP'lerden gelen istekleri dinlemesini sağlar
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]