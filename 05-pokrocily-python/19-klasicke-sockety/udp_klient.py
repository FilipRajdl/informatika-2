"""
UDP KLIENT
Demonstrace "nespojované" komunikace.
Klient se "nepřipojuje". Prostě vezme data, napíše na ně adresu serveru a hodí je do sítě.
"""

import socket

HOST = '127.0.0.1'
PORT = 65432

def main():
    # Vytvoříme UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print("UDP Klient připraven.")
        print(f"Posílám data na {HOST}:{PORT} (bez záruky doručení).")
        
        while True:
            text = input("Zadej zprávu (nebo 'q'): ")
            if text.lower() == 'q':
                break
            
            # Odeslání: sendto(data, adresa_cíle)
            # Nepoužíváme connect(), ale rovnou posíláme.
            s.sendto(text.encode('utf-8'), (HOST, PORT))
            
            # Čekání na odpověď (volitelné)
            # U UDP není garantováno, že odpověď přijde!
            # V reálné aplikaci by zde měl být timeout (s.settimeout(2.0))
            try:
                s.settimeout(2.0) # Čekáme max 2 sekundy
                data, server = s.recvfrom(1024)
                print(f"Odpověď od {server}: {data.decode('utf-8')}")
            except socket.timeout:
                print("Server neodpověděl včas (paket se ztratil?).")

if __name__ == "__main__":
    main()