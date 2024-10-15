import os
import json
import hashlib
import zlib

BASELINE_FILE = 'checker/baseline.json'

class IntegrityChecker:
    def __init__(self):
        self.baseline = self.load_baseline()

    def load_baseline(self):
        if os.path.exists(BASELINE_FILE):
            try:
                with open(BASELINE_FILE, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def update_baseline(self, folder_path):
        baseline = {}
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                baseline[file_path] = self.get_file_hash(file_path)
        with open(BASELINE_FILE, 'w') as file:
            json.dump(baseline, file, indent=4)
        self.baseline = baseline
        return "Baseline updated."

    def check_integrity(self, folder_path):
        current_files = {}
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                current_files[file_path] = self.get_file_hash(file_path)

        added_files = [file for file in current_files if file not in self.baseline]
        deleted_files = [file for file in self.baseline if file not in current_files]
        modified_files = [
            file for file in current_files
            if file in self.baseline and current_files[file] != self.baseline[file]
        ]

        return {
            "added_files": added_files,
            "deleted_files": deleted_files,
            "modified_files": modified_files,
        }
    @staticmethod
    def get_file_hash(file_path):
        crc32_hash = 0
        md5_hash = hashlib.md5()
        sha256_hash = hashlib.sha256()
        blake2b_hash = hashlib.blake2b(digest_size=32)  

        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):
                crc32_hash = zlib.crc32(chunk, crc32_hash)
                md5_hash.update(chunk)
                sha256_hash.update(chunk)
                blake2b_hash.update(chunk)

        crc32_result = f"{crc32_hash:08x}"  
        md5_result = md5_hash.hexdigest()
        sha256_result = sha256_hash.hexdigest()
        blake2b_result = blake2b_hash.hexdigest()

        print(f"CRC32 Hash: {crc32_result}")
        print(f"MD5 Hash: {md5_result}")
        print(f"SHA-256 Hash: {sha256_result}")
        print(f"Blake2b Hash: {blake2b_result}")

        hybrid_hash = (
            crc32_result +         
            md5_result +         
            sha256_result +      
            blake2b_result       
        )
        
        print(f"Hybrid Hash: {hybrid_hash}")

        return hybrid_hash
    
