import requests as rt
from time import sleep
import json, datetime
from threading import Thread

with open('settings.json', 'r') as r:
    header = json.load(r)['header']

def edit_bio(bio: str):
    link = 'https://discord.com/api/v9/users/@me'
    data = {'bio': bio}
    rt.patch(link, headers=header, json=data)

def update_bio():
    last_time = ""
    while True:
        now_time = datetime.datetime.now()
        hours_time = now_time.strftime('%I')
        minuts_time = int(now_time.strftime('%M'))
        status_time = now_time.strftime('%p').lower()
        if last_time != hours_time:
            if minuts_time == 00 or minuts_time == 10 or minuts_time == 20 or minuts_time == 30 or minuts_time == 40 or minuts_time == 50:
                edit_bio(f"```[!] Error 404 : the meaning of life is not found```")
                sleep(10)
                edit_bio(f"```[!] Error 429 : I'm trying to escape from something that you can't escape from.```")
                sleep(16)
                for i in ['.', '..', '...']:
                    edit_bio(f"```Fix some errors{i}```")
                    sleep(1)
            else:
                edit_bio(f"```Its {int(hours_time)}{status_time} and i still miss you```")
        sleep(60)


if __name__ == "__main__":
    Thread(target=update_bio).start()
