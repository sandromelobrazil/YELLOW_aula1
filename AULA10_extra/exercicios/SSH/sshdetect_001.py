#!/usr/bin/python

from netmiko import Netmiko
from netmiko import SSHDetect

target = '11.11.11.171'
user = 'msfadmin'
pwd = 'msfadmin'
device = 'linux'

device = { "device_type": "autodetect", "host": target, "username": user, "password": pwd }

sshtarget = SSHDetect(**device)
best_match = sshtarget.autodetect()
print('Isso eh provavelmente:', best_match)
print('Pontecial de:', str(sshtarget.potential_matches))


