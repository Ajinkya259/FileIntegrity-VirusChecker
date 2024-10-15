
from cryptography.fernet import Fernet
import base64
import os

class FileEncryptor:
    def __init__(self, password):
        self.key = self.generate_key(password)

    def generate_key(self, password):
        return base64.urlsafe_b64encode(password.ljust(32).encode('utf-8')[:32])

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(file_data)

        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        return f"File {file_path} encrypted."

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        fernet = Fernet(self.key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
        return f"File {file_path} decrypted."
