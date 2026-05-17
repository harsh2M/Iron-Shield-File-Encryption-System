# 🔐 IRON SHIELD v3

IRON SHIELD v3 is a Python-based encryption and secure file protection system designed to explore practical cryptography, secure deletion techniques, and modern storage security concepts.

The project implements password-protected text and file encryption using Fernet symmetric cryptography, PBKDF2 key derivation, SHA-256 hashing, and secure binary file handling. Encrypted files are stored in a custom `.shield` container format with integrity validation and controlled restoration workflows.

Beyond encryption, the project investigates a critical cybersecurity misconception: deleting a file does not necessarily destroy the underlying data. Modern operating systems typically remove file references rather than immediately erasing physical binary contents, which may leave sensitive information partially recoverable until overwritten.

To study this behavior practically, IRON SHIELD v3 includes overwrite-based secure deletion mechanisms using multi-pass random-byte overwriting to reduce recoverability on traditional storage systems.

---

## 🚀 Features

* 🔐 Text Encryption & Decryption
* 🛡️ Password-Protected File Encryption
* 🔑 PBKDF2 + SHA-256 Secure Key Derivation
* ⚙️ Fernet Symmetric Encryption
* 📁 Custom `.shield` Encrypted File Format
* 🧹 Multi-Pass Secure Overwrite Deletion
* 🚫 Corruption & Invalid Password Detection
* ⚡ Binary File Processing
* 🖥️ Interactive Command-Line Interface
* 📦 Modular Python Architecture

---

## 🧠 Concepts Explored

* Applied Cryptography
* Secure File Handling
* Password-Based Authentication
* Data Remanence
* File System Behavior
* HDD vs SSD Storage Architecture
* Journaling & Storage Persistence
* Binary-Level File Operations
* Secure Software Development
* Defensive Programming

---

## ⚠️ Important Security Note

This project is intended for educational, research, and learning purposes.

While overwrite-based deletion can reduce recoverability on many traditional HDD systems, modern SSD architectures introduce complexities such as:

* Wear Leveling
* Flash Translation Layers
* TRIM Operations
* Firmware-Level Block Remapping

Because of these hardware abstractions, software-level overwriting cannot guarantee irreversible destruction on all storage devices.

---

## 📚 Learning Outcomes

This project helped strengthen my understanding of:

* Practical Cryptographic Implementation
* Operating System Storage Behavior
* Secure Deletion Limitations
* Secure System Design Principles
* Low-Level File Management in Python
* Real-World Cybersecurity Concepts

The project represents both a secure encryption utility and an exploration into how modern computing systems manage, preserve, and sometimes unintentionally retain digital information.
