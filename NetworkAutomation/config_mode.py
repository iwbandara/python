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

# Moves in to the Enable mode
connect.enable()

# Moves into the Global configuration mode
connect.config_mode()

# Send the command to Config mode to execute with 'do' command at the front
output = connect.send_command('do show version | include Version')

print(output)

print(connect.find_prompt())

connect.disconnect()