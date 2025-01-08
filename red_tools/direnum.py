import requests
import sys

def main():
    # Check that the domain is provided as an argument
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    try:
        with open("wordlist.txt", "r") as f:
            # Remove empty lines and trailing spaces
            directories = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("wordlist.txt not found. Ensure the file is in the same directory.")
        sys.exit(1)

    for directory in directories:
        url = f"http://{domain}/{directory}.html"
        try:
            r = requests.head(url, timeout=5)
            if r.status_code != 404:
                print(f"Valid directory: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error requesting {url}: {e}")

if __name__ == "__main__":
    main()