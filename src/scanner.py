import requests
import os
import time

class FileScanner:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.virustotal.com/api/v3"
        self.max_file_size_mb = 650  # Maximum file size in MB for VirusTotal

    def scan_file(self, file_path):
        # Check file size before uploading
        file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB
        if file_size > self.max_file_size_mb:
            return {"error": {"message": f"File size exceeds the {self.max_file_size_mb} MB limit."}}
        url = f"{self.base_url}/files"
        headers = {
            "x-apikey": self.api_key
        }
        try:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = requests.post(url, headers=headers, files=files)
                
                # Check for a successful response
                if response.status_code != 200:
                    return {"error": response.json()}
                
                return response.json()
        except FileNotFoundError:
            return {"error": {"message": "File not found."}}
        except requests.exceptions.RequestException as e:
            return {"error": {"message": f"Network error: {str(e)}"}}

    def get_report(self, file_id, max_retries=3, wait_time=5):
        url = f"{self.base_url}/analyses/{file_id}"
        headers = {
            "x-apikey": self.api_key
        }
        
        for attempt in range(max_retries):
            response = requests.get(url, headers=headers)

            # If the response is successful, return the report
            if response.status_code == 200:
                return response.json()

            # If not successful, wait and retry
            if attempt < max_retries - 1:
                time.sleep(wait_time)
        
        return {"error": {"message": "Failed to retrieve report after multiple attempts."}}

    def check_file_status(self, file_id):
        """Check the status of the file analysis."""
        url = f"{self.base_url}/analyses/{file_id}"
        headers = {
            "x-apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()
