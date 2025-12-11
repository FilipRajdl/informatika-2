"""
KLASICKÝ MULTI-THREADED SERVER
Tento server zvládne více klientů najednou díky vláknům.
Je to přímý ekvivalent C++ serveru z předchozích lekcí.
"""

import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def obsluz_klienta(conn, addr):
    """
    Funkce, která běží ve vlastním vlákně pro každého klienta.
    """
    print(f"[Vlákno {threading.get_ident()}] Připojen klient: {addr}")
    
    try:
        with conn:
            while True:
                # recv blokuje vlákno, dokud nepřijdou data
                data = conn.recv(1024)
                if not data:
                    break
                
                zprava = data.decode('utf-8')
                print(f"[{addr}] Přijato: {zprava}")
                
                # Echo odpověď
                odpoved = f"Server přijal: {zprava}"
                conn.sendall(odpoved.encode('utf-8'))
    except ConnectionResetError:
        print(f"[{addr}] Spojení násilně ukončeno.")
            
    print(f"[Vlákno] Klient {addr} odpojen.")

def start_server():
    print(f"--- START SERVERU ({HOST}:{PORT}) ---")
    # AF_INET = IPv4, SOCK_STREAM = TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Povolíme reuse adresy (aby šel server hned restartovat)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        
        while True:
            print("Čekám na spojení...")
            # accept blokuje hlavní vlákno
            conn, addr = s.accept()
            
            # Pro každého klienta nastartujeme nové vlákno
            t = threading.Thread(target=obsluz_klienta, args=(conn, addr))
            t.start()
            
            # Vypíšeme počet aktivních vláken (minus hlavní vlákno)
            print(f"[Info] Počet klientů: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()