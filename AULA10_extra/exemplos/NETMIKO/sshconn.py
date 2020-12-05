
#!/usr/bin/python3.7

from netmiko import Netmiko

sshconn = Netmiko(
    "10.171.1.129", 
    username="msfadmin", 
    password="msfadmin", 
    device_type="linux")

print(sshconn.find_prompt())
sshconn.disconnect()


