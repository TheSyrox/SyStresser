import argparse
import asyncio
import aiohttp
import threading
import requests
import time

# Argümanları işleme
parser = argparse.ArgumentParser(description='HTTP isteği gönderen program')
parser.add_argument('--url', required=True, help='İstek gönderilecek URL')
parser.add_argument('--port', type=int, required=True, help='Bağlanılacak port')
parser.add_argument('--time', type=int, required=True, help='İsteklerin süresi (saniye)')
parser.add_argument('--threads', type=int, default=1, help='Eşzamanlı istek gönderilecek thread sayısı')
parser.add_argument('--connections', type=int, default=1, help='Eşzamanlı istek gönderilecek bağlantı sayısı')
args = parser.parse_args()

# İstek gönderen işlev (asyncio)
async def send_request_async(url, port, duration):
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        while time.time() - start_time < duration:
            async with session.get(f'http://{url}:{port}') as response:
                if response.status == 200:
                    print(f'Başarılı async istek gönderildi: {url}:{port}')

# İstek gönderen işlev (thread)
def send_request_thread(url, port, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        try:
            response = requests.get(f'http://{url}:{port}')
            if response.status_code == 200:
                print(f'Başarılı thread istek gönderildi: {url}:{port}')
        except Exception as e:
            print(f'Hata oluştu: {e}')

# Thread'leri oluştur ve başlat (thread)
threads = []
for _ in range(args.threads):
    t = threading.Thread(target=send_request_thread, args=(args.url, args.port, args.time))
    threads.append(t)
    t.start()

# asyncio ile istekleri asenkron olarak gönder (asyncio)
async def main_async():
    tasks = []
    for _ in range(args.connections):
        task = send_request_async(args.url, args.port, args.time)
        tasks.append(task)
    
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main_async())

# Thread'lerin tamamlanmasını bekle (thread)
for t in threads:
    t.join()

print('İstekler tamamlandı.')
