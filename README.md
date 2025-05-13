
# 📝 Task Manager API

Bu proje, FastAPI kullanarak geliştirilmiş basit bir görev yönetimi (CRUD) REST API uygulamasıdır. Görev ekleme, listeleme, güncelleme ve silme işlemleri yapılabilir.

## 🚀 Kullanılan Teknolojiler

- Python 3.12
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Swagger UI (otomatik dokümantasyon)

## ⚙️ Kurulum

1. Bu repoyu klonla:
   ```bash
   git clone https://github.com/mregodd/task-manager-api.git
   cd task-manager-api
   ```

2. Sanal ortam oluştur:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate       # Windows
   ```

3. Gerekli paketleri yükle:
   ```bash
   pip install -r requirements.txt
   ```

4. Uygulamayı başlat:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Tarayıcıdan aç:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## 🔮 Geliştirme Planları

- [ ] Docker ile container haline getirme  
- [ ] JWT ile kullanıcı doğrulama  
- [ ] Unit test (pytest)  
- [ ] Frontend arayüz (React/Vue ile)

---
