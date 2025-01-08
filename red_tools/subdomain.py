#!/usr/bin/python3

import sys
import requests

def main():
    if len(sys.argv) < 3:
        print(f"Bruk: python3 {sys.argv[0]} <domene/IP> <wordlist>")
        sys.exit(1)


    domain = sys.argv[1]
    wordlist_path = sys.argv[2]

    try:
        with open(wordlist_path, "r") as f:
            subdomains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Finner ikke filen '{wordlist_path}'. Sjekk at filen finnes.")
        sys.exit(1)

    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"Valid domain: {url}")
        except requests.ConnectionError:
            pass
        except requests.exceptions.Timeout:
            print(f"Timeout for {url}")
        except requests.exceptions.RequestException as e:
            print(f"Feil ved henting av {url}: {e}")

if __name__ == "__main__":
    main()

