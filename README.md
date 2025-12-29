# 🔐 Password Strength Checker
# Şifre Güç Kontrolcüsü

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey.svg)

**Terminal tabanlı şifre güvenlik analiz aracı**

*Developed by h3atwave*

</div>

---

## 📋 İçindekiler

- [Hakkında](#-hakkında)
- [Özellikler](#-özellikler)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Puanlama Sistemi](#-puanlama-sistemi)
- [Ekran Görüntüleri](#-ekran-görüntüleri)
- [Kod Yapısı](#-kod-yapısı)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

---

## 📖 Hakkında

**Password Strength Checker**, girilen şifrelerin güvenlik seviyesini analiz eden bir Python uygulamasıdır. Bu proje, hem bir şifre güvenlik aracı hem de Python programlama öğrenmek isteyenler için eğitici bir kaynak olarak tasarlanmıştır.

Her satır detaylı Türkçe yorumlarla açıklanmıştır, böylece kod okuyarak Python'ı öğrenebilirsiniz.

---

## ✨ Özellikler

| Özellik | Açıklama |
|---------|----------|
| 🔢 **Entropi Hesaplama** | Şifrenin matematiksel karmaşıklığını bit cinsinden ölçer |
| 📊 **Puan Sistemi** | 0-100 arası detaylı puanlama |
| 🚨 **Yaygın Şifre Kontrolü** | 40+ yaygın şifre veritabanı |
| 🔤 **Karakter Analizi** | Büyük/küçük harf, rakam, özel karakter kontrolü |
| 📱 **Ardışık Karakter Tespiti** | "abc", "123", "qwerty" gibi zayıf pattern'ları tespit eder |
| 💡 **Öneriler** | Şifreyi güçlendirmek için akıllı öneriler |
| 🎨 **Renkli Arayüz** | ANSI renk kodlarıyla görsel geri bildirim |

---

## 🚀 Kurulum

### Gereksinimler

- Python 3.6 veya üzeri
- Terminal/Komut satırı erişimi

### Adımlar

```bash
# 1. Projeyi klonlayın
git clone https://github.com/yourusername/password-checker.git

# 2. Proje klasörüne gidin
cd password-checker

# 3. Programı çalıştırın
python password_checker.py
```

> 💡 **Not:** Harici kütüphane kurulumu gerektirmez. Sadece Python'ın standart kütüphanelerini kullanır.

---

## 🎮 Kullanım

### Temel Kullanım

```bash
python password_checker.py
```

Program çalıştığında:
1. Şifrenizi girin ve Enter'a basın
2. Analiz sonuçlarını inceleyin
3. Önerilere göre şifrenizi güçlendirin
4. Çıkmak için `exit` yazın

### Komutlar

| Komut | Açıklama |
|-------|----------|
| `help` | Yardım menüsünü gösterir |
| `tips` | Güçlü şifre oluşturma ipuçları |
| `clear` | Ekranı temizler |
| `exit` | Programdan çıkar |

---

## 📊 Puanlama Sistemi

Şifreler 0-100 arası puanlanır:

| Puan | Güç Seviyesi | Açıklama |
|------|--------------|----------|
| 80-100 | 🟢 **Çok Güçlü** | Mükemmel! Bu şifre çok güvenli |
| 60-79 | 🟢 **Güçlü** | İyi seviye, çoğu uygulama için yeterli |
| 40-59 | 🟡 **Orta** | Kabul edilebilir ama geliştirilebilir |
| 20-39 | 🔴 **Zayıf** | Güçlendirme gerekli |
| 0-19 | 🔴 **Çok Zayıf** | Tehlikeli! Hemen değiştirin |

### Puanlama Kriterleri

```
UZUNLUK          : +25 puan (16+ karakter)
Küçük harf       : +10 puan
Büyük harf       : +10 puan
Rakam            : +10 puan
Özel karakter    : +10 puan
Yüksek entropi   : +20 puan
─────────────────────────────
CEZALAR:
Yaygın şifre     : -30 puan
Ardışık karakterler: -5 puan (her biri için)
```

---

## 📸 Ekran Görüntüleri

### Ana Ekran
```
══════════════════════════════════════════════════════════════════════

    ██╗  ██╗██████╗  █████╗ ████████╗██╗    ██╗ █████╗ ██╗   ██╗███████╗
    ██║  ██║╚════██╗██╔══██╗╚══██╔══╝██║    ██║██╔══██╗██║   ██║██╔════╝
    ███████║ █████╔╝███████║   ██║   ██║ █╗ ██║███████║██║   ██║█████╗  
    ██╔══██║ ╚═══██╗██╔══██║   ██║   ██║███╗██║██╔══██║╚██╗ ██╔╝██╔══╝  
    ██║  ██║██████╔╝██║  ██║   ██║   ╚███╔███╔╝██║  ██║ ╚████╔╝ ███████╗
    ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝

                    🔐 PASSWORD STRENGTH CHECKER 🔐
                          Gururla Sunar
══════════════════════════════════════════════════════════════════════
```

### Örnek Analiz Çıktısı
```
════════════════════════════════════════════════════════════
            📊 ŞİFRE ANALİZ RAPORU 📊
════════════════════════════════════════════════════════════

  Şifre:        M***************!
  Uzunluk:      18 karakter

  Güç:          ÇOK GÜÇLÜ
  Skor:         [████████████████████] 95/100
  Entropi:      107.18 bit

  ────────────────────────────────────────
  📝 KARAKTER ANALİZİ
  ────────────────────────────────────────
    ✓ Küçük harf (a-z)
    ✓ Büyük harf (A-Z)
    ✓ Rakam (0-9)
    ✓ Özel karakter (!@#$)

════════════════════════════════════════════════════════════
```

---

## 🏗️ Kod Yapısı

```
password_checker.py
│
├── class Colors           # ANSI renk kodları
│
├── def print_banner()     # ASCII art banner
├── def loading_animation()# Nokta nokta animasyonu
│
├── def calculate_entropy()     # Entropi hesaplama
├── def check_common_passwords()# Yaygın şifre kontrolü
├── def check_sequential_chars()# Ardışık karakter tespiti
│
├── def analyze_password() # Ana analiz fonksiyonu
├── def print_report()     # Sonuç raporlama
│
├── def print_help()       # Yardım menüsü
├── def print_tips()       # Şifre ipuçları
│
└── def main()             # Ana program döngüsü
```

### Kullanılan Kütüphaneler

| Kütüphane | Kullanım Amacı |
|-----------|----------------|
| `re` | Regex ile karakter pattern kontrolü |
| `math` | Entropi hesaplama (log2 fonksiyonu) |
| `time` | Animasyon gecikmeleri |
| `sys` | Terminal buffer kontrolü |
| `collections.Counter` | Karakter sayımı |

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! İşte nasıl katkıda bulunabileceğiniz:

1. Bu repo'yu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request açın

### Geliştirme Fikirleri

- [ ] Sözlük saldırısı simülasyonu
- [ ] Şifre kırılma süresi tahmini
- [ ] Çoklu şifre dosyası analizi
- [ ] GUI arayüz (Tkinter)
- [ ] API entegrasyonu (Have I Been Pwned)

---

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 👨‍💻 Geliştirici

**h3atwave**

- GitHub: [@h3atwave](https://github.com/musstafasnn)

---

<div align="center">

**⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

*Güvenli şifreler kullanın! 🔐*

</div>

