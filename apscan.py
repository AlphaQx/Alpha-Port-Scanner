import socket
import sys
import threading
import logging


usage = "python3 apscan.py IP_address START_PORT END_PORT"
print("-"*80)
print("Welcome to Port Scanner by AlphaQx")
print("-"*80)

if(len(sys.argv) != 4) :
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Error 404: Name Resolution")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning Target",target)

def scan_port(port):
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target, port))
    if(not conn):
        print("port {} is OPEN" . format(port))
        s.close()
        #Added open port information in log file with timestamp
        print("Logging in open port details in same directory...")
        logging.basicConfig(level=logging.INFO, format='%(message)s port open at %(asctime)s' ,filename='openports.log',filemode='a',datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("{}".format(port))

for port in range(start_port, end_port+1):

    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()
