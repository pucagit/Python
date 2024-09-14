import threading
import socket
from queue import Queue

# target = input("Enter the target IP address: ")
target = "192.168.1.1"
ports_to_scan = Queue()
open_ports = []
threads = []

def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP connection
        s.connect((target, port))
        return True
    except:
        return False
    
def worker():
    while not ports_to_scan.empty():
        port = ports_to_scan.get() # get the port from the queue and remove it
        if port_scan(port):
            print(f"Port {port} is open")
            open_ports.append(port)
        ports_to_scan.task_done()
        
if __name__ == "__main__":
    for i in range(1, 1024):
        ports_to_scan.put(i)
    
    for i in range(100):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
        
    print(f"Open ports are: {open_ports}")