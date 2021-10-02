import socket
import sys
import threading
import logging


usage = "Usage: python3 apscan.py IP_address START_PORT END_PORT"
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

if end_port > 65535:
    print("Highest TCP port number is 65535 and you have given ",end_port,". Will only scan till 65535")
    end_port = 65535

print("Scanning Target",target)

def scan_port(start_port,end_port):
    for port in range(start_port,end_port):
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

#Starts 5 threads only if the number of ports to be scanned is greater than 5
if end_port - start_port <=5:
    per_thread_count = 5
else:
    per_thread_count = (end_port - start_port) // 5 # Gonna allocate only (end_port-start_port) / 5 number of threads to check for a single thread
threads = []
for port in range(start_port,end_port,per_thread_count):

    thread = threading.Thread(target = scan_port, args = (port,port+per_thread_count))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Done Searching for open ports")