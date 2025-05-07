from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import time

current_time = time.strftime('%Y-%m-%d %H:%M')

# List of IP addresses to connect to
ip_list = [
    "192.168.10.1",
    "192.168.10.2",
    "192.168.10.3",
    "192.168.10.254"
]

# Common device credentials
username = "indika"
password = "indika"
device_type = "cisco_ios"

for ip in ip_list:
    print(f"Connecting to {ip}...")
    device = {
        "device_type": device_type,
        "ip": ip,
        "username": username,
        "password": password,
    }

    try:
        connection = ConnectHandler(**device)
        prompt = connection.find_prompt()
        print(f"👍 Successfully connected to {ip}. Prompt: {prompt}")
        print(f'Connected at : {current_time}')
        connection.disconnect()
    except NetmikoAuthenticationException:
        print(f"👎 Authentication failed for {ip}.")
    except NetmikoTimeoutException:
        print(f"👎 Connection timed out for {ip}.")
    except Exception as e:
        print(f"🤔 An error occurred while connecting to {ip}: {e}")
