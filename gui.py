import sys
import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from integrity_checker import IntegrityChecker
from scanner import FileScanner

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Integrity and Virus Checker")
        self.root.geometry("700x500")  # Adjusted window size for better usability

        self.integrity_checker = IntegrityChecker()
        self.file_scanner = FileScanner(api_key="a1c9d5ffd22ed1dc0557cebf6f9451bc7fce4e21947039c670830c5dcd0aeaaa")
        self.create_widgets()

    def create_widgets(self):
        # Define button width for uniform size
        button_width = 20

        self.select_button = tk.Button(self.root, text="Select Files", command=self.select_files, width=button_width)
        self.select_button.pack(pady=20)

        self.check_button = tk.Button(self.root, text="Check Integrity", command=self.check_integrity, width=button_width)
        self.check_button.pack(pady=10)

        self.scan_button = tk.Button(self.root, text="Scan for Viruses", command=self.scan_files, width=button_width)
        self.scan_button.pack(pady=10)

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"))  # Bold font for status label
        self.status_label.pack(pady=10)

        # Area for displaying results
        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(pady=20)

    def clear_results(self):
        # Clear the results displayed in the result_frame
        for widget in self.result_frame.winfo_children():
            widget.destroy()

    def display_result(self, results):
        self.clear_results()
        for file_name, status in results:
            result_label = tk.Label(self.result_frame, text=f"{file_name}: {status}", font=("Helvetica", 12, "bold"))  # Larger and bold font
            result_label.pack(anchor="w", padx=10)

    def select_files(self):
        self.files = filedialog.askopenfilenames()
        if self.files:
            self.status_label.config(text=f"Selected {len(self.files)} file(s)")
        else:
            self.status_label.config(text="No files selected.")

    def check_integrity(self):
        if hasattr(self, 'files'):
            results = self.integrity_checker.check_files(self.files)
            self.display_result(results)
            self.status_label.config(text="Integrity check completed.")
        else:
            self.status_label.config(text="No files selected.")

    def scan_files(self):
        if hasattr(self, 'files'):
            for file_path in self.files:
                try:
                    result = self.file_scanner.scan_file(file_path)
                    file_id = result.get("data", {}).get("id")
                    
                    if not file_id:
                        error_message = result.get('error', {}).get('message', 'Unknown error')
                        messagebox.showerror("Error", f"File scan failed: {error_message}")
                        continue

                    report = None
                    retry_count = 0
                    max_retries = 10
                    while not report and retry_count < max_retries:
                        report = self.file_scanner.get_report(file_id)
                        if report and "error" not in report:
                            malicious = report['data']['attributes']['stats']['malicious']
                            suspicious = report['data']['attributes']['stats']['suspicious']
                            undetected = report['data']['attributes']['stats']['undetected']

                            result_status = "File is safe" if malicious == 0 and suspicious == 0 else "Warning..! Unsafe file"
                            result_color = "green" if malicious == 0 and suspicious == 0 else "red"

                            # Display scan result for each file
                            scan_label = tk.Label(self.result_frame, text=f"{os.path.basename(file_path)}: {result_status}", fg=result_color, font=("Helvetica", 12, "bold"))  # Larger and bold font
                            scan_label.pack(anchor="w", padx=10)
                            break
                        else:
                            retry_count += 1
                            self.status_label.config(text="Waiting for scan result...")
                            self.root.update()  # Update the GUI to reflect changes
                            time.sleep(5)

                    # If after retries, the report is still not available
                    if retry_count == max_retries:
                        messagebox.showerror("Error", f"Failed to get a valid report after {max_retries} attempts.")
                except Exception as e:
                    messagebox.showerror("Error", f"An exception occurred: {str(e)}")

            # Update status label after scanning is completed
            self.status_label.config(text="Scan completed.")
        else:
            messagebox.showwarning("Warning", "No files selected.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GUI()
    app.run()
