import websocket
import json

with open('settings.json', 'r') as r:
    token = json.load(r)["header"]["authorization"]

ws = websocket.WebSocket()
ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
heartbeat_interval = json.loads(ws.recv())['d']['heartbeat_interval']
ws.send(json.dumps({
    "op": 2,
    "d": {
        "token": token,
        "properties": {
            "$os": "windows",
            "$browser": "Discord",
            "$device": "desktop"
        }
    }
}
)
)

activity = {
    "type": 0,
    "name": "Hacking The World",
    "details": "Not your buissnes ;)",
    "timestamps": {
        "start": 1507665886
    },
    "application_id": "909945005462925322",
    "assets": {
        "large_image": "909948361988247602",
        "large_text": "Not Your Buissnes",
        "small_text": "I SAY NOT YOUR BUISSNES"
    },
    "party": {
        "id": "ae488379-351d-4a4f-ad32-2b9b01c91657",
        "size": [1, 5]
    },
    "secrets": {
        "join": "MTI4NzM0OjFpMmhuZToxMjMxMjM= "
    }
}

payload = {
    "op": 3,
    "d": {
        "since": 9999999999999999999999999999999999999999999999,
        "activities": [activity],
        "status": "online",
        "afk": False
    }
}


print(ws.send(json.dumps(payload)))
