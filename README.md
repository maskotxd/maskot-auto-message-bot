# Kurulum

## 1. Projeyi İndirin

GitHub reposunu klonlayın:

```bash
git clone https://github.com/maskotxd/maskot-auto-message-bot.git
```

Klasöre girin:

```bash
cd maskot-auto-message-bot
```

veya ZIP olarak indirip çıkartın.

---

## 2. Python Kurulumu

Bilgisayarınızda Python 3.10 veya üzeri bir sürümün kurulu olduğundan emin olun.

Kontrol etmek için:

```bash
python --version
```

veya

```bash
python3 --version
```

---

## 3. Gerekli Kütüphaneleri Kurun

```bash
pip install -r requirements.txt
```

Alternatif:

```bash
pip3 install -r requirements.txt
```

---

## 4. API Bilgilerini Düzenleyin

`maskot.py` dosyasını açın.

Aşağıdaki alanları kendi bilgilerinizle değiştirin:

```python
api_id = API_ID_BURAYA
api_hash = "API_HASH_BURAYA"
```

API bilgilerinizi almak için:

https://my.telegram.org

adresine giriş yapıp **API Development Tools** bölümünden yeni uygulama oluşturabilirsiniz.

---

## 5. Grup ID'lerini Düzenleyin

`maskot.py` içerisinde:

```python
groups = [
    GRUP_ID_1,
    GRUP_ID_2,
    GRUP_ID_3
]
```

alanını kendi grup ID'lerinizle değiştirin.

---

## 6. Gönderilecek Mesajı Düzenleyin

`maskot.py` içerisinde:

```python
message = "GONDERILECEK_MESAJ"
```

alanını istediğiniz mesaj ile değiştirin.

---

## 7. Botu Çalıştırın

Terminal veya CMD üzerinden:

```bash
python maskot.py
```

komutunu çalıştırın.

---

## 8. İlk Giriş

İlk çalıştırmada Telegram hesabınıza giriş yapmanız istenir.

Telefon numaranızı girin:

```text
Please enter your phone:
```

Ardından Telegram'dan gelen doğrulama kodunu girin.

Başarılı giriş sonrası proje klasöründe:

```text
session.session
```

dosyası oluşacaktır.

Bu dosya oturum bilgilerinizi saklar ve sonraki çalıştırmalarda tekrar giriş yapmanız gerekmez.

---

## Çalışma Mantığı

* Listedeki gruplara sırayla mesaj gönderilir.
* Her mesaj arasında 20-30 saniye rastgele beklenir.
* Tüm gruplar tamamlandıktan sonra 10 dakika beklenir.
* İşlem sonsuz döngü halinde devam eder.

---

## Durdurma

Botu durdurmak için:

```text
CTRL + C
```

tuşlarına basmanız yeterlidir.

---

## Dosya Yapısı

```text
maskot-auto-message-bot
├── .gitignore
├── maskot.py
├── requirements.txt
└── README.md
```
