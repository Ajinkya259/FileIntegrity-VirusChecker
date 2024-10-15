# frontend/gui.py

import tkinter as tk
from tkinter import filedialog
from checker.integrity_checker import IntegrityChecker
from checker.file_encryptor import FileEncryptor  

class IntegrityCheckerGUI:
    def __init__(self):
        self.checker = IntegrityChecker()
        self.root = tk.Tk()
        self.root.title("Folder Integrity Checker")
        self.folder_path = tk.StringVar()
        self.file_path = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self.root, text="Check Integrity", font=('Arial', 14, 'bold'), fg="white").grid(row=0, column=0, columnspan=3, pady=(10, 5))

        tk.Label(self.root, text="Select Folder:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.folder_path, width=50).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_folder).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Update Baseline", command=self.update_baseline).grid(row=2, column=1, pady=10)
        tk.Button(self.root, text="Check Integrity", command=self.check_integrity).grid(row=3, column=1, pady=10)

        self.status_label = tk.Label(self.root, text="", fg="white")
        self.status_label.grid(row=4, column=0, columnspan=3, pady=5)

        self.modified_files_label = tk.Label(self.root, text="Modified Files: ")
        self.modified_files_label.grid(row=5, column=0, sticky='w', padx=10, pady=5)

        self.new_files_label = tk.Label(self.root, text="Newly Added Files: ")
        self.new_files_label.grid(row=6, column=0, sticky='w', padx=10, pady=5)

        self.deleted_files_label = tk.Label(self.root, text="Deleted Files: ")
        self.deleted_files_label.grid(row=7, column=0, sticky='w', padx=10, pady=5)

        self.modified_files_text = tk.Label(self.root, text="", anchor='w', justify='left')
        self.modified_files_text.grid(row=5, column=1, sticky='w', padx=10, pady=5)

        self.new_files_text = tk.Label(self.root, text="", anchor='w', justify='left')
        self.new_files_text.grid(row=6, column=1, sticky='w', padx=10, pady=5)

        self.deleted_files_text = tk.Label(self.root, text="", anchor='w', justify='left')
        self.deleted_files_text.grid(row=7, column=1, sticky='w', padx=10, pady=5)

        tk.Label(self.root, text="Encrypt-Decrypt Files", font=('Arial', 14, 'bold'), fg="white").grid(row=8, column=0, columnspan=3, pady=(20, 5))

        tk.Label(self.root, text="Select File to Encrypt/Decrypt:").grid(row=9, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.file_path, width=50).grid(row=9, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse File", command=self.browse_file).grid(row=9, column=2, padx=10, pady=10)

        tk.Label(self.root, text="Enter Password:").grid(row=10, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.password, width=50, show="*").grid(row=10, column=1, padx=10, pady=10)

        self.file_status_label = tk.Label(self.root, text="", fg="white")
        self.file_status_label.grid(row=11, column=0, columnspan=3, pady=5)

        tk.Button(self.root, text="Encrypt File", command=self.encrypt_file).grid(row=12, column=1, pady=10)
        tk.Button(self.root, text="Decrypt File", command=self.decrypt_file).grid(row=13, column=1, pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)
            self.status_label.config(text=f"Selected folder: {folder_selected}")

    def update_baseline(self):
        folder = self.folder_path.get()
        if folder:
            message = self.checker.update_baseline(folder)
            self.status_label.config(text=message)  
        else:
            self.status_label.config(text="Please select a folder to update the baseline.", fg="white")

    def check_integrity(self):
        folder = self.folder_path.get()
        if folder:
            results = self.checker.check_integrity(folder)

            self.modified_files_text.config(text=", ".join(results["modified_files"]) or "None")
            self.new_files_text.config(text=", ".join(results["added_files"]) or "None")
            self.deleted_files_text.config(text=", ".join(results["deleted_files"]) or "None")

            self.status_label.config(text="Integrity check completed.", fg="white")
        else:
            self.status_label.config(text="Please select a folder to check integrity.", fg="white")

    def browse_file(self):
        file_selected = filedialog.askopenfilename()
        if file_selected:
            self.file_path.set(file_selected)
            self.file_status_label.config(text=f"Selected file: {file_selected}", fg="white")

    def encrypt_file(self):
        file_path = self.file_path.get()
        password = self.password.get()
        if file_path and password:
            encryptor = FileEncryptor(password)
            message = encryptor.encrypt_file(file_path)
            self.file_status_label.config(text=message, fg="white")
        else:
            self.file_status_label.config(text="Please select a file and enter a password.", fg="white")

    def decrypt_file(self):
        file_path = self.file_path.get()
        password = self.password.get()
        if file_path and password:
            encryptor = FileEncryptor(password)
            try:
                message = encryptor.decrypt_file(file_path)
                self.file_status_label.config(text=message, fg="white")
            except Exception:
                self.file_status_label.config(text="Decryption failed. Incorrect password.", fg="white")
        else:
            self.file_status_label.config(text="Please select a file and enter a password.", fg="white")

    def run(self):
        self.root.mainloop()
