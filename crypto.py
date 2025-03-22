from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open (KEY_FILE, "wb") as key_file:
            return key_file.write(key)
        

def load_key():
    with open (KEY_FILE, "rb") as key_file:
        return key_file.read()
    

def encrypt_password(password: str) -> bytes:
    key = load_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password: bytes) -> str:
    key=load_key()
    cipher = Fernet(key)
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password




