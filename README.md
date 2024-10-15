### Folder Integrity Checker
1.  The Folder Integrity Checker is a Python-based tool for monitoring the integrity of files within a directory. By hashing files and storing their unique signatures in a baseline file, it helps identify any modifications, additions, or deletions to files, maintaining data integrity over time. Additionally, the application includes an encryption and decryption module, providing security for sensitive files.

### Features
File Integrity Monitoring: Detect changes in files by comparing their hash signatures to the baseline.
Hybrid Hashing Algorithm: Uses a combination of CRC32, MD5, SHA-256, and Blake2b algorithms for a robust file signature.
Encryption and Decryption Module: Encrypts and decrypts files with a user-provided password, adding a layer of security.
User-Friendly GUI: Built with Tkinter for easy interaction.


### Installation:

1. **Clone the repository** :
git clone https://github.com/Ajinkya259/folder-integrity-checker.git
cd folder-integrity-checker
2. **Install Dependencies**: Ensure Python 3.8 or later is installed. 
    pip install -r requirements.txt
3. **Run the Application**:
    python main.py

### Usage
1. Update Baseline:
    Use the "Update Baseline" button to create or update the baseline of hashes for files in the selected folder.
    The baseline data is saved in checker/baseline.json.
2. Check Integrity:
    Select a folder and click "Check Integrity" to compare the current files with the baseline.
    The tool will display any added, deleted, or modified files.
3. Encryption and Decryption:
    *Encrypt Files*: Select files, provide a password, and encrypt them using the "Encrypt" button. The encrypted files are saved in a secure format.
    *Decrypt Files*: Choose encrypted files, enter the correct password, and click "Decrypt" to restore them to their original state.

## Project Structure

folder-integrity-checker/
│
├── checker/
│   ├── integrity_checker.py       # Integrity checker logic with hybrid hashing
│   ├── encryption_module.py       # Encryption and decryption functionality
│   └── baseline.json              # Stores baseline hashes
│
├── frontend/
│   └── gui.py                     # Tkinter-based GUI for the tool
│
├── main.py                        # Main file to launch the application
└── README.md                      # Project documentation

**Hybrid Hashing Algorithm:**
    The tool uses a custom hybrid hashing approach that combines the following algorithms:

1. CRC32: Fast, commonly used for checksums but less secure alone.
2. MD5: Provides a unique hash but vulnerable to collisions; used here in combination.
3. SHA-256: A secure cryptographic hash.
4. Blake2b: A modern, high-performance cryptographic hash.
    The combination ensures both speed and reliability in integrity checking.

**Encryption and Decryption Module**
    This module allows users to encrypt files with a password and decrypt them as needed. It uses AES-256 encryption to secure sensitive data, making sure files are accessible only to those with the correct password.

**Contributing**
Feel free to submit issues or pull requests. Contributions are welcome!

**License**
This project is licensed under the MIT License.








