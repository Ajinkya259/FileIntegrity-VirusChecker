import tkinter as tk
from tkinter import filedialog, messagebox
from src.integrity_checker import IntegrityChecker

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Integrity Checker")
        
        # Set the window size (width x height)
        self.root.geometry("600x400")
        
        self.integrity_checker = IntegrityChecker()
        self.create_widgets()

    def create_widgets(self):
        # Add some padding around the widgets
        self.select_button = tk.Button(self.root, text="Select Files", command=self.select_files)
        self.select_button.pack(pady=20, padx=20)
        
        self.check_button = tk.Button(self.root, text="Check Integrity", command=self.check_integrity)
        self.check_button.pack(pady=20, padx=20)
        
        # Add a label to display status messages
        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

    def select_files(self):
        self.files = filedialog.askopenfilenames()
        # Update status label
        if self.files:
            self.status_label.config(text=f"Selected {len(self.files)} file(s)")

    def check_integrity(self):
        if hasattr(self, 'files'):
            results = self.integrity_checker.check_files(self.files)
            for result in results:
                print(result)
            self.status_label.config(text="Check completed. Check the console for results.")
            messagebox.showinfo("Integrity Check Results", "Check the console for results.")
        else:
            self.status_label.config(text="No files selected.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GUI()
    app.run()
