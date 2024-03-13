# (c) AzureTecDevs 2024

# Main library
import requests

# Download function
def download(file, url):
	r = requests.get(url, allow_redirects=True)
	open(file, 'w').write(r.content)