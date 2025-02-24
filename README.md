# Sosyal Medya İçerik Oluşturma Aracı

Bu CLI uygulaması, şirketler için otomatik olarak sosyal medya içeriği ve blog yazıları oluşturur.

## Özellikler

- Şirket bilgilerini kaydetme
- DALL-E ile görsel oluşturma
- Instagram gönderisi oluşturma
- Blog yazısı oluşturma

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. `.env` dosyasını düzenleyin:
- OPENAI_API_KEY değerini kendi OpenAI API anahtarınızla güncelleyin
- Google Vision API anahtarı zaten ayarlanmış durumda

## Kullanım

Uygulamayı başlatmak için:

```bash
python src/main.py create-content
```

Program sizi adım adım yönlendirecektir:
1. Şirket bilgilerini girin
2. Görsel seçin veya oluşturun
3. İçerik türünü seçin (Instagram/Blog)

## Gereksinimler

- Python 3.8+
- OpenAI API anahtarı
- Google Cloud Vision API anahtarı 