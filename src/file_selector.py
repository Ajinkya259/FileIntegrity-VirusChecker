import argparse
import os

class FileSelector:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="File Integrity Checker")
        self.parser.add_argument("files", metavar="F", type=str, nargs="+", help="Files or directories to check")

    def select_files(self):
        args = self.parser.parse_args()
        files = []
        for path in args.files:
            if os.path.isfile(path):
                files.append(path)
            elif os.path.isdir(path):
                for root, _, filenames in os.walk(path):
                    for filename in filenames:
                        files.append(os.path.join(root, filename))
        return files
