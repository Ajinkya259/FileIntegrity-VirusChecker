# File Integrity and Virus Checker

## Overview

The **File Integrity and Virus Checker** is a Python application designed to ensure the integrity of files by calculating checksums and scanning for potential viruses using the VirusTotal API. This application helps users maintain the security and reliability of their files by providing a user-friendly graphical interface.

## Features

- **File Integrity Checking**: Calculates checksums for selected files and checks them against previously stored checksums to identify any modifications.
- **Virus Scanning**: Integrates with the VirusTotal API to scan files for potential threats and vulnerabilities.
- **Logging**: Logs all actions and results in a designated log file for auditing purposes.
- **User-Friendly GUI**: Built with Tkinter, providing an intuitive interface for users to interact with the application.

## Requirements

- Python 3.x
- `requests` library for making HTTP requests to the VirusTotal API
- `tkinter` for the graphical user interface
- `hashlib` for checksum calculations

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/FileIntegrityAndVirusChecker.git
   cd FileIntegrityAndVirusChecker

2. Install the required packages:

    ```bash
    
    pip install requests

3. Ensure you have a valid API key for VirusTotal. 
    Replace the placeholder API key in the scanner.py file with your actual API key.


### Usage
Run the application:

    1. python gui.py

    2. Use the Select Files button to choose the files you want to check.

    3. Click on Check Integrity to calculate and verify checksums against previously stored values.

    4. Click on Scan for Viruses to scan the selected files for potential threats.

### Test
Steps to Test with an Unsafe File:

    X5O!P%@AP[4\PZX54(P^)7CC)7{Q!EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H* 
    
Copy the above line into a text file named "eicar.com"


### Logging

    The application logs actions and results in the integrity_check.log file.
    This file contains a record of all integrity checks and virus scan results for auditing and troubleshooting purposes.

### Contributing

    Contributions are welcome! If you have suggestions for improvements or additional features,
    feel free to create an issue or submit a pull request.

### License

    This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements

    VirusTotal for providing the API for virus scanning.
    Tkinter for the graphical user interface framework.


### Key Sections Included:
- **Overview:** A brief introduction to the project.
- **Features:** Highlights the main functionalities.
- **Requirements:** Lists the necessary dependencies.
- **Installation:** Step-by-step instructions for setting up the project.
- **Usage:** Explains how to run and use the application.
- **File Structure:** Provides a visual of the project structure.
- **Logging:** Details the logging mechanism for auditing.
- **Contributing:** Encourages collaboration and contributions.
- **License:** Indicates the licensing information.
- **Acknowledgements:** Credits any external libraries or services used.


