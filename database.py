import csv
import os
from crypto import encrypt_password, decrypt_password

PASSWORD_FILE = "password.csv"

def init_db():
    if not os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Website", "Username", "Encrypet password"])

def add_password(website: str, usernname: str, password: str ):

    encrypted_password = encrypt_password(password)
    
    with open(PASSWORD_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website, usernname, encrypted_password])

def get_password(website: str):
    
    password = decrypt_password(password)

    with open(PASSWORD_FILE, mode='r') as file:
        
        reader = reader.csv(file)

        for row in reader:
            if row[0] == website:
                decrypted_password = decrypt_password(row[2].encode())
                return decrypted_password
            
def list_passwords():
    
    with open(PASSWORD_FILE, mode='r') as file:
        
        reader = csv.reader(file)

        for row in reader:
            print(f"Website: {row[0]}, Username: {row[1]}, Password: {decrypt_password(row[2].encode())}")
            
            





