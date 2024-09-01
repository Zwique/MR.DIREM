import sys
import os
import requests
from colorama import init, Fore, Style
import cowsay

# Check if necessary libraries are installed
try:
    import requests
    from colorama import init, Fore, Style
    import cowsay
except ImportError as e:
    missing_lib = str(e).split()[-1]
    print(f"{Fore.RED}Missing library: {missing_lib}. Attempting to install...{Style.RESET_ALL}")
    os.system(f"pip3 install {missing_lib}")
    # Re-import after installation
    import requests
    from colorama import init, Fore, Style
    import cowsay

# Display a message using cowsay
cowsay.cow("MR.DIREM")

# Initialize colorama
init(autoreset=True)

def load_common_dirs(file_path):
    """Load directory names from a file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except IOError as e:
        print(f"{Fore.RED}Error reading file {file_path}: {e}{Style.RESET_ALL}")
        sys.exit(1)

def check_directory(url, directory):
    """Check if a directory exists on the given URL."""
    full_url = f"{url.rstrip('/')}/{directory.lstrip('/')}"
    try:
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"{Fore.LIGHTBLUE_EX}Found: {full_url}{Style.RESET_ALL}")
        elif response.status_code == 403:
            print(f"{Fore.YELLOW}Forbidden: {full_url}{Style.RESET_ALL}")
        elif response.status_code == 404:
            print(f"{Fore.RED}Not found: {full_url}{Style.RESET_ALL}")
        # Handle additional status codes as needed
    except requests.RequestException as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 3:
        print(f"{Fore.RED}Usage: python directory_scanner.py <base_url> <file_with_dirs>{Style.RESET_ALL}")
        sys.exit(1)

    base_url = sys.argv[1]
    file_path = sys.argv[2]
    
    # Load directories from the file
    common_dirs = load_common_dirs(file_path)
    
    # Print a message indicating the start of the scan
    print(f"{Fore.CYAN}Starting scan on {base_url} using directories from {file_path}...{Style.RESET_ALL}")
    
    # Check each directory
    for directory in common_dirs:
        check_directory(base_url, directory)
    
    # Print a message indicating the end of the scan
    print(f"{Fore.GREEN}Scan complete.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
