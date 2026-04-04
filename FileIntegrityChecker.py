import hashlib
import json
def generateHash(filePath):
    fileHash=hashlib.sha256()
    with open("filename.txt","w") as f:
        f.write(filePath)
    with open(filePath,"rb") as f:
        while chunk:=f.read(4096):
            fileHash.update(chunk)
    return fileHash.hexdigest()


def checkIntegrity(filepath,hashfile):
    currentHash=generateHash(filepath)
    print(currentHash)
    file=""
    with open("filename.txt","r") as f:
        file=f.readline()
    with open(hashfile,"r") as f:
        originalHash=f.read()

        print(originalHash)
    if filePath==file:
        if originalHash=="" or originalHash==" " or len(originalHash)==0:
            print("No hash found, generating...")
            originalHash=generateHash(filePath)
            with open("hash.txt","w") as m:
                m.write(originalHash)
        if currentHash==originalHash:
            print("File integrity verified. No changes detected.")
        
        else:
            print("File integrity compromised. Changes detected.")
    if originalHash=="" or originalHash==" " or len(originalHash)==0:
        originalHash=generateHash(filePath)
        with open("hash.txt","w") as f:
            f.write(originalHash)
            print(f"Hash generated and stored in hash.txt for {filePath}")

filePath=input("Enter your file path: ")
# with open("hash.txt","w") as g:
#     g.write(generateHash(filePath))
checkIntegrity(filePath,"hash.txt")