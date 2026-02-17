import requests
import sys
from datetime import datetime, timedelta
import io

# GitHub sunucularında Türkçe karakterlerin düzgün görünmesi için
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Webhook URL'niz
WEBHOOK_URL = "https://discord.com/api/webhooks/1467994929035743484/T5dXAwBljLxJIzVubjAjl9h3oNjpXtlcu6VR_u7yi75grkWryqP_Pg4yIda6_MZRYRLm"

# Ders Programı Verisi
DERS_PROGRAMI = {
    "Monday": [
        "🖥️ 08:20 - 11:30 | Sunucu İşletim Sistemleri (4 Saat)",
        "📚 11:40 - 13:10 | Türk Dili ve Edebiyatı (2 Saat)",
        "🕌 13:55 - 15:25 | Din Kültürü ve Ahlak Bilgisi (2 Saat)"
    ],
    "Tuesday": [
        "⚽ 08:20 - 09:50 | Beden Eğitimi (2 Saat)",
        "🧠 10:00 - 11:30 | Felsefe (2 Saat)",
        "📚 11:40 - 13:10 | Türk Dili ve Edebiyatı (2 Saat)",
        "➕ 13:55 - 15:25 | Seçmeli Temel Matematik (2 Saat)",
        "📜 15:35 - 17:00 | Tarih (2 Saat)"
    ],
    "Wednesday": [
        "🌐 08:20 - 15:25 | Ağ Sistemleri ve Yönlendirme (8 Saat)"
    ],
    "Thursday": [
        "🏥 08:20 - 09:00 | Sağlık Bilgisi (1 Saat)",
        "🧪 09:10 - 10:40 | Seçmeli Kimya (2 Saat)",
        "💻 10:50 - 13:10 | Seçmeli Programlama (3 Saat)",
        "📚 13:55 - 14:35 | Türk Dili ve Edebiyatı (1 Saat)",
        "💭 14:45 - 16:15 | Seçmeli Türk Düşünce Tarihi (2 Saat)"
    ],
    "Friday": [
        "🧭 08:20 - 09:00 | Rehberlik ve Yönlendirme (1 Saat)",
        "🛡️ 09:10 - 13:10 | Siber Güvenlik Temelleri (5 Saat)",
        "🧪 13:55 - 15:25 | Seçmeli Kimya (2 Saat)",
        "🤝 15:35 - 16:15 | Seçmeli Ahilik Kültürü ve Girişimcilik (1 Saat)"
    ]
}

# Gün İsimleri Eşleştirmesi
GUN_ISIMLERI = {
    "Monday": "PAZARTESİ",
    "Tuesday": "SALI",
    "Wednesday": "ÇARŞAMBA",
    "Thursday": "PERŞEMBE",
    "Friday": "CUMA",
    "Saturday": "CUMARTESİ",
    "Sunday": "PAZAR"
}

def discord_mesaj_gonder(icerik):
    """Discord Webhook'una içeriği gönderir."""
    payload = {"content": icerik}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if 200 <= response.status_code < 300:
            print("✅ Discord mesajı başarıyla gönderildi.")
        else:
            print(f"❌ Hata kodu: {response.status_code}")
    except Exception as e:
        print(f"⚠️ İletişim hatası: {e}")

def ders_programini_gonder():
    # ÖNEMLİ: GitHub UTC saatini kullanır (İstanbul'dan 3 saat geridedir).
    # İstanbul saatini (UTC+3) yakalamak için üzerine 3 saat ekliyoruz.
    turkiye_saati = datetime.utcnow() + timedelta(hours=3)
    
    gun_ingilizce = turkiye_saati.strftime("%A")
    tr_gun_ismi = GUN_ISIMLERI.get(gun_ingilizce, gun_ingilizce.upper())
    
    # Hafta sonu kontrolü
    if gun_ingilizce in ["Saturday", "Sunday"]:
        print(f"Bugün {tr_gun_ismi}, hafta sonu olduğu için mesaj gönderilmedi.")
        return

    # Mesaj başlığı
    mesaj_icerigi = f"📅 **{tr_gun_ismi} GÜNLÜK DERS PROGRAMI**\n\n"
    
    # Günlük dersleri al
    dersler = DERS_PROGRAMI.get(gun_ingilizce, [])
    
    if dersler:
        mesaj_icerigi += "\n\n".join(dersler)
    else:
        mesaj_icerigi += "Bugün için ders programı verisi bulunamadı."

    print(f"Gönderiliyor: {tr_gun_ismi}")
    discord_mesaj_gonder(mesaj_icerigi)

if __name__ == "__main__":
    ders_programini_gonder()
