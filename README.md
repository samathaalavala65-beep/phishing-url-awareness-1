# Phishing URL Awareness Checker

A beginner-friendly Python program that checks the **text** of a URL for common warning signs that may appear in phishing links.

## Six checks
1. `@` symbol in the URL
2. URL longer than 100 characters
3. IP address used as the hostname
4. Hostname with five or more dot-separated segments
5. Punycode marker (`xn--`) in the hostname
6. HTTP instead of HTTPS

## Improvements
- Check multiple URLs in one run; type `quit` to exit.
- Handle parsing errors and missing hostnames with a helpful message.

## Requirements
- Python 3
- No third-party packages required.

## Run on Android
1. Install a Python IDE such as Pydroid 3 from Google Play.
2. Save `phishing_checker.py` on your phone.
3. Open it in the IDE and tap Run.
4. Enter a URL as text, or type `quit` to exit.

## Run on a computer
```bash
python phishing_checker.py
```

## Sample test plan
These are example strings for testing. Do not visit them.

| Test | Sample input | Expected warning |
|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs |
| 2 | `http://192.0.2.10/account` | IP address; HTTP |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol; HTTP |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Five or more hostname segments |
| 5 | `https://xn--example.invalid/` | Punycode marker |

Run the tests yourself and fill in `tests/test_samples.md` with actual results. Do not claim a test passed until you have run it.

## Project structure
```text
phishing-url-awareness/
├── phishing_checker.py
├── README.md
├── requirements.txt
├── tests/test_samples.md
└── screenshots/README.md
```

## Limitations and safety
- This program only examines the URL text entered by the user.
- It does not open URLs, connect to websites, or check live reputation.
- Phishing websites can use HTTPS, and legitimate websites can use HTTP.
- A URL with no detected warning signs is not necessarily safe.

## Author details
Add your name, course, institution, and submission details before submitting.
