# Using Netmiko library for managing network devices via SSH
# You must have installed Netmiko (pip install netmiko) and have SSH access to the network devices you want to manage
# Replace the device parameters (host, username, password, etc.) with the appropriate values for your network devices

from netmiko import ConnectHandler

# Define device parameters
device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "password",
}

device2 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.2",
    "username": "admin",
    "password": "password",
}


# Example 1: Connecting to a device and retrieving its prompt
def get_device_prompt(device):
    with ConnectHandler(**device) as conn:
        return conn.find_prompt()


print("Example 1: Retrieving device prompts")
print("Device 1 prompt:", get_device_prompt(device1))
print("Device 2 prompt:", get_device_prompt(device2))
print()


# Example 2: Retrieving device hostname
def get_device_hostname(device):
    with ConnectHandler(**device) as conn:
        output = conn.send_command("show run | i hostname")
        return output.split()[1]


print("Example 2: Retrieving device hostname")
print("Device 1 hostname:", get_device_hostname(device1))
print("Device 2 hostname:", get_device_hostname(device2))
print()


# Example 3: Retrieving device interface status
def get_interface_status(device, interface):
    with ConnectHandler(**device) as conn:
        output = conn.send_command(f"show interface {interface} status")
        return output


print("Example 3: Retrieving device interface status")
print("Device 1 interface status:")
print(get_interface_status(device1, "GigabitEthernet0/1"))
print("Device 2 interface status:")
print(get_interface_status(device2, "GigabitEthernet0/1"))
print()


# Example 4: Configuring an interface description
def configure_interface_description(device, interface, description):
    with ConnectHandler(**device) as conn:
        config_commands = [
            f"interface {interface}", f"description {description}"]
        output = conn.send_config_set(config_commands)
        return output


print("Example 4: Configuring interface description")
print("Configuring description for Device 1 interface:")
print(configure_interface_description(
    device1, "GigabitEthernet0/1", "Connected to switch1"))
print("Configuring description for Device 2 interface:")
print(configure_interface_description(
    device2, "GigabitEthernet0/1", "Connected to switch2"))
print()


# Example 5: Saving configuration changes
def save_configuration(device):
    with ConnectHandler(**device) as conn:
        output = conn.save_config()
        return output


print("Example 5: Saving configuration changes")
print("Saving configuration for Device 1:")
print(save_configuration(device1))
print("Saving configuration for Device 2:")
print(save_configuration(device2))
print()
