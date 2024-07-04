import httpx #ДЛЯ РЕКВЕСТОВ
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7035854081:AAFjHzxsT_vsDYsHXhVPRnctcq2RBg_A8mA'
TEXT = 'Новый апдейт'
MAX_COUNTER = 100
API_CAT = 'https://api.thecatapi.com/v1/images/search'

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    print(f"attempt = {counter}")

    updates = httpx.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}").json()
    cat_photo = httpx.get("https://api.thecatapi.com/v1/images/search").json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = httpx.get(API_CAT)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                httpx.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                httpx.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={"error"}')



    time.sleep(1)
    counter += 1