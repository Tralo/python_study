#!/usr/bin/env python
# coding=utf-8

import sys
import thread
from socket import 

def tcp_test(port):i
    sock = socket(AF_INET,SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip,port))
    if result == 0:
        lock.acquire()
        print "Opened Port: ",port
        lock.release()


if __name__ == '__main__':
    host = sys.argv[1]
    portstrs = sys.argv[2].spilt('-')
    
    start_port = portstrs[0]
    end_port = portstrs[1]

    target_ip = gethostbyname(host)
    lock = thread.allocate_lock()
    
    for port in range(start_port,end_port):
        thread.start_new_thread(tcp_test,(port,))



