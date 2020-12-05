#!/usr/bin/python

from netmiko import Netmiko

target = '11.11.11.171'
user = 'msfadmin'
pwd = 'xmsfadmin'
device = 'linux'

sshmiko = Netmiko(
        target,
        username = user,
        password = pwd,
        device_type = device)

print(sshmiko.find_prompt())
sshmiko.disconnect()





