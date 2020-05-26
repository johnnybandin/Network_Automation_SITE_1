from netmiko import ConnectHandler
import getpass
import re
password = getpass.getpass()
username = input('Enter username here: ')

VIRLR1 = {
    "device_type": "cisco_ios",
    "ip": '192.168.122.80',
    'username': username,
    'password': password
    }


net_connect = ConnectHandler(**VIRLR1)
output = net_connect.send_command('show version')
regexoutput = re.search('15.......................', output)
print(regexoutput)

with open('version.txt', 'w') as f:
    f.write(str(regexoutput))
