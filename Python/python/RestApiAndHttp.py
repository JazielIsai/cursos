# Vamos a hacer una petición request
import requests
url = 'https://www.ibm.com/'
r = requests.get(url)
print(r.status_code)
print(r.request.headers)
