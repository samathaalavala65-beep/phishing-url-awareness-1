from urllib.parse import urlparse
import ipaddress

def check_url(url):
    """Check URL text only. This program never visits the website."""
    warnings = []
    try:
        parsed = urlparse(url.strip())
        hostname = parsed.hostname
    except ValueError:
        return ["Invalid URL format: could not parse this address."]

    if not url.strip() or not hostname:
        return ["Invalid URL: enter a complete address with a hostname."]

    if "@" in url:
        warnings.append("Contains '@' symbol.")
    if len(url) > 100:
        warnings.append("Unusually long URL (more than 100 characters).")

    try:
        ipaddress.ip_address(hostname)
        warnings.append("Uses an IP address instead of a domain name.")
    except ValueError:
        pass

    if len(hostname.split(".")) >= 5:
        warnings.append("Hostname has five or more segments.")
    if "xn--" in hostname.lower():
        warnings.append("Contains a punycode marker (xn--).")
    if parsed.scheme.lower() == "http":
        warnings.append("Uses HTTP instead of HTTPS.")
    elif parsed.scheme.lower() != "https":
        warnings.append("Uses an unusual or missing URL scheme.")

    return warnings


def main():
    print("PHISHING URL AWARENESS CHECKER")
    print("Checks URL text only; it does not open websites.")
    print("No warnings does NOT guarantee that a URL is safe.\n")
    while True:
        url = input("Enter a URL (or type 'quit' to exit): ").strip()
        if url.lower() == "quit":
            print("Thank you for using the checker.")
            break
        results = check_url(url)
        if results:
            print("\nWarning signs found:")
            for warning in results:
                print("- " + warning)
        else:
            print("\nNo listed warning signs were detected.")
            print("This does not prove that the website is safe.")
        print()


if __name__ == "__main__":
    main()
