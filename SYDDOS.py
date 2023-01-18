import socket
import time

def send_packets(host, port, packet_count):
    # Socket oluştur
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    start_time = time.time()
    # Bağlantıyı yap
    s.connect((host, port))
    end_time = time.time()
    connection_time = end_time - start_time
    
    start_time = time.time()
    # Paketleri gönder
    data = b'PAKET'* packet_count
    s.sendall(data)
    end_time = time.time()
    sending_time = end_time - start_time
    
    print("PAKET SENDING: ", packet_count)
    print("Bağlantı süresi: ", connection_time * 1000, "ms")
    print("Gönderme süresi: ", sending_time * 1000, "ms")

    # Bağlantıyı kapat
    s.close()

host = input("Hedef website adresi: ")
port = int(input("Hedef port numarası: "))
packet_count = int(input("Gönderilecek paket sayısı: "))

send_packets(host, port, packet_count)
time.sleep(3)
print("Saldırı başarılı")
time.sleep(99)
