import requests
import re
import html

query = "python"
url = f"https://www.google.com/search?q={query}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    urls = re.findall(r'https?://\S+', response.text)
    for url in urls:
        decoded_url = html.unescape(url)
        url_parts = decoded_url.split("\\")
        cleaned_url = url_parts[0]
        cleaned_url = cleaned_url.replace('"', '')
        if not cleaned_url.startswith(('http://www.w3.org', 'https://www.google.com', "https://policies.google.com", "https://accounts.google.com", "https://support.google.com")):
            print(cleaned_url)
else:
    print("error")

