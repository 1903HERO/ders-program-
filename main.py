import requests
import sys
from datetime import datetime
import io

# Türkçe karakter desteği
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

WEBHOOK_URL = "https://discord.com/api/webhooks/1467994929035743484/T5dXAwBljLxJIzVubjAjl9h3oNjpXtlcu6VR_u7yi75grkWryqP_Pg4yIda6_MZRYRLm"

DERS_PROGRAMI = {
    "Monday": ["🖥️ 08:20 - 11:30 | Sunucu İşletim Sistemleri (4 Saat)", "📚 11:40 - 13:10 | Türk Dili ve Edebiyatı (2 Saat)", "🕌 13:55 - 15:25 | Din Kültürü (2 Saat)"],
    "Tuesday": ["⚽ 08:20 - 09:50 | Beden Eğitimi (2 Saat)", "🧠 10:00 - 11:30 | Felsefe (2 Saat)", "📚 11:40 - 13:10 | Türk Dili ve Edebiyatı (2 Saat)", "➕ 13:55 - 15:25 | Temel Matematik (2 Saat)", "📜 15:35 - 17:00 | Tarih (2 Saat)"],
    "Wednesday": ["🌐 08:20 - 15:25 | Ağ Sistemleri ve Yönlendirme (8 Saat)"],
    "Thursday": ["🏥 08:20 - 09:00 | Sağlık Bilgisi (1 Saat)", "🧪 09:10 - 10:40 | Seçmeli Kimya (2 Saat)", "💻 10:50 - 13:10 | Seçmeli Programlama (3 Saat)", "📚 13:55 - 14:35 | Türk Dili ve Edebiyatı (1 Saat)", "💭 14:45 - 16:15 | Türk Düşünce Tarihi (2 Saat)"],
    "Friday": ["🧭 08:20 - 09:00 | Rehberlik (1 Saat)", "🛡️ 09:10 - 13:10 | Siber Güvenlik Temelleri (5 Saat)", "🧪 13:55 - 15:25 | Seçmeli Kimya (2 Saat)", "🤝 15:35 - 16:15 | Ahilik Kültürü (1 Saat)"]
}

GUN_ISIMLERI = {"Monday": "PAZARTESİ", "Tuesday": "SALI", "Wednesday": "ÇARŞAMBA", "Thursday": "PERŞEMBE", "Friday": "CUMA", "Saturday": "CUMARTESİ", "Sunday": "PAZAR"}

def discord_mesaj_gonder(icerik):
    payload = {"content": icerik}
    requests.post(WEBHOOK_URL, json=payload)

def ders_programini_gonder():
    bugun = datetime.now()
    gun_ingilizce = bugun.strftime("%A")
    tr_gun_ismi = GUN_ISIMLERI.get(gun_ingilizce, gun_ingilizce.upper())
    
    if gun_ingilizce in ["Saturday", "Sunday"]:
        print("Hafta sonu, mesaj gönderilmedi.")
        return

    mesaj_icerigi = f"📅 **{tr_gun_ismi} GÜNLÜK DERS PROGRAMI**\n\n"
    dersler = DERS_PROGRAMI.get(gun_ingilizce, [])
    
    if dersler:
        mesaj_icerigi += "\n\n".join(dersler)
        discord_mesaj_gonder(mesaj_icerigi)
        print(f"{tr_gun_ismi} programı gönderildi.")

if __name__ == "__main__":
    ders_programini_gonder()
