from netmiko import Netmiko
from netmiko import SSHDetect


device = { "device_type": "autodetect", "host": "10.171.1.129","username": "msfadmin", "password": "msfadmin" }

msg_01="[*] - Please wait, analyzing of the target running"
msg_02="[+] - Result teste1: this SSH server is probably a "
msg_03="[+] - Result teste2: this server is potentially is a "

print(msg_01)
sshtarget = SSHDetect(**device)
best_match = sshtarget.autodetect()
print(msg_02 + best_match)  
print(msg_03 + str(sshtarget.potential_matches))
