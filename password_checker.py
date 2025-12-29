#!/usr/bin/env python3
#Linux/Mac üzerinde python3 ile çalıştırılmasını sağlıyor.

# -*- coding: utf-8 -*-
#kodlarda türkçe karakter olabileceğini belirtiyor.

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        🔐 PASSWORD STRENGTH CHECKER 🔐                       ║
║                                                                              ║
║  Bu program girilen şifrelerin güvenlik seviyesini analiz eder.             ║
║                                                                              ║
║  Özellikler:                                                                 ║
║  • Entropi (karmaşıklık) hesaplama                                          ║
║  • Yaygın şifre kontrolü                                                     ║
║  • Karakter çeşitliliği analizi                                              ║
║  • Detaylı güvenlik raporu                                                   ║
║  • Şifre güçlendirme önerileri                                              ║
║                                                                              ║
║  Geliştirici: h3atwave                                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import re       # Regular Expression (Düzenli ifadeler) - karakter pattern kontrolü için
import math     # Matematiksel işlemler - entropi hesaplama için
import time     # Zaman işlemleri - animasyonlar için
import sys      # Sistem işlemleri - terminal kontrolü için
import os       # İşletim sistemi işlemleri için

from collections import Counter  # Karakter sayımı için

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                       WINDOWS UTF-8 DESTEĞI                                  ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# Windows'ta UTF-8 karakter desteğini etkinleştir
# Bu sayede emoji ve özel karakterler düzgün görüntülenir
if sys.platform == 'win32':
    try:
        # Windows konsolu için UTF-8 modunu etkinleştir
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleOutputCP(65001)  # UTF-8 code page
        kernel32.SetConsoleCP(65001)
        
        # stdout encoding'i UTF-8 yap
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stdin.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass  # Hata olursa sessizce devam et

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                            ANSI RENK KODLARI SINIFI                          ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

class Colors:
    """
    Terminal ekranında renkli yazı yazmak için ANSI escape kodları.
    
    Kullanım:
        print(f"{Colors.RED}Bu kırmızı yazı{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}Bu kalın yeşil yazı{Colors.RESET}")
    """
    
    RED = '\033[91m'        # Kırmızı - hata mesajları için
    GREEN = '\033[92m'      # Yeşil - başarılı sonuçlar için
    YELLOW = '\033[93m'     # Sarı - uyarılar için
    BLUE = '\033[94m'       # Mavi - bilgi mesajları için
    MAGENTA = '\033[95m'    # Mor - özel vurgular için
    CYAN = '\033[96m'       # Cyan - başlıklar ve çerçeveler için
    WHITE = '\033[97m'      # Beyaz - normal metin için
    BOLD = '\033[1m'        # Kalın - önemli başlıklar için
    DIM = '\033[2m'         # Soluk - ikincil bilgiler için
    RESET = '\033[0m'       # Sıfırla - rengi normale döndür

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                              BANNER FONKSİYONU                               ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def print_banner():
    """
    Program başlatıldığında gösterilen ASCII art banner.
    h3atwave imzalı profesyonel görünüm sağlar.
    """
    
    banner = f"""
{Colors.CYAN}{'═' * 70}
{Colors.RED}
    ██╗  ██╗██████╗  █████╗ ████████╗██╗    ██╗ █████╗ ██╗   ██╗███████╗
    ██║  ██║╚════██╗██╔══██╗╚══██╔══╝██║    ██║██╔══██╗██║   ██║██╔════╝
    ███████║ █████╔╝███████║   ██║   ██║ █╗ ██║███████║██║   ██║█████╗  
    ██╔══██║ ╚═══██╗██╔══██║   ██║   ██║███╗██║██╔══██║╚██╗ ██╔╝██╔══╝  
    ██║  ██║██████╔╝██║  ██║   ██║   ╚███╔███╔╝██║  ██║ ╚████╔╝ ███████╗
    ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝
{Colors.CYAN}
                    🔐 PASSWORD STRENGTH CHECKER 🔐
{Colors.YELLOW}                          Gururla Sunar
{Colors.CYAN}{'═' * 70}{Colors.RESET}
"""
    
    print(banner)

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                            LOADİNG ANİMASYONU                                ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def loading_animation(text="Analiz ediliyor"):
    """
    Profesyonel loading animasyonu - nokta nokta efekti.
    
    Parametreler:
        text (str): Gösterilecek metin (varsayılan: "Analiz ediliyor")
    
    Örnek:
        loading_animation("Hesaplanıyor")  # "Hesaplanıyor..." gösterir
    """
    
    for i in range(3):
        # 3 kez döngü: ".", "..", "..."
        sys.stdout.write(f"\r{Colors.YELLOW}{text}{'.' * (i + 1)}   {Colors.RESET}")
        sys.stdout.flush()  # Buffer'ı temizle, anında göster
        time.sleep(0.3)     # 0.3 saniye bekle
    
    print()  # Yeni satıra geç

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                            ENTROPİ HESAPLAMA                                 ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def calculate_entropy(password):
    """
    Şifre entropisini hesaplar (bit cinsinden).
    
    Entropi = Şifrenin ne kadar karmaşık/rastgele olduğunu ölçer.
    Yüksek entropi = Daha güçlü şifre
    
    Formül: Entropi = Şifre_Uzunluğu × log2(Karakter_Seti_Büyüklüğü)
    
    Parametreler:
        password (str): Analiz edilecek şifre
    
    Döndürür:
        float: Entropi değeri (bit cinsinden)
    
    Entropi Seviyeleri:
        < 28 bit  : Çok zayıf
        28-35 bit : Zayıf
        36-59 bit : Orta
        60-127 bit: Güçlü
        128+ bit  : Çok güçlü
    """
    
    charset_size = 0  # Toplam karakter seti büyüklüğü
    
    # Küçük harf kontrolü (a-z = 26 karakter)
    if re.search(r'[a-z]', password):
        charset_size += 26
    
    # Büyük harf kontrolü (A-Z = 26 karakter)
    if re.search(r'[A-Z]', password):
        charset_size += 26
    
    # Rakam kontrolü (0-9 = 10 karakter)
    if re.search(r'[0-9]', password):
        charset_size += 10
    
    # Özel karakter kontrolü (!@#$%^&*... = ~32 karakter)
    if re.search(r'[^a-zA-Z0-9]', password):
        charset_size += 32
    
    # Boş şifre veya tanınmayan karakterler
    if charset_size == 0:
        return 0
    
    # Entropi hesaplama
    entropy = len(password) * math.log2(charset_size)
    
    return round(entropy, 2)  # 2 ondalık basamağa yuvarla

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                          YAYGIN ŞİFRE KONTROLÜ                               ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def check_common_passwords(password):
    """
    Şifrenin yaygın kullanılan şifreler listesinde olup olmadığını kontrol eder.
    
    Bu şifreler dünyadaki en çok kullanılan ve en kolay kırılan şifrelerdir.
    Veri ihlallerinden elde edilen bilgilere dayanır.
    
    Parametreler:
        password (str): Kontrol edilecek şifre
    
    Döndürür:
        bool: True = yaygın şifre (tehlikeli!), False = yaygın değil
    """
    
    common_passwords = [
        # En çok kullanılan şifreler (kesinlikle kullanmayın!)
        'password', '123456', '12345678', 'qwerty', 'abc123',
        'monkey', '1234567', 'letmein', 'trustno1', 'dragon',
        'baseball', 'iloveyou', 'master', 'sunshine', 'ashley',
        'bailey', 'password1', '123456789', 'password123',
        'admin', 'welcome', 'login', '1234', '12345',
        'qwerty123', 'admin123', 'root', 'toor', 'pass',
        '123123', 'password1234', '1q2w3e4r', 'qwertyuiop',
        '111111', '123321', 'superman', 'batman', 'shadow',
        'michael', 'jennifer', 'football', 'jordan', 'princess'
    ]
    
    return password.lower() in common_passwords

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                          ARDIŞIK KARAKTER KONTROLÜ                           ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def check_sequential_chars(password):
    """
    Şifrede ardışık karakterler (abc, 123, qwe) olup olmadığını kontrol eder.
    
    Ardışık karakterler şifreyi zayıflatır çünkü tahmin edilmesi kolaydır.
    
    Parametreler:
        password (str): Kontrol edilecek şifre
    
    Döndürür:
        list: Bulunan ardışık pattern'ların listesi
    """
    
    # Yaygın ardışık pattern'lar
    sequential_patterns = [
        # Alfabe sıralaması
        'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 
        'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr',
        'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz',
        
        # Sayı sıralaması
        '012', '123', '234', '345', '456', '567', '678', '789',
        
        # Klavye sıralaması (QWERTY)
        'qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
        'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl',
        'zxc', 'xcv', 'cvb', 'vbn', 'bnm',
        
        # Tekrarlayan karakterler
        'aaa', 'bbb', 'ccc', '111', '222', '333', '000'
    ]
    
    found_patterns = []
    password_lower = password.lower()
    
    for pattern in sequential_patterns:
        if pattern in password_lower:
            found_patterns.append(pattern)
    
    return found_patterns

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                          ŞİFRE GÜÇ ANALİZİ                                   ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def analyze_password(password):
    """
    Şifreyi her açıdan analiz eder ve detaylı sonuç döndürür.
    
    Analiz Kriterleri:
        1. Uzunluk (minimum 8, ideal 12+)
        2. Küçük harf varlığı
        3. Büyük harf varlığı
        4. Rakam varlığı
        5. Özel karakter varlığı
        6. Yaygın şifre kontrolü
        7. Ardışık karakter kontrolü
        8. Entropi hesaplaması
    
    Parametreler:
        password (str): Analiz edilecek şifre
    
    Döndürür:
        dict: Analiz sonuçlarını içeren sözlük
    """
    
    results = {
        'password': password,
        'length': len(password),
        'has_lowercase': bool(re.search(r'[a-z]', password)),
        'has_uppercase': bool(re.search(r'[A-Z]', password)),
        'has_digit': bool(re.search(r'[0-9]', password)),
        'has_special': bool(re.search(r'[^a-zA-Z0-9]', password)),
        'is_common': check_common_passwords(password),
        'sequential_chars': check_sequential_chars(password),
        'entropy': calculate_entropy(password),
        'score': 0,
        'strength': '',
        'suggestions': []
    }
    
    # ═══════════════════════════════════════════════════════════════════════
    # PUANLAMA SİSTEMİ (0-100 arası)
    # ═══════════════════════════════════════════════════════════════════════
    
    score = 0
    suggestions = []
    
    # 1. UZUNLUK PUANLAMASI (maksimum 25 puan)
    # ─────────────────────────────────────────
    if results['length'] >= 16:
        score += 25  # Mükemmel uzunluk
    elif results['length'] >= 12:
        score += 20  # İyi uzunluk
    elif results['length'] >= 8:
        score += 10  # Minimum kabul edilebilir
    elif results['length'] >= 6:
        score += 5   # Çok kısa
        suggestions.append("⚠️  Şifrenizi en az 8 karakter yapın")
    else:
        score += 0   # Tehlikeli derecede kısa
        suggestions.append("🚨 Şifreniz çok kısa! En az 8 karakter olmalı")
    
    # 2. KARAKTER ÇEŞİTLİLİĞİ (maksimum 40 puan)
    # ──────────────────────────────────────────
    
    # Küçük harf (10 puan)
    if results['has_lowercase']:
        score += 10
    else:
        suggestions.append("💡 Küçük harf ekleyin (a-z)")
    
    # Büyük harf (10 puan)
    if results['has_uppercase']:
        score += 10
    else:
        suggestions.append("💡 Büyük harf ekleyin (A-Z)")
    
    # Rakam (10 puan)
    if results['has_digit']:
        score += 10
    else:
        suggestions.append("💡 Rakam ekleyin (0-9)")
    
    # Özel karakter (10 puan)
    if results['has_special']:
        score += 10
    else:
        suggestions.append("💡 Özel karakter ekleyin (!@#$%^&*)")
    
    # 3. ENTROPİ BONUSU (maksimum 20 puan)
    # ────────────────────────────────────
    entropy = results['entropy']
    if entropy >= 80:
        score += 20  # Çok yüksek entropi
    elif entropy >= 60:
        score += 15  # Yüksek entropi
    elif entropy >= 40:
        score += 10  # Orta entropi
    elif entropy >= 28:
        score += 5   # Düşük entropi
    else:
        score += 0   # Çok düşük entropi
    
    # 4. CEZALAR (negatif puanlar)
    # ────────────────────────────
    
    # Yaygın şifre cezası (-30 puan)
    if results['is_common']:
        score -= 30
        suggestions.insert(0, "🚨 Bu şifre çok yaygın! Hemen değiştirin!")
    
    # Ardışık karakter cezası (her biri için -5 puan)
    if results['sequential_chars']:
        penalty = len(results['sequential_chars']) * 5
        score -= min(penalty, 15)  # Maksimum 15 puan ceza
        suggestions.append(f"⚠️  Ardışık karakterlerden kaçının: {', '.join(results['sequential_chars'])}")
    
    # 5. SKOR SINIRLANDIRMA
    # ─────────────────────
    score = max(0, min(100, score))  # 0-100 arasında tut
    
    # 6. GÜÇ SEVİYESİ BELİRLEME
    # ─────────────────────────
    if score >= 80:
        strength = 'ÇOK GÜÇLÜ'
        strength_color = Colors.GREEN
    elif score >= 60:
        strength = 'GÜÇLÜ'
        strength_color = Colors.GREEN
    elif score >= 40:
        strength = 'ORTA'
        strength_color = Colors.YELLOW
    elif score >= 20:
        strength = 'ZAYIF'
        strength_color = Colors.RED
    else:
        strength = 'ÇOK ZAYIF'
        strength_color = Colors.RED
    
    # Sonuçları güncelle
    results['score'] = score
    results['strength'] = strength
    results['strength_color'] = strength_color
    results['suggestions'] = suggestions
    
    return results

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                            SONUÇ RAPORLAMA                                   ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def print_report(results):
    """
    Şifre analiz sonuçlarını güzel formatlanmış şekilde ekrana yazdırır.
    
    Parametreler:
        results (dict): analyze_password() fonksiyonundan dönen sonuçlar
    """
    
    # Renkler için kısayollar
    C = Colors
    
    # Güç çubuğu oluştur (görsel gösterim)
    score = results['score']
    bar_length = 20
    filled = int(score / 100 * bar_length)
    empty = bar_length - filled
    
    # Çubuk rengi
    if score >= 60:
        bar_color = C.GREEN
    elif score >= 40:
        bar_color = C.YELLOW
    else:
        bar_color = C.RED
    
    progress_bar = f"{bar_color}{'█' * filled}{C.DIM}{'░' * empty}{C.RESET}"
    
    # ═══════════════════════════════════════════════════════════════════════
    # RAPOR YAZDIRMA
    # ═══════════════════════════════════════════════════════════════════════
    
    print(f"\n{C.CYAN}{'═' * 60}{C.RESET}")
    print(f"{C.BOLD}{C.WHITE}            📊 ŞİFRE ANALİZ RAPORU 📊{C.RESET}")
    print(f"{C.CYAN}{'═' * 60}{C.RESET}\n")
    
    # Şifre bilgisi (gizlenmiş)
    masked_password = results['password'][0] + '*' * (len(results['password']) - 2) + results['password'][-1] if len(results['password']) > 2 else '*' * len(results['password'])
    print(f"  {C.WHITE}Şifre:{C.RESET}        {C.DIM}{masked_password}{C.RESET}")
    print(f"  {C.WHITE}Uzunluk:{C.RESET}      {results['length']} karakter")
    
    # Güç göstergesi
    strength_color = results.get('strength_color', C.WHITE)
    print(f"\n  {C.WHITE}Güç:{C.RESET}          {strength_color}{C.BOLD}{results['strength']}{C.RESET}")
    print(f"  {C.WHITE}Skor:{C.RESET}         [{progress_bar}] {score}/100")
    print(f"  {C.WHITE}Entropi:{C.RESET}      {results['entropy']} bit")
    
    # Karakter analizi
    print(f"\n  {C.CYAN}{'─' * 40}{C.RESET}")
    print(f"  {C.BOLD}{C.WHITE}📝 KARAKTER ANALİZİ{C.RESET}")
    print(f"  {C.CYAN}{'─' * 40}{C.RESET}")
    
    # Kontrol işaretleri
    check_mark = f"{C.GREEN}✓{C.RESET}"
    cross_mark = f"{C.RED}✗{C.RESET}"
    
    checks = [
        ('Küçük harf (a-z)', results['has_lowercase']),
        ('Büyük harf (A-Z)', results['has_uppercase']),
        ('Rakam (0-9)', results['has_digit']),
        ('Özel karakter (!@#$)', results['has_special']),
    ]
    
    for label, has_it in checks:
        mark = check_mark if has_it else cross_mark
        print(f"    {mark} {label}")
    
    # Uyarılar
    if results['is_common']:
        print(f"\n    {C.RED}⚠️  UYARI: Bu şifre yaygın şifreler listesinde!{C.RESET}")
    
    if results['sequential_chars']:
        print(f"    {C.YELLOW}⚠️  Ardışık pattern bulundu: {', '.join(results['sequential_chars'])}{C.RESET}")
    
    # Öneriler
    if results['suggestions']:
        print(f"\n  {C.CYAN}{'─' * 40}{C.RESET}")
        print(f"  {C.BOLD}{C.WHITE}💡 ÖNERİLER{C.RESET}")
        print(f"  {C.CYAN}{'─' * 40}{C.RESET}")
        
        for suggestion in results['suggestions']:
            print(f"    {suggestion}")
    
    print(f"\n{C.CYAN}{'═' * 60}{C.RESET}\n")

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                              YARDIM MENÜSÜ                                   ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def print_help():
    """Kullanım kılavuzunu ekrana yazdırır."""
    
    C = Colors
    
    help_text = f"""
{C.CYAN}{'═' * 60}{C.RESET}
{C.BOLD}{C.WHITE}                    📖 YARDIM MENÜSÜ 📖{C.RESET}
{C.CYAN}{'═' * 60}{C.RESET}

{C.YELLOW}KULLANIM:{C.RESET}
    Şifrenizi girin ve Enter'a basın.

{C.YELLOW}KOMUTLAR:{C.RESET}
    {C.GREEN}help{C.RESET}    - Bu yardım menüsünü gösterir
    {C.GREEN}clear{C.RESET}   - Ekranı temizler
    {C.GREEN}tips{C.RESET}    - Güçlü şifre ipuçları gösterir
    {C.GREEN}exit{C.RESET}    - Programdan çıkar
    {C.GREEN}quit{C.RESET}    - Programdan çıkar

{C.YELLOW}PUANLAMA SİSTEMİ:{C.RESET}
    0-19   : {C.RED}Çok Zayıf{C.RESET} - Hemen değiştirin!
    20-39  : {C.RED}Zayıf{C.RESET} - Güçlendirme gerekli
    40-59  : {C.YELLOW}Orta{C.RESET} - Kabul edilebilir
    60-79  : {C.GREEN}Güçlü{C.RESET} - İyi seviye
    80-100 : {C.GREEN}Çok Güçlü{C.RESET} - Mükemmel!

{C.CYAN}{'═' * 60}{C.RESET}
"""
    print(help_text)

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                            ŞİFRE İPUÇLARI                                    ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def print_tips():
    """Güçlü şifre oluşturma ipuçlarını gösterir."""
    
    C = Colors
    
    tips_text = f"""
{C.CYAN}{'═' * 60}{C.RESET}
{C.BOLD}{C.WHITE}              🔐 GÜÇLÜ ŞİFRE OLUŞTURMA İPUÇLARI 🔐{C.RESET}
{C.CYAN}{'═' * 60}{C.RESET}

{C.GREEN}✓ YAPIN:{C.RESET}
    • En az 12 karakter kullanın (ideal: 16+)
    • Büyük ve küçük harfleri karıştırın
    • Rakam ve özel karakterler ekleyin
    • Her hesap için farklı şifre kullanın
    • Şifre yöneticisi kullanın
    • Parola yerine "passphrase" kullanın
      Örnek: "MaviKedi$Kosuyor#2024!"

{C.RED}✗ YAPMAYIN:{C.RESET}
    • Kişisel bilgiler kullanmayın (doğum tarihi, isim)
    • Sözlük kelimeleri kullanmayın
    • Ardışık karakterler kullanmayın (abc, 123)
    • Aynı şifreyi birden fazla yerde kullanmayın
    • Şifrenizi başkalarıyla paylaşmayın
    • Şifrenizi not defterine yazmayın

{C.YELLOW}💡 İPUCU:{C.RESET}
    Güçlü bir şifre oluşturmak için bir cümle düşünün:
    "Kedim 3 yaşında ve çok tatlı!" → "K3yv&çt!"
    
    Veya rastgele kelimeler birleştirin:
    "Masa+Lamba+Deniz+42" → "MasaLambaDeniz42!"

{C.CYAN}{'═' * 60}{C.RESET}
"""
    print(tips_text)

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                              ANA PROGRAM                                     ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def main():
    """
    Ana program döngüsü.
    
    Kullanıcıdan sürekli şifre alır ve analiz eder.
    'exit' veya 'quit' yazana kadar devam eder.
    """
    
    C = Colors
    
    # Banner göster
    print_banner()
    
    print(f"{C.WHITE}Şifre güvenliğinizi test etmek için şifrenizi girin.{C.RESET}")
    print(f"{C.DIM}(Yardım için 'help' yazın, çıkmak için 'exit' yazın){C.RESET}\n")
    
    while True:
        try:
            # Kullanıcıdan şifre al
            password = input(f"{C.CYAN}🔑 Şifre:{C.RESET} ")
            
            # Boş giriş kontrolü
            if not password.strip():
                print(f"{C.YELLOW}⚠️  Lütfen bir şifre girin.{C.RESET}\n")
                continue
            
            # Komut kontrolü
            command = password.strip().lower()
            
            if command in ['exit', 'quit', 'q', 'çık', 'çıkış']:
                print(f"\n{C.GREEN}✨ Güvenli günler dileriz! Görüşmek üzere...{C.RESET}\n")
                break
            
            elif command in ['help', 'yardım', 'h', '?']:
                print_help()
                continue
            
            elif command in ['clear', 'cls', 'temizle']:
                # Ekranı temizle (Windows ve Unix uyumlu)
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
                print_banner()
                print(f"{C.DIM}(Yardım için 'help' yazın, çıkmak için 'exit' yazın){C.RESET}\n")
                continue
            
            elif command in ['tips', 'ipucu', 'ipuçları', 'öneri']:
                print_tips()
                continue
            
            # Şifre analizi
            loading_animation("Şifre analiz ediliyor")
            results = analyze_password(password)
            print_report(results)
            
        except KeyboardInterrupt:
            # Ctrl+C ile çıkış
            print(f"\n\n{C.YELLOW}⚠️  Program sonlandırıldı.{C.RESET}\n")
            break
        
        except Exception as e:
            # Beklenmeyen hata
            print(f"\n{C.RED}❌ Bir hata oluştu: {e}{C.RESET}\n")

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                              PROGRAM GİRİŞ NOKTASI                           ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

if __name__ == "__main__":
    """
    Bu blok sadece dosya doğrudan çalıştırıldığında çalışır.
    Başka bir dosyadan import edildiğinde çalışmaz.
    
    Kullanım:
        python password_checker.py
    """
    main()