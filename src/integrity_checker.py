import hashlib
import os
import json
import logging

class IntegrityChecker:
    def __init__(self, checksum_file='src/checksums.json', log_file='src/logs/integrity_check.log'):
        self.checksum_file = checksum_file
        self.log_file = log_file
        self.checksums = self.load_checksums()
        self.setup_logging()

    def setup_logging(self):
        # Configure logging
        logging.basicConfig(filename=self.log_file, level=logging.INFO,
                            format='%(asctime)s - %(message)s')

    def calculate_checksum(self, file_path, hash_function='sha256'):
        hasher = hashlib.new(hash_function)
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def load_checksums(self):
        if os.path.exists(self.checksum_file):
            try:
                with open(self.checksum_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: {self.checksum_file} is corrupted or empty.")
                return {}
        return {}

    def save_checksum(self, file_path, checksum):
        self.checksums[file_path] = checksum
        with open(self.checksum_file, 'w') as f:
            json.dump(self.checksums, f)

    def log_result(self, file, result):
        # Log the result to the file
        logging.info(f"{file} - {result}")

    def check_files(self, files):
        results = []
        for file in files:
            current_checksum = self.calculate_checksum(file)
            previous_checksum = self.checksums.get(file)
            
            print(f"Checking file: {file}")
            print(f"Current checksum: {current_checksum}")
            print(f"Previous checksum: {previous_checksum}")

            if previous_checksum:
                if current_checksum == previous_checksum:
                    result = "Unchanged"
                else:
                    result = "Altered"
            else:
                result = "New file, checksum saved"
                self.save_checksum(file, current_checksum)

            results.append(f"{file} - {result}")
            self.log_result(file, result)

        return results
