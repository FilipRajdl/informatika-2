"""
JEDNODUCHÝ KLIENT
Připojí se, pošle zprávu, počká na odpověď.
"""

import socket

HOST = '127.0.0.1'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            print(f"Připojuji se k {HOST}:{PORT}...")
            s.connect((HOST, PORT))
            print("Připojeno! Pište zprávy (nebo 'q' pro konec).")
            
            while True:
                text = input("> ")
                if text.lower() == 'q':
                    break
                    
                s.sendall(text.encode('utf-8'))
                
                # Čekáme na odpověď (blokující)
                data = s.recv(1024)
                print(f"Server: {data.decode('utf-8')}")
                
        except ConnectionRefusedError:
            print("CHYBA: Server neběží nebo spojení odmítnuto.")

if __name__ == "__main__":
    main()