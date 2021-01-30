class config:
    BOT_TOKEN = ""
    APP_ID = ""
    API_HASH = ""
    DATABASE_URL = ""
    SUDO_USERS = "" # Sepearted by space.
    SUPPORT_CHAT_LINK = ""
    DOWNLOAD_DIRECTORY = "./downloads/"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**Merhaba {}.**\n__Ben quidefilite Drive Botu.Beni Google Drive'a Dosya Yüklemek (Youtube & Direkt Link &T elegram Dosyaları) İçin Kullanabilirsin.__\n__/help Komutu İle Kuruluma Geçebilirsin.__"

    HELP_MSG = [
        ".",
        "**quidefilite Drive Uploader**\n__Beni Google Drive'a Dosya Yüklemek (Youtube&Direkt Link&Telegram Dosyaları) İçin Kullanabilirsin. Tek ihtiyacım olan, Google Drive Hesabınızda kimliğimi doğrulamak ve doğrudan bir indirme bağlantısı veya Telegram Dosyası göndermeniz.__\n\nÇok Daha Fazla Özelliğe Sahibim ...! DEvamı İçin Sadece bu öğreticiye göz at ve mesajları dikkatlice oku.",
        
        f"**Google Drive'ınızı Bota Bağlamak**\n__ /{BotCommands.Authorize[0]} komutuna basın ve bir URL alacaksınız, URL'yi ziyaret edecek ve adımları izleyip alınan kodu buraya göndereceksiniz. /{BotCommands.Revoke[0]} Komutuysa Bağlı Olan Hesabınızı Bottan Kaldırır.__\n\n**Not: Siz /{BotCommands.Authorize[0]}  Komutu İle Bağlantı Sağlayana Kadar Diğer Komutlar Çalışmayacaktır.\nBotun, Düzgün Çalışabilmesi İçin Doğrulama Gereklidir !**",
        
        f"**Direkt Bağlantılar**\n__Bota bir dosya için doğrudan indirme bağlantısı gönderin, botda sunucuya indirip Google Drive Hesabınıza yükleyesin. Dosya İsimlerini Yükleme Yapmadan Önce Değiştirebilirsiniz. İsimlendirme için önceki linki daha sonra ayırmak için ' | ' yi ve daha sonrasında dosya adını yazın (sonuna dosya türünü eklemeyi unutmayın).__\n\n**__örneğin:__**\n```https://örnek.com/doğrudannidirmelinki.mkv | Yeni Dosya İsmi.mkv```\n\n**Telegram Dosyaları**\n__Telegramdaki dosyaları Google Drive Hesabınıza yüklemek için bota dosyayı gönderin, bot da Google Drive Hesabınıza yüklesin. Not: Telegram Dosyalarının İndirilmesi yavaştır (Telegramdan Dolayı). Büyük dosyalar için daha uzun sürebilir.__\n\n**YouTube Desteği**\n__Youtube Videolarınızı Drive'ınıza Kaydedin.\n /{BotCommands.YtDl[0]} (YouTube Linki)__ komutu ile kullanabilirsiniz.",
        
        f"**Hedef Klasörü Ayarlamak**\n__Yüklemeleri Kendi Belirlediğiniz Klasöre Yada__ **TeamDrive'a** __ mı Yüklemek İstiyorsunuz ?\n /{BotCommands.SetFolder[0]} (Klasör Linki) Komutu İle Yükleme Hedefini Ayarlayabilirsiniz.\nDeğişiklik Yapılana Kadar Tüm Dosyalar Belirlediğiniz Klasöre Yüklenir.__",
        
        f"**Google Drive'dan Dosya Silmek**\n__Drive'dan Dosya Silmek İçin /{BotCommands.Delete[0]} (Dosya/Klasör Linki) Komutunu Kullanabilirsiniz.\n /{BotCommands.EmptyTrash[0]} Komutu İle Drive'daki Çöp Kutusunu Boşaltabilirsiniz.\nNot: Dosyalar Anında Silinir. Bu İşlem Geri Alınamaz.\n\n**Google Drive'a Dosya Kopyalamak**\n__Başka Bir Google Drive Dosyasını Kendi Drive'ınıza Kopyalayın.\n__ /{BotCommands.Clone[0]} (Dosya/Klasör Linki) Komutu İle Kendi Drive'ınıza Kopyalayabilirsiniz.__",
        
        "**Kurallar & Uyarılar**\n__1. Büyük Dosyaları/Klasörleri Kopyalamaya Çalışmayın.Bu işlem Bota (Sadece Sizin İçin Geçerli) Zarar Verebilir..\n2.Her Seferinde Tek Bir Dosyayı İşleme Sokun Ve Yeni Bir İşlem İçin Eskisinin Bitmesini Bekliyin .\n3.Botu Çok Fazla Zorlamayın Ve +18 İçerikler İçin Kullanmayın.\n4. Bu Kurallara Uymayan Herkes Bot'dan Banlanacaktır.__",
        
        # Dont remove this ↓ if you respect developer.
        "**Geliştirici @quiong**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Hız Limiti Aşıldı.**\n__İndirme Limiti Aşıldı 24 Saat Sonra Tekrar Deneyin(Google Drive Kaynaklı Sorun).__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **Dosya/Klasör Bulunamadı.**\n__File id - {} Bulunamadı. Bunun Erişilebilir\Bir Hesap Olduğundan Emin Olun.__"
    
    INVALID_GDRIVE_URL = "❗ **Geçersiz Google Drive Linki**\nLinkin Düzgün Bir Formatta Olduğundan Emin Olun."
    
    COPIED_SUCCESSFULLY = "✅ **Başarıyla Kopyalandı.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **Bağlanmış Bir Google Hesabınız Bulunmamaktadır.**\n__Send /{BotCommands.Authorize[0]} Bağlamak İçin.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Dosya Yükleniyor...**\n**Dosya Adı:** ```{}```\n**Dosya Boyutu:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Yükleme başarı ile tamamlandı.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**İndirme Başarısız**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Dosya Yüklenmek Üzere Sunucuya İndiriliyor...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Zaten Bağlanmış Bir Google Hesabınız Bulunmaktadır.**\n__Şuan ki Hesabınızı Kaldırmak İçin /revoke komutunu kullanın.__\n__Bana Google Drive'a Yüklemem İçin Bir Dosya Yada Direkt Link Gönderin__"
    
    FLOW_IS_NONE = f"❗ **Geçersiz Komut**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Google Hesabınız Başarıyla Doğrulandı Ve Bağlandı.**'
    
    INVALID_AUTH_CODE = '❗ **Geçersiz Kod**\n__Gönderdiğiniz Kod Geçersiz Veya Daha Önceden Kullanılmış. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "⛓️ **Google Hesabınızı Bağlamak İçin Bu Bağlantıya Gidin [URL]({}) Ve Size Verilen Kodu Bota Gönderin.**\n__Alttaki Butondan Linke Gidin > Hesabınızı Seçin Ve İzin Verin > Kodunuz Dönüştürülecek > Kopyalayın > Buraya Gönderin__"
    
    DOWNLOAD_TG_FILE = "📥 **Dosya İndiriliyor...**\n**Dosya Adı:** ```{}```\n**Boyut:** ```{}```\n**Tür:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Klasör Bağlantınız Ayarlandı.**\n__Klasör id - {}\nKlasör Seçenekleri Sıfırlamak İçin__ ```/{} clear``` __Komutunu Kullanın.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Mevcut Klasör Bağlantısı Başarı İle Sıfırlandı.**\n__Ayarlamak için__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __Komutunu Kullan__.'
    
    CURRENT_PARENT = "🆔 **Şuan Ki Mevcut Klasör ID - {}**\n__Değiştirmek için__ ```/{} (Folder link)``` __Komutunu Kullanın.__"
    
    REVOKED = f"🔓 **Bağlı Olan Hesap Başarı İle Kaldırıldı.**\n__Tekrardan Hesap Bağlamak İçin /{BotCommands.Authorize[0]} Komutunu Kullanın.__"
    
    NOT_FOLDER_LINK = "❗ **Geçersiz Klasör Linki.**\n__Yolladığınız Link Bir Klasöre Ait Olmalıdır.__"
    
    CLONING = "🗂️ **Google Drive'a Kopyalanıyor...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Komutla birlikte geçerli bir Google Drive URL'si Girin.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **Bu dosya için yeterli izniniz yok.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **Dosya Başarıyla Silindi.**\n__Dosya kalıcı olarak silindi !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **HATA : Birşeyler Yanlış Gitti**\n__Daha Sonra Tekrar Dene.__"
    
    EMPTY_TRASH = "🗑️🚮**Çöp Kutusu Başarıyla Boşaltıldı !**"
    
    PROVIDE_YTDL_LINK = "❗**YouTube-DL 'in Desteklediği Bir Link Girdiğinize Emin Olun.**"
