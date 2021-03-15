#!/usr/bin/python3

# Ref: TryHackMe [Scripting] room, Task 2
#  https://tryhackme.com/room/scripting

import sys
import socket
import time
import requests
import datetime
from bs4 import BeautifulSoup

def initialize(host, port):
    res = requests.get("http://{0}:{1}".format(host, port))
    soup = BeautifulSoup(res.text, 'html.parser')
    next_port = soup.find(id="onPort").string
    print("[+] Next Port: {0}".format(next_port))
    return 1337
# This task starts from 1337/tcp.
#    return next_port

def calc(host, next_port, start_num):
    num = float(start_num)
    while next_port != 9765:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(next_port)))
            request = "GET / HTTP/1.0\r\n\r\n"
            s.send(request.encode())
            response = s.recv(8192)
            print("[+] Connected: http://{0}:{1}".format(host, next_port))
#            print(response.decode())
            response = response.decode().split("\r\n\r\n")[1].split(" ")

            operator = response[0]
            new_number = float(response[1])
            next_port = response[2]

            print("[+] Operator:" + operator + " NUM:" + str(new_number) + " NEXT_PORT:" + next_port)

            if operator == "add":
                num += new_number
            elif operator == "minus":
                num -= new_number
            elif operator == "multiply":
                num *= new_number
            elif operator == "divide":
                num /= new_number
            elif operator == "STOP":
                print("[*] Done. NUM:{:.12}".format(num))
                sys.exit()
            else:
                print("[*] Done. NUM:{:.12}".format(num))
                sys.exit()

            print("[+] Calc Result:{:.12}".format(num))
            s.close()
            time.sleep(3.5)
        except ConnectionRefusedError:
            print("[-] " + str(datetime.datetime.now()) + " Retry...")
            time.sleep(0.2)
        except TimeoutError:
            print("[-] " + str(datetime.datetime.now()) + " Retry...")
            time.sleep(0.2)
        except IndexError:
            print("[*] IndexErrorr: " + str(response))
            if (response[0] == "STOP"):
                sys.exit()


if __name__ == '__main__':
    print("[*] Web Response Calc")
    print("    Calcurate HTTP Response: (add|minus|multiply|divide|STOP) <number> <next_port>")
    if len(sys.argv) != 3:
        print("[-] usage: python3 -u " + sys.argv[0] + " <HOST> <PORT>")
    else:
        print("[+] Connecting")
        host = sys.argv[1]
        port = sys.argv[2] # default: 3010
        start_num = 0.0
        next_port = initialize(host, port)
        calc(host, next_port, start_num)
