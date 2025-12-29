
# 📖 KOD AÇIKLAMA REHBERİ
## Password Strength Checker - Satır Satır Açıklama

Bu belge, `password_checker.py` dosyasındaki her kod bloğunun ne işe yaradığını açıklar.

---

## 📑 İÇİNDEKİLER

1. [Dosya Başlığı ve Import'lar](#1-dosya-başlığı-ve-importlar)
2. [Windows UTF-8 Desteği](#2-windows-utf-8-desteği)
3. [Colors Sınıfı](#3-colors-sınıfı)
4. [Banner Fonksiyonu](#4-banner-fonksiyonu)
5. [Loading Animasyonu](#5-loading-animasyonu)
6. [Entropi Hesaplama](#6-entropi-hesaplama)
7. [Yaygın Şifre Kontrolü](#7-yaygın-şifre-kontrolü)
8. [Ardışık Karakter Kontrolü](#8-ardışık-karakter-kontrolü)
9. [Şifre Analizi](#9-şifre-analizi)
10. [Sonuç Raporlama](#10-sonuç-raporlama)
11. [Yardım ve İpuçları](#11-yardım-ve-ipuçları)
12. [Ana Program](#12-ana-program)

---

## 1. DOSYA BAŞLIĞI VE IMPORT'LAR

```python
#!/usr/bin/env python3
```
**Ne yapar:** Linux/Mac'te dosyayı `./password_checker.py` ile çalıştırmanı sağlar.

---

```python
# -*- coding: utf-8 -*-
```
**Ne yapar:** Python'a "bu dosyada Türkçe karakterler var" der.

---

```python
import re
```
**Ne yapar:** Regular Expression (düzenli ifade) kütüphanesi.  
**Nerede kullanılır:** Şifrede büyük harf, küçük harf, rakam, özel karakter aramak için.  
**Örnek:** `re.search(r'[A-Z]', "Hello")` → Büyük harf bulur.

---

```python
import math
```
**Ne yapar:** Matematik işlemleri kütüphanesi.  
**Nerede kullanılır:** Entropi hesaplamada `log2()` fonksiyonu için.  
**Örnek:** `math.log2(62)` → 5.95 (62'nin 2 tabanında logaritması)

---

```python
import time
```
**Ne yapar:** Zaman işlemleri kütüphanesi.  
**Nerede kullanılır:** Animasyonlarda bekleme yapmak için.  
**Örnek:** `time.sleep(0.3)` → 0.3 saniye bekle.

---

```python
import sys
```
**Ne yapar:** Sistem işlemleri kütüphanesi.  
**Nerede kullanılır:** Terminal çıktısını kontrol etmek, encoding ayarları.  
**Örnek:** `sys.stdout.write()` → Yazı yazmak (print gibi ama satır sonu yok).

---

```python
import os
```
**Ne yapar:** İşletim sistemi işlemleri.  
**Nerede kullanılır:** Ekranı temizlemek için.  
**Örnek:** `os.system('cls')` → Windows'ta ekranı temizler.

---

```python
from collections import Counter
```
**Ne yapar:** Bir listedeki elemanları sayar.  
**Örnek:** `Counter("hello")` → `{'l': 2, 'h': 1, 'e': 1, 'o': 1}`

---

## 2. WINDOWS UTF-8 DESTEĞİ

```python
if sys.platform == 'win32':
```
**Ne yapar:** "İşletim sistemi Windows mu?" diye kontrol eder.

---

```python
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleOutputCP(65001)
```
**Ne yapar:** Windows konsolunu UTF-8 moduna geçirir.  
**Neden gerekli:** Emoji ve özel karakterler (🔐, ✓, █) düzgün görünsün diye.

---

```python
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
```
**Ne yapar:** Python'ın çıktı sistemini UTF-8'e ayarlar.  
**`errors='replace'`:** Gösterilemeyen karakterleri `?` ile değiştirir.

---

## 3. COLORS SINIFI

```python
class Colors:
```
**Ne yapar:** Terminal renklerini bir arada tutar.

---

```python
RED = '\033[91m'
```
**Ne yapar:** Kırmızı renk kodu.  
- `\033` → Terminale "özel komut geliyor" der.
- `[91m` → Kırmızı rengi aktif et.

**Kullanımı:**
```python
print(f"{Colors.RED}Bu kırmızı{Colors.RESET}")
```

---

| Kod | Renk | Kullanım Amacı |
|-----|------|----------------|
| `\033[91m` | 🔴 Kırmızı | Hatalar |
| `\033[92m` | 🟢 Yeşil | Başarı |
| `\033[93m` | 🟡 Sarı | Uyarılar |
| `\033[94m` | 🔵 Mavi | Bilgi |
| `\033[96m` | 🔵 Cyan | Başlıklar |
| `\033[1m` | **Kalın** | Vurgular |
| `\033[0m` | Normal | Rengi sıfırla |

---

## 4. BANNER FONKSİYONU

```python
def print_banner():
```
**Ne yapar:** Programın açılış ekranını (ASCII art logo) yazdırır.

---

```python
banner = f"""
{Colors.CYAN}{'═' * 70}
```
**Ne yapar:** 
- `f"""..."""` → Çok satırlı format string.
- `'═' * 70` → `═` karakterini 70 kez tekrarla.

---

## 5. LOADING ANİMASYONU

```python
def loading_animation(text="Analiz ediliyor"):
```
**Ne yapar:** "Analiz ediliyor..." şeklinde nokta nokta animasyon gösterir.  
**Parametre:** `text` - Gösterilecek yazı (varsayılan: "Analiz ediliyor")

---

```python
for i in range(3):
```
**Ne yapar:** 3 kez döngü yapar (i = 0, 1, 2).

---

```python
sys.stdout.write(f"\r{text}{'.' * (i + 1)}")
```
**Ne yapar:**
- `\r` → İmleci satır başına götür (aynı satırı güncelle).
- `'.' * (i + 1)` → Nokta sayısını artır (., .., ...)

---

```python
sys.stdout.flush()
```
**Ne yapar:** Yazıyı hemen ekrana yazdırır (buffer'ı temizler).

---

## 6. ENTROPİ HESAPLAMA

```python
def calculate_entropy(password):
```
**Ne yapar:** Şifrenin "rastgelelik" seviyesini hesaplar (bit cinsinden).

---

### Entropi Formülü:
```
Entropi = Uzunluk × log₂(Karakter Seti)
```

**Örnek:**
- Şifre: `Abc123` (6 karakter)
- Karakter seti: küçük(26) + büyük(26) + rakam(10) = 62
- Entropi: 6 × log₂(62) = 6 × 5.95 = **35.7 bit**

---

```python
if re.search(r'[a-z]', password):
    charset_size += 26
```
**Ne yapar:** Küçük harf varsa karakter setine 26 ekle.

---

| Regex | Anlamı | Karakter Sayısı |
|-------|--------|-----------------|
| `[a-z]` | Küçük harf | 26 |
| `[A-Z]` | Büyük harf | 26 |
| `[0-9]` | Rakam | 10 |
| `[^a-zA-Z0-9]` | Özel karakter | 32 |

---

## 7. YAYGIN ŞİFRE KONTROLÜ

```python
def check_common_passwords(password):
```
**Ne yapar:** Şifrenin "en kötü şifreler" listesinde olup olmadığını kontrol eder.

---

```python
return password.lower() in common_passwords
```
**Ne yapar:**
1. `password.lower()` → Şifreyi küçük harfe çevir.
2. `in common_passwords` → Listede var mı kontrol et.
3. `True`/`False` döndür.

---

## 8. ARDIŞIK KARAKTER KONTROLÜ

```python
def check_sequential_chars(password):
```
**Ne yapar:** "abc", "123", "qwerty" gibi kolay tahmin edilebilir pattern'ları bulur.

---

```python
sequential_patterns = ['abc', 'bcd', '123', '234', 'qwe', 'asd', ...]
```
**Ne yapar:** Tehlikeli pattern listesi.

---

```python
if pattern in password_lower:
    found_patterns.append(pattern)
```
**Ne yapar:** Şifrede pattern bulursa listeye ekler.

---

## 9. ŞİFRE ANALİZİ

```python
def analyze_password(password):
```
**Ne yapar:** TÜM kontrolleri yapar ve puan verir.

---

### Puanlama Sistemi:

| Kriter | Puan |
|--------|------|
| Uzunluk 16+ | +25 |
| Uzunluk 12-15 | +20 |
| Uzunluk 8-11 | +10 |
| Küçük harf | +10 |
| Büyük harf | +10 |
| Rakam | +10 |
| Özel karakter | +10 |
| Yüksek entropi | +20 |
| **CEZALAR** | |
| Yaygın şifre | -30 |
| Ardışık karakter | -5 (her biri) |

---

```python
score = max(0, min(100, score))
```
**Ne yapar:** Puanı 0-100 arasında sınırlar.
- `min(100, score)` → 100'den büyükse 100 yap.
- `max(0, ...)` → 0'dan küçükse 0 yap.

---

## 10. SONUÇ RAPORLAMA

```python
def print_report(results):
```
**Ne yapar:** Analiz sonuçlarını güzel biçimde ekrana yazdırır.

---

```python
bar_length = 20
filled = int(score / 100 * bar_length)
progress_bar = f"{'█' * filled}{'░' * empty}"
```
**Ne yapar:** Görsel güç çubuğu oluşturur.
- 80 puan → `████████████████░░░░`

---

```python
masked_password = password[0] + '*' * (len-2) + password[-1]
```
**Ne yapar:** Şifreyi gizler.
- `TestPassword` → `T**********d`

---

## 11. YARDIM VE İPUÇLARI

```python
def print_help():
```
**Ne yapar:** Kullanılabilir komutları listeler.

---

```python
def print_tips():
```
**Ne yapar:** Güçlü şifre oluşturma tavsiyelerini gösterir.

---

## 12. ANA PROGRAM

```python
def main():
```
**Ne yapar:** Program başladığında çalışan fonksiyon. Ana döngü burada.

---

```python
while True:
```
**Ne yapar:** Sonsuz döngü. Kullanıcı `exit` yazana kadar devam eder.

---

```python
password = input(f"{Colors.CYAN}🔑 Şifre:{Colors.RESET} ")
```
**Ne yapar:** Kullanıcıdan şifre alır.

---

```python
if command in ['exit', 'quit']:
    break
```
**Ne yapar:** Döngüden çık, programı sonlandır.

---

```python
except KeyboardInterrupt:
```
**Ne yapar:** Ctrl+C basılırsa programı düzgünce kapat.

---

```python
if __name__ == "__main__":
    main()
```
**Ne yapar:** 
- Dosya doğrudan çalıştırılırsa → `main()` çalışır.
- Başka dosyadan import edilirse → Çalışmaz.

---

## 📌 HIZLI REFERANS KARTI

| Sembol | Anlamı |
|--------|--------|
| `def` | Fonksiyon tanımla |
| `class` | Sınıf tanımla |
| `if/elif/else` | Koşul kontrolü |
| `for` | Döngü |
| `while True` | Sonsuz döngü |
| `break` | Döngüden çık |
| `return` | Değer döndür |
| `f"..."` | Format string |
| `r'...'` | Raw string (regex için) |
| `try/except` | Hata yakalama |

---

## 🎯 ÖRNEK KOD AKIŞI

```
1. Program başlar
   ↓
2. print_banner() çalışır → Logo görünür
   ↓
3. while True döngüsü başlar
   ↓
4. input() ile şifre alınır
   ↓
5. Komut mu kontrol edilir (exit, help, tips, clear)
   ↓
6. Şifre ise:
   → loading_animation() → "Analiz ediliyor..."
   → analyze_password() → Tüm kontroller yapılır
   → print_report() → Sonuç gösterilir
   ↓
7. Tekrar şifre istenir (4. adıma dön)
   ↓
8. "exit" yazılırsa → break → Program biter
```

---

*Bu belge h3atwave tarafından hazırlanmıştır. 🔐*
