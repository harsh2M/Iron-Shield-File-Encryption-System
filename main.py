# main.py
from encrypt import encrypt_text, encrypt_file, secure_delete
from decrypt import decrypt_text, decrypt_file
import base64
import getpass

def main():
    print("🛡️ IRON SHIELD v3 (File Protection Enabled)")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Encrypt File")
    print("4. Decrypt File")

    choice = input("Choose option (1/2/3/4): ")
    password = getpass.getpass("Enter password: ")
    if choice == "1":
        data = input("Enter text to encrypt: ")
        encrypted = encrypt_text(data, password)
        encoded = base64.urlsafe_b64encode(encrypted).decode()

        print("\n🔒 Encrypted Data:")
        print(encoded)

    elif choice == "2":
        data = input("Enter encrypted text: ")
        try:
            decoded = base64.urlsafe_b64decode(data.encode())
            decrypted = decrypt_text(decoded, password)

            print("\n🔓 Decrypted Data:")
            print(decrypted)

        except Exception:
            print("❌ Access Denied!")

    elif choice == "3":
        file_path = input("Enter file path: ")
        try:
            try:
                output = encrypt_file(file_path, password)
                print(f"\n🛡️ File Encrypted: {output}")

            except FileExistsError:
                print("⚠️ Encrypted file already exists!")
                choice = input("Replace existing file? (y/n): ")

                if choice.lower() == 'y':
                    output = encrypt_file(file_path, password, overwrite=True)
                    print(f"\n🛡️ File Encrypted (Overwritten): {output}")
                else:
                    print("❌ Encryption cancelled.")
                    return

            # ✅ Ask AFTER encryption
            print("⚠️ Warning: Secure deletion is irreversible!")
            confirm = input("🛑 Securely delete original file? (y/n): ")

            if confirm.lower() == 'y':
                secure_delete(file_path)
                print("🧹 Original file securely deleted.")
            else:
                print("📁 Original file kept.")
        
        except FileNotFoundError:
            print("❌ Original File not found.")   
        except Exception as e:
            print(f"❌ Error encrypting file: {e}")

    elif choice == "4":
        file_path = input("Enter .shield file path: ")
        try:
            output = decrypt_file(file_path, password)
            print(f"\n🔓 File Decrypted: {output}")

             # ⚠️ Ask before deleting encrypted file
            print("⚠️ Warning: This will delete the encrypted (.shield) file.")
            confirm = input("Delete encrypted file after decryption? (y/n): ")

            if confirm.lower() == 'y':
                secure_delete(file_path)
                print("🧹 Encrypted file securely deleted.")
            else:
                print("📁 Encrypted file kept.")

        except Exception as e:
            print(f"❌ Access Denied or corrupted file: {e}")

    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()