import argparse
import threading
import requests
import time

# Argümanları işleme
parser = argparse.ArgumentParser(description='HTTP isteği gönderen program')
parser.add_argument('--url', required=True, help='İstek gönderilecek URL')
parser.add_argument('--port', type=int, required=True, help='Bağlanılacak port')
parser.add_argument('--time', type=int, required=True, help='İsteklerin süresi (saniye)')
parser.add_argument('--threads', type=int, default=1, help='Eşzamanlı istek gönderilecek thread sayısı')
args = parser.parse_args()

# İstek gönderen işlev
def send_request(url, port, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        try:
            response = requests.get(f'http://{url}:{port}')
            if response.status_code == 200:
                print(f'Başarılı istek gönderildi: {url}:{port}')
        except Exception as e:
            print(f'Hata oluştu: {e}')

# Thread'leri oluştur ve başlat
threads = []
for _ in range(args.threads):
    t = threading.Thread(target=send_request, args=(args.url, args.port, args.time))
    threads.append(t)
    t.start()

# Thread'lerin tamamlanmasını bekle
for t in threads:
    t.join()

print('İstekler tamamlandı.')
