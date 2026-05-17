# decrypt.py
from cryptography.fernet import Fernet
from utils import derive_key
import os

def decrypt_text(encrypted_data: bytes, password: str) -> str:
    salt = encrypted_data[:16]
    actual_data = encrypted_data[16:]

    key = derive_key(password, salt)
    cipher = Fernet(key)

    decrypted_data = cipher.decrypt(actual_data)
    return decrypted_data.decode()


def decrypt_file(input_file: str, password: str) -> str:
    """
    Decrypts a .shield file and restores original file
    """

    # ✅ Validate extension first
    if not input_file.endswith(".shield"):
        raise ValueError("Invalid file format")
    
    with open(input_file, "rb") as f:
        file_data = f.read()

     # ✅ Validate file size
    if len(file_data) < 17:
        raise ValueError("Invalid or corrupted file.")

    salt = file_data[:16]
    actual_data = file_data[16:]

    key = derive_key(password, salt)
    cipher = Fernet(key)

    try:
        decrypted_data = cipher.decrypt(actual_data)
    except Exception:
        raise ValueError("Incorrect password or corrupted file")
    
    # Remove .shield extension not because i removed it
    output_file = input_file[:-7]

    if os.path.exists(output_file):
        raise FileExistsError("Output file already exists.")

    with open(output_file, "wb") as f:
        f.write(decrypted_data)

    return output_file