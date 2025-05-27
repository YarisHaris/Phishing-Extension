import os
import requests

def check_url_safe(url):
    api_key = os.getenv("GOOGLE_API_KEY")
    body = {
        "client": {
            "clientId": "your-extension-name",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    res = requests.post(
        f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}",
        json=body
    )

    data = res.json()
    return bool(data.get("matches"))
