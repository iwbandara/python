from netmiko import ConnectHandler
from getpass import getpass

cisco_devices = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.1',
    'username': 'indika',
    'password': getpass('Password: '),
    'port': '22',
    'secret': getpass('Password: ')
}

connect = ConnectHandler(**cisco_devices)

connect.enable()

output = connect.send_command('show version | include Version')

print(output)

print(connect.find_prompt())

connect.disconnect()