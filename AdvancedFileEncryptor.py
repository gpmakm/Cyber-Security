filePath=input("Enter the file path to encrypt file: ")
with open(filePath,"r") as f:
    content=f.readline()
    print(content)
    for m in content:
        if m=='a':
            print("a found")

