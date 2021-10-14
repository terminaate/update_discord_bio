import requests
from time import sleep
import json
import datetime
from threading import Thread
import random
from nickname_generator import generate as rand_nick

with open('settings.json', 'r') as r:
    settings = json.load(r)

header = {"authorization": settings['token']}

def rand_url():
    urls = ["https://cutt.ly/OE77qdy", "https://cutt.ly/1E77rnI"]
    nurl = random.choice(urls)
    return nurl

def edit_bio(bio: str):
    link = 'https://discord.com/api/v9/users/@me'
    data = {'bio': bio}
    requests.patch(link, headers=header, json=data)

def edit_status(status: str):
    link = 'https://discordapp.com/api/v9/users/@me/settings'
    data = {'custom_status': {'text': status}}
    requests.patch(link, headers=header, json=data)

def update_bio():
    last_time = ""
    while True:
        now_time = datetime.datetime.now()
        hours_time = now_time.strftime('%I')
        minuts_time = int(now_time.strftime('%M'))
        status_time = now_time.strftime('%p').lower()
        if last_time != hours_time:
            if minuts_time == 00 or minuts_time == 10 or minuts_time == 20 or minuts_time == 30 or minuts_time == 40 or minuts_time == 50:
                edit_bio(f"```Its01``` **{rand_url()}** ```01 and eErOR i s12ti4ll6 mi76ss12 you```")
                sleep(10)
                for i in ['.', '..', '...']:
                    edit_bio(f"```Fix some errors{i}```")
                    sleep(1)
            else:
                edit_bio(f"```Its {int(hours_time)}{status_time} and i still miss you```")
        sleep(60)
        

guilds_ids = []


def get_guilds_ids() -> list:
    r = requests.get(
        "https://discord.com/api/v9/users/@me/guilds",
        headers=header
    )
    r = json.loads(r.text)
    for i in r:
        guilds_ids.append(i['id'])
    return guilds_ids


def edit_guild_nick(guild_id, nick):
    requests.patch(
        f"https://discord.com/api/v9/guilds/{guild_id}/members/@me",
        headers=header,
        json={'nick': nick}
    )
    sleep(8)


def update_guild_nick():
    while True:
        for i in get_guilds_ids():
            edit_guild_nick(i, rand_nick())
            sleep(3)
    
def update_status():
    while True:
        for i in '\|/-':
            edit_status(f"{i} Hacking the world.")
        sleep(1)



if __name__ == "__main__":
    Thread(target=update_bio).start()
    Thread(target=update_status).start()
    Thread(target=update_guild_nick).start()
