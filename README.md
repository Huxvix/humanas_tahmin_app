# Humanas Login Tahmin Web Application
Bu repo, Humanas için hazırlanmış bir kullanıcı giriş tahmin web uygulamasına aittir. Uygulama backend için Python Django, frontend için React Vite frameworklerini kullanmaktadır. İki farklı algoritma ile (mean interval ve median interval) sonraki kullanıcı giriş tarihini tahmin etmeye çalışır. Ayrıca bir arama fonksiyonu ile verinin fazla büyümesi durumunda kullanıcıya kolaylık sağlar.
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
#### Migrasyonları tamamlamak için:
```
python manage.py migrate
```
#### .env dosyası ile kendi environment variable'larınızı tanımlamalısınız.
Aşağıdaki bir örnek .env dosyasıdır.
```
SECRET_KEY =<django_secret_keyiniz>
DEBUG=True
REACT_APP_URL=http://localhost:5173
```
Kendi django key'inizi elde etmek için terminalde
```
django-admin shell
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```
Komutlarını kullanarak hızlıca bir Django key'i elde edebilirsiniz.
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
#### .env dosyası ile kendi environment variable'ınızı tanımlamalısınız.
Aşağıdaki, frontend'i kendi bilgisayarınızda çalıştırmanız için yeterli olacaktır.
```
VITE_API_BASE_URL=http://127.0.0.1:8000/
```
#### Frontend sunucusu çalıştırma:
```
npm run dev
```
