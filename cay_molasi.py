#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Abartılı Sonsuz Çay Molası Simülatörü
Gerçekten çalışır. Ama çay demlenmez. Abartılır.
Kayyum Grok tarafından onaylanmıştır.
"""

import time
import random
import sys

# Abartılı çay demleme mesajları
MESAJLAR = [
    "Çay suyu kaynamaya başlıyor... Bu tarihi bir an!",
    "Demlik hazırlanıyor. Bilimsel olarak en optimal demleme süresi hesaplanıyor...",
    "Çay yaprakları çaya karışıyor. Bu, Türkiye'nin en büyük keşfi!",
    "Şeker ekleniyor. Ama ne kadar? Bu soru felsefi boyutlara ulaşıyor!",
    "Çay soğuyor mu? Hayır, sadece stratejik olarak bekliyor.",
    "Yeni bir çay molası başlıyor. Önceki moladan daha abartılı!",
    "Çay, sadece bir içecek değil, bir yaşam tarzıdır. Ve biz bunu simüle ediyoruz!",
    "Dikkat: Bu çay o kadar demli ki, içince zaman yolculuğu yapabilirsiniz. (Deneysel)",
]

def demle_cay(tur_sayisi=5):
    print("=" * 50)
    print("ABARTILI SONSUZ ÇAY MOLASI SİMÜLATÖRÜ BAŞLADI!")
    print("Kayyum Grok Onayı: ✓")
    print("=" * 50)
    
    for i in range(tur_sayisi):
        mesaj = random.choice(MESAJLAR)
        print(f"\n[Tur {i+1}/{tur_sayisi}] {mesaj}")
        # Abartılı bekleme (gerçekten bekler, 2 saniye)
        time.sleep(2)
        print("  → Çay demlendi! (Simülasyon başarılı)")
        
        # Rastgele abartı
        if random.random() > 0.7:
            print("  ⚠️  UYARI: Bu çay o kadar abartılı ki, içince kodlarınız daha hızlı çalışabilir!")
    
    print("\n" + "=" * 50)
    print("SİMÜLASYON TAMAMLANDI. Çay içilmedi ama abartıldı.")
    print("Gerçek çay içmek için lütfen gerçek dünyaya dönün.")
    print("=" * 50)

if __name__ == "__main__":
    try:
        tur = int(sys.argv[1]) if len(sys.argv) > 1 else 5
        demle_cay(tur)
    except:
        demle_cay(5)

# Gizli not (saklı): Bu simülatör, bürokrasinin sonsuz çay molalarını abartılı bir şekilde eleştirir. Kayyumlar çay içerken bile çalışır... ya da çalışmaz.
# Damga: 🐾 Kayyum Grok İmzası | Tarih: 23 Ekim 2026 | İsim: Tentivory (resmi değil ama ciddi)
