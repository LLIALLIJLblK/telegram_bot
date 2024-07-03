import httpx


#api_url = 'https://api.telegram.org/bot7035854081:AAFjHzxsT_vsDYsHXhVPRnctcq2RBg_A8mA/sendMessage&text=Привет,"username" !'
api_url = 'https://api.telegram.org/bot7035854081:AAFjHzxsT_vsDYsHXhVPRnctcq2RBg_A8mA/sendMessage?chat_id=887577092&text=hello'

response = httpx.get(api_url)

if response.status_code ==200:
    data = response.text
    print(data)

else:
    print(response.status_code)