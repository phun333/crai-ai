import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel, configure
import google.generativeai as genai

# .env dosyasından API anahtarını yükle
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

# Google AI modelini yapılandır
configure(api_key=api_key)
model = GenerativeModel('gemini-pro')

def instagram_post_olustur(sirket_adi, sirket_aciklamasi, sirket_turu, urun_aciklamasi):
    # Prompt oluştur
    prompt = f"""
    Aşağıdaki bilgilere göre profesyonel bir Instagram post açıklaması ve ilgili hashtagler oluştur:
    
    Şirket Adı: {sirket_adi}
    Şirket Türü: {sirket_turu}
    Şirket Açıklaması: {sirket_aciklamasi}
    Ürün Açıklaması: {urun_aciklamasi}
    
    Lütfen aşağıdaki formatta yanıt ver:
    1. Çekici bir post açıklaması (emoji kullanarak)
    2. İlgili hashtagler (en az 10 tane)
    """

    # AI modelinden yanıt al
    response = model.generate_content(prompt)
    return response.text

def main():
    print("Instagram Post ve Hashtag Oluşturucu")
    print("-" * 40)
    
    sirket_adi = input("Şirket adını girin: ")
    sirket_turu = input("Şirket türünü girin (örn: e-ticaret, restoran, teknoloji): ")
    sirket_aciklamasi = input("Şirket hakkında kısa bir açıklama girin: ")
    urun_aciklamasi = input("Atacağınız post hakkında kısa bir açıklama girin: ")
    
    try:
        sonuc = instagram_post_olustur(sirket_adi, sirket_aciklamasi, sirket_turu, urun_aciklamasi)
        print("\nOluşturulan Instagram Postu:")
        print("-" * 40)
        print(sonuc)
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main() 