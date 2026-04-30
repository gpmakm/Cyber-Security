from modules_pentest.port_scanner import scan_ports
from modules_pentest.packet_sniffer import capture_packets
from modules_pentest.PasswordGenerator import PatternGenerator
from scapy.all import get_if_list
print( "Welcome to the pentester")
print("Available practices ")
with open("D://PythonPrograms/Internship-Projects/TaskLists.txt","r") as f:
    content=f.readlines()
    print(content)


def passwordgen():
    passwords=PatternGenerator()
    filename="D://PythonPrograms/Internship-Projects/Passwords.txt"
    passwords.save_to_file(filename)
    with open(filename,"r") as g:
        password=g.readlines()
        print(password)
def runPacketSniffer(interface, count):
    packets = capture_packets(interface, count)

    # Handle errors safely
    if isinstance(packets, dict) and "error" in packets:
        print("Error:", packets["error"])
        return

    for i, pkt in enumerate(packets):
        print(f"Packet {i+1}: {pkt}")
def runPortScanning(host):
    

    result = scan_ports(host, 1, 100)

    if isinstance(result, dict) and "error" in result:
        print(result["error"])
    else:
        for item in result:
            print(f"Port {item['port']} is OPEN ({item['service']})")
command=int(input("Enter the activity to perform : "))
if command==1:
    s=input("Enter target to scan: ")
    runPortScanning(s)
elif command == 2:
    interfaces = get_if_list()

    if not interfaces:
        print("No network interfaces found.")
    else:
        print("\nAvailable Network Interfaces:")
        for i, iface in enumerate(interfaces):
            print(f"{i}: {iface}")

        try:
            choice = int(input("Select interface number: "))
            interface = interfaces[choice]
        except (ValueError, IndexError):
            print("Invalid interface selection.")
            interface = None

        if interface:
            try:
                count = int(input("Enter the number of packets to capture: "))
                runPacketSniffer(interface, count)
            except ValueError:
                print("Invalid packet count.")
elif command==3:
    print("Below is the set of strong passwords try them:")
    passwordgen()
else:
    print("No commands found!!")
