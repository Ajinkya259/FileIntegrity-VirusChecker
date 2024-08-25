import sys
from src.integrity_checker import IntegrityChecker

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <file1> [<file2> ...]")
        sys.exit(1)

    files = sys.argv[1:]
    integrity_checker = IntegrityChecker()
    results = integrity_checker.check_files(files)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
