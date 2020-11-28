# -*- coding: utf-8 -*-
import socket

ip_address=10.171.1.129
port=21

def banner_grab(ip_address, port):
    port_1 = int(port)
    addr = (ip_address, port_1)
    s = socket.socket()
    s.connect(addr)
    return s.recv(1024)


def main(ip_address, port):
    ip=ip_address
    p=port
    print ('Banner Grabbing FTP for IP Address : %s' % ip_address)
    output = banner_grab(ip, p)
    # Save output into file under respective IP addresses under FTP directory
    f = open('./%s/FTP/%s_%s_banner.txt'% (ip_address, ip_address, port), 'w') 
    f.write(output)
    f.close()

main(10.171.1.129,21)

