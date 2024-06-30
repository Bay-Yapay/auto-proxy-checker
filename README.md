# auto-proxy-checker
automatically checks for proxies and writes to files

# Proxy Checker

Bu Python betiği, çeşitli proxy türlerini kontrol ederek çalışanları belirlemek için kullanılır. HTTP/s, SOCKS4 ve SOCKS5 proxy türleri desteklenir ve Proxyscrape API kullanılarak proxy listeleri alınır.

## Kurulum

1. Python'un yüklü olduğundan emin olun.
2. Gerekli kütüphaneleri yüklemek için terminalde veya komut isteminde şu komutu çalıştırın:
 pip install requirements.txt

4. Betiği çalıştırmak için `proxy_checker.py` dosyasını çalıştırın.

## Kullanım

1. Program çalıştırıldığında, HTTP/s, SOCKS4 ve SOCKS5 proxy türlerinden kaç adet kontrol edileceğini sorar. şuanda işlevsizdir 
2. Her proxy türü için belirtilen sayıda proxy kontrol edilir ve çalışan proxyler belirtilir.
3. Sonuçlar `http_proxies.txt`, `socks4_proxies.txt` ve `socks5_proxies.txt` dosyalarına yazılır.

## Özellikler

- Çoklu thread kullanarak hızlı proxy kontrolü
- Renkli çıktılarla kullanıcı dostu arayüz
- Başlık güncellemesi ile işlem durumu takibi

## Katkıda Bulunma

1. Bu repo'yu klonlayın (`git clone https://github.com/kullanıcı_adı/proxy-checker.git`)
2. Yeni özellikler ekleyin veya hataları düzeltin
3. Değişikliklerinizi (`git commit -am 'Yeni özellik: ...'`) ileterek bir dal oluşturun (`git checkout -b özellik/düzeltme`)
4. Değişikliklerinizi yükleyin (`git push origin özellik/düzeltme`)
5. Bir pull isteği açın

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
