import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

# Constants
SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32  # 256-bit AES
ITERATIONS = 100000


def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a secure key from password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


def encrypt_file(input_file: str, output_file: str, password: str):
    """Encrypt a file using AES-256-GCM."""
    # Read file
    with open(input_file, "rb") as f:
        data = f.read()

    # Generate random salt & nonce
    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)

    # Derive key
    key = derive_key(password, salt)

    # Encrypt
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, data, None)

    # Save: [salt][nonce][ciphertext]
    with open(output_file, "wb") as f:
        f.write(salt + nonce + ciphertext)

    print(f"File encrypted successfully → {output_file}")


def decrypt_file(input_file: str, output_file: str, password: str):
    """Decrypt a file encrypted with AES-256-GCM."""
    with open(input_file, "rb") as f:
        data = f.read()

    # Extract components
    salt = data[:SALT_SIZE]
    nonce = data[SALT_SIZE:SALT_SIZE + NONCE_SIZE]
    ciphertext = data[SALT_SIZE + NONCE_SIZE:]

    # Derive key
    key = derive_key(password, salt)

    # Decrypt
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    # Save file
    with open(output_file, "wb") as f:
        f.write(plaintext)

    print(f"File decrypted successfully → {output_file}")


print("Welcome to the Advanced File Encryptor")
print("1. File Encryption \n 2. File Decryption")
choice = input("Enter your choice (1 or 2): ")
file = input("Enter the file path to encrypt/decrypt: ")
if choice == "1":
    password = input("Enter a strong password for encryption: ")
    output_file = input("Enter the output file path for encrypted file: ")
    encrypt_file(file, output_file, password)
else:
    password = input("Enter the password used for encryption: ")
    output_file = input("Enter the output file path for decrypted file: ")
    decrypt_file(file, output_file, password)