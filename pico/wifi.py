import network
import time
import json
from tools import out

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def connect_wifi(led):
    with open('./wifi.json', 'r') as f:
        config = json.load(f)
    ssid = config['ssid']
    out(f'Connecting [{ssid}]...')
    wlan.connect(ssid, config['pwd'])
    cnt = 0
    while not wlan.isconnected() and wlan.status() >= 0:
        out(f"Waiting [{cnt}]")
        led.off()
        time.sleep(1)
        cnt += 1
        led.on()
    out(f'Connected Wifi [{ssid}]')
    led.on()
    ip = wlan.ifconfig()[0]
    return ip
