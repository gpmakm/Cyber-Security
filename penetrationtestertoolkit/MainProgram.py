from modules_pentest.port_scanner import scan_ports
from modules_pentest.packet_sniffer import capture_packets
from modules_pentest.PasswordGenerator import PatternGenerator

print( "Welcome to the pentester")
print("Available practices ")
with open("D://PythonPrograms/Internship-Projects/TaskLists.txt","r") as f:
    content=f.readline()
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

    for i, pkt in enumerate(packets):
        print(f"Packet {i+1}: {pkt.summary()}")

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
elif command==2:
    interface = input("Enter the network interface to capture packets (e.g., 'eth0', 'wlan0'): ")
    count = int(input("Enter the number of packets to capture: "))
    runPacketSniffer(interface, count)
elif command==3:
    print("Below is the set of strong passwords try them:")
    passwordgen()
else:
    print("No commands found!!")
