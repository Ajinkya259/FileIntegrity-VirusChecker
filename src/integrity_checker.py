import hashlib
import os
import json
import logging

class IntegrityChecker:
    def __init__(self, checksum_file='checksums.json', log_file='integrity_check.log'):
        self.checksum_file = checksum_file
        self.log_file = log_file
        self.hash_method = 'sha256'  # You can change to 'md5', 'sha1', etc.
        self.checksums = self.load_checksums()
        self.setup_logging()

    def setup_logging(self):
        # Configure logging
        logging.basicConfig(filename=self.log_file, level=logging.INFO,
                            format='%(asctime)s - %(message)s')

    def calculate_checksum(self, file_path):
        """Calculate checksum using the specified hash method."""
        hash_func = hashlib.new(self.hash_method)
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_func.update(chunk)
            return hash_func.hexdigest()
        except FileNotFoundError:
            return None

    def load_checksums(self):
        """Load previously stored checksums."""
        if os.path.exists(self.checksum_file):
            try:
                with open(self.checksum_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: {self.checksum_file} is corrupted or empty.")
                return {}
        return {}

    def save_checksum(self, file_path, checksum):
        """Save the new checksum in the file."""
        self.checksums[file_path] = checksum
        with open(self.checksum_file, 'w') as f:
            json.dump(self.checksums, f, indent=4)

    def log_result(self, file, result):
        """Log the result."""
        logging.info(f"{file} - {result}")

    def check_files(self, file_paths):
        """Check files against stored checksums."""
        results = []
        for file_path in file_paths:
            checksum = self.calculate_checksum(file_path)
            if checksum:
                file_name = os.path.basename(file_path)
                previous_checksum = self.checksums.get(file_path)

                if previous_checksum:
                    if checksum == previous_checksum:
                        status = "Unchanged File"
                    else:
                        status = "Tampered FILE"
                else:
                    status = "Checksum generated for new file"
                    self.save_checksum(file_path, checksum)

                results.append((file_name, status))
                self.log_result(file_name, status)
            else:
                file_name = os.path.basename(file_path)
                status = "File not found or unreadable."
                results.append((file_name, status))
                self.log_result(file_name, status)
        return results
