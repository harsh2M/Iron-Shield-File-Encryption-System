# encrypt.py
from cryptography.fernet import Fernet
from utils import generate_salt, derive_key
import os

def encrypt_text(data: str, password: str) -> bytes:
    salt = generate_salt()
    key = derive_key(password, salt)
    cipher = Fernet(key)

    encrypted_data = cipher.encrypt(data.encode())
    return salt + encrypted_data


def encrypt_file(input_file: str, password: str, overwrite: bool = False) -> str:
    """
    Encrypts a file, saves it as .shield, and deletes original safely.
    """
    salt = generate_salt()
    key = derive_key(password, salt)
    cipher = Fernet(key)

    # Read original file
    with open(input_file, "rb") as f:
        file_data = f.read()

    encrypted_data = cipher.encrypt(file_data)

    output_file = input_file + ".shield"

    # ⚠️ Check for duplicate
    if os.path.exists(output_file):
        if not overwrite:
            raise FileExistsError("Encrypted file already exists.")

    # Write encrypted file
    with open(output_file, "wb") as f:
        f.write(salt + encrypted_data)

    # ✅ SAFETY CHECK: ensure file exists before deleting original
    #shifted to main.py to confirm first then delete it irreversibly

    return output_file

def secure_delete(file_path: str, passes: int = 3):
    if not os.path.exists(file_path):
        return

    length = os.path.getsize(file_path)

    with open(file_path, "r+b") as f:
        for _ in range(passes):
            f.seek(0)
            f.write(os.urandom(length))

    # Rename file before deletion
    temp_name = file_path + ".deleted"
    os.rename(file_path, temp_name)

    os.remove(temp_name)