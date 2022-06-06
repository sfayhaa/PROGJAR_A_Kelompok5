import argparse, random, socket, zen_utils
import sys, random, multiprocessing

HOST = "127.0.0.1"
PORT = 1060
NUMJOBS = 6

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data

def worker(address, i, data):
    # membuat socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address) # connect socket

    message = ""
    for ii in data: # untuk setiap 'ii' dalam data
        ii = ii.strip() # di strip dulu karena di paling kanan masih ada newline 
        len_msg = b"%03d" % (len(ii),) 
        msg = len_msg + bytes(ii, encoding="ascii")
        sock.sendall(msg)
        len_msg = recvall(sock, 3)
        message = recvall(sock, int(len_msg))
        message = str(message, encoding="ascii")
    print(message)
    sock.close()

if __name__ == '__main__':
     # membaca input.txt. dan disimpan menjadi list dalam data
    f = open("input.txt")
    data = f.readlines()
    f.close()

    address = (HOST, PORT)
    jobs = [] #list job


    for i in range(NUMJOBS):
        p = multiprocessing.Process(target=worker, args=(address, i, data))
        
        jobs.append(p) # hasil p di append ke dalam list jobs
    print("JOBS:", len(jobs))

    for p in jobs:
        p.start()

# dilakukan join. thread utama akan menunggu sampai semua join.
    for p in jobs:
        p.join()

# vim:sw=4:ai
