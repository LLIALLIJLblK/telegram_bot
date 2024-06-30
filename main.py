import httpx


api_url = 'http://api.open-notify.org/iss-now.json'

response = httpx.get(api_url)

if response.status_code ==200:
    print(response.text)

else:
    print(response.status_code)