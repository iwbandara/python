from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.254',
    'username': 'indika',
    'password': 'indika',
    'port': '22'
}

net_connect = ConnectHandler(**cisco_device)

output = net_connect.send_command('show ip interface brief')

print(output)

file_info = open('router_config.txt','a')

file_info.write(output)
file_info.close()
# print(net_connect.find_prompt())
net_connect.disconnect()

