# (c) AzureTecDevs 2024

# Main library
import requests
import os

# Download function
def download(file, url):
	r = requests.get(url, allow_redirects=True)
	if not os.path.exists(os.path.dirname(file)):
	    os.makedirs(os.path.dirname(file))
	open(file, 'wb').write(r.content)