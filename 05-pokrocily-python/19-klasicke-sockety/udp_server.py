"""
UDP SERVER (Datagramy)
Tento server neudržuje žádná trvalá spojení.
Pouze "sedí" na portu a čeká, až mu někdo pošle balíček dat.
"""

import socket

HOST = '127.0.0.1'
PORT = 65432

def start_udp_server():
    print(f"--- START UDP SERVERU ({HOST}:{PORT}) ---")
    
    # SOCK_DGRAM = UDP protokol
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print("Server připraven. Čekám na datagramy...")
        
        while True:
            # recvfrom je blokující, ale vrací data rovnou (není tu accept)
            # vrací n-tici: (data, (ip, port))
            data, addr = s.recvfrom(1024)
            
            zprava = data.decode('utf-8')
            print(f"[Příjem] Od {addr}: {zprava}")
            
            # Pokud chceme odpovědět, musíme explicitně říct KAM (addr)
            # Protože neexistuje trvalé spojení, musíme adresu pokaždé uvést.
            odpoved = f"UDP Server potvrzuje: {zprava}"
            s.sendto(odpoved.encode('utf-8'), addr)

if __name__ == "__main__":
    start_udp_server()