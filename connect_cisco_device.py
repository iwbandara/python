from netmiko import ConnectHandler
from getpass import getpass

# Netmiko module uses SSH to connect to remote devices

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.254',
    'username': input('username: '),    # Prompt for username
    'password': getpass('Password: '),  # Prompt for password
    'port': '22',
    'secret': 'ccna'                    # Assign 'ccna' as the enable mode password
}

net_connect = ConnectHandler(**cisco_device)

# Sends a command to the device to execute at User mode
# output = net_connect.send_command('show ip interface brief | exclude unassigned')

# Moves the prompt to Enable mode
net_connect.enable()

# Execute command at Enable mode & assign the output to a variable
output = net_connect.send_command('show access-lists')

# output = net_connect.send_command('show ip route')
# 
# config_list = [
#     'access-list 1 permit any any'
# ]

# cfg_output = net_connect.send_config_set(config_list)

# print(cfg_output)
print(output)

# print(net_connect.check_enable_mode())

# file_info = open('router_config.txt','a')

# file_info.write(output)
# file_info.close()

print(net_connect.find_prompt())
net_connect.disconnect()

