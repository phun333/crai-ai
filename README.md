# Instagram Post Oluşturucu

> **Not**: Bu proje, bir hackathon etkinliği kapsamında geliştirilen bir web sitesi için oluşturulmuş bir prototiptir.

Bu Python uygulaması, şirketlerin Instagram için post açıklamaları ve hashtagler oluşturmasına yardımcı olmak için Google'ın Gemini AI modelini kullanır.

## Özellikler

- Şirket bilgilerine göre özelleştirilmiş Instagram post açıklamaları oluşturur
- İlgili hashtagler önerir
- Kullanıcı dostu komut satırı arayüzü
- Google Gemini AI modelini kullanır

## Kurulum

1. Repoyu klonlayın:
```bash
git clone <repo-url>
cd instagram-post-olusturucu
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. `.env` dosyasını oluşturun ve Google API anahtarınızı ekleyin:
```
GOOGLE_API_KEY=sizin_api_anahtariniz
```

## Kullanım

Uygulamayı çalıştırmak için:

```bash
python instagram_post_generator.py
```

Uygulama size aşağıdaki bilgileri soracaktır:
- Şirket adı
- Şirket türü
- Şirket açıklaması
- Post hakkında açıklama

Bu bilgileri girdikten sonra, uygulama AI tarafından oluşturulan bir Instagram post açıklaması ve ilgili hashtagleri gösterecektir.

## Gereksinimler

- Python 3.7+
- python-dotenv
- google-generativeai

## Not

Bu uygulama için geçerli bir Google API anahtarına ihtiyacınız vardır. [Google AI Studio](https://makersuite.google.com/app/apikey) üzerinden bir API anahtarı alabilirsiniz. 