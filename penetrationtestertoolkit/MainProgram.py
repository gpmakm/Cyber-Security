from modules_pentest.port_scanner import scan_ports


print( "Welcome to the pentester")
print("Available practices ")
with open("D://PythonPrograms/Internship-Projects/TaskLists.txt","r") as f:
    content=f.readline()
    print(content)


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


