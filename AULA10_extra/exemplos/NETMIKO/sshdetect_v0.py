from netmiko import Netmiko
from netmiko import SSHDetect


device = { "device_type": "autodetect", "host": "10.171.1.129", "username": "msfadmin", "password": "msfadmin" }

msg_01="[*] - Please wait, analyzing of the target running"
msg_02="[+] - This SSH server is probably a "


print(msg_01)
sshtarget = SSHDetect(**device)
best_match = sshtarget.autodetect()
print(msg_02 + best_match)  

#device["device_type"] = best_match
