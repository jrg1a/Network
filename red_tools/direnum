import requests
import sys

def main():
    # Sjekk at vi har fått inn domenet som argument
    if len(sys.argv) < 2:
        print(f"Bruk: python {sys.argv[0]} <domene>")
        sys.exit(1)

    domain = sys.argv[1]

    # Bruk kontekstblokk for å forsikre oss om at filen lukkes
    try:
        with open("wordlist.txt", "r") as f:
            # Fjern tomme linjer og trailing spaces
            directories = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Finner ikke wordlist.txt. Kontroller at fila ligger i samme mappe.")
        sys.exit(1)

    for directory in directories:
        url = f"http://{domain}/{directory}.html"
        try:
            r = requests.get(url, timeout=5)
            # Sjekk alle statuskoder utenom 404 (eller velg selv hva du anser som 'valid')
            if r.status_code != 404:
                print(f"Valid directory: {url}")
        except requests.exceptions.RequestException as e:
            # Håndter alle typer requests-feil (ConnectionError, Timeout, etc.)
            print(f"Feil ved forespørsel mot {url}: {e}")

if __name__ == "__main__":
    main()
