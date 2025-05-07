# Humanas Login Tahmin Web Application
Bu repo, Humanas için hazırlanmış bir kullanıcı giriş tahmin web uygulamasına aittir. Uygulama backend için Python Django, frontend için React.js frameworklerini kullanmaktadır. İki farklı algoritma ile (mean interval ve exponential smoothing) sonraki kullanıcı giriş tarihini tahmin etmeye çalışır.
## Kurulum
### Backend Kurulumu
Terminalde yazmanız gerekenler:
```
git clone https://github.com/Huxvix/humanas_tahmin_app.git
cd humanas_tahmin_app
```
#### Sanal ortam oluşturmak isterseniz:
```
python -m venv env
```
#### Sanal ortamı aktifleştirmek için:
* Windows
```
venv/bin/activate
```
* Mac/Linux
```
source venv/bin/activate
```
#### Çalıştırmak için gerekli paketleri yüklemek için:
```
pip install -r requirements.txt
```
#### Ayrıca .env.example dosyasının sonundaki ".example" kısmını silip, kendi ortam değişkenlerinizi girebilirsiniz.
#### Migrasyonları tamamlamak için:
```
python manage.py migrate
```
#### Backend'i çalıştırmak için:
```
python manage.py runserver
```

### Frontend Kurulumu
#### Frontend dizinine geçin veya halen backend klasöründe iseniz aşağıdaki komutu çalıştırın:
```
cd ../tahmin_frontend
```
#### Paketleri yükleyin
```
npm install
```
#### Frontend sunucusu çalıştırma (geliştirme için):
```
npm run dev
```
