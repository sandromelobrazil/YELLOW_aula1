from netmiko import Netmiko
from netmiko import SSHDetect
#from getpass import getpass

device = { "device_type": "autodetect", "host": "10.171.1.129", "username": "msfadmin", "password": "msfadmin" }


guesser = SSHDetect(**device)
best_match = guesser.autodetect()
print(best_match)  # Name of the best device_type to use further
print(guesser.potential_matches)  # Dictionary of the whole matching result

device["device_type"] = best_match
connection = Netmiko(**device)

print(connection.find_prompt())
