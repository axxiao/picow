import time
import machine
from oled import setup_oled, show_text
from wifi import connect_wifi


led = machine.Pin("LED", machine.Pin.OUT) 


def main():
     # Init
    oled = setup_oled()
    led.off()
    led.on()
    ip = connect_wifi(led)
    last_dig = ip.split('.')[-1]
    show_text(f"IP.{last_dig}")

 
if __name__ == "__main__":
     main()

