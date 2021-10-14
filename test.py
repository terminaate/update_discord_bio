import requests as rt
import json
from threading import Thread
from time import sleep
import re

from requests.api import get

with open('settings.json', 'r') as r:
    settings = json.load(r)
    
header = {
    'authorization' : settings['token']
}

guilds_ids = []

def get_guilds_ids() -> list:
    r = rt.get(
        "https://discord.com/api/v9/users/@me/guilds",
        headers=header
    )
    r = json.loads(r.text)
    print(r)
    for i in r:
        guilds_ids.append(i['id'])
    return guilds_ids
    
def edit_guild_nick(guild_id, nick):
    print(guild_id)
    print(rt.patch(
        f"https://discord.com/api/v9/guilds/{guild_id}/members/@me",
        headers=header,
        json={'nick' : nick}
    ))
    sleep(10)


def rand_nick() -> str:
    return json.loads(rt.get("https://cryptons.ga/api/v1/randomusername").text)['output']


def update_guild_nick():
    while True:
        for i in get_guilds_ids():
            edit_guild_nick(i, rand_nick())
            sleep(3)
            
if __name__ == '__main__':
    Thread(target=update_guild_nick).start()
