# File Integrity Checker

## Overview
This project is a File Integrity Checker that allows users to select files or directories and verifies their integrity using checksums (e.g., SHA-256). The project supports both command-line and GUI-based interaction.

## Installation
1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the project using `python main.py`.

## Usage
- **Command-Line Interface:** Run `python main.py` followed by the files or directories you want to check.
- **Graphical Interface (Optional):** Run `python src/ui/gui.py` to start the GUI.

## Configuration
Modify `config/config.yaml` to set the hash function and other settings.

## Testing
Run tests using `python -m unittest discover tests`.

## Logs
Logs are stored in the `logs/` directory.
