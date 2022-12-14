from machine import Pin, I2C
import framebuf
from ssd1306 import SSD1306_I2C

WIDTH = 128 # oled display width
HEIGHT = 32 # oled display height
oled = None

def setup_oled(scl=9,sda=8,freq=400000):
    i2c = I2C(0,scl=Pin(scl), sda=Pin(sda),freq=freq)
    print(i2c.scan())
    print("I2C Address : "+hex(i2c.scan()[0]).upper()) # Display device address
    print("I2C Configuration: "+str(i2c))
    global oled
    oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) # Init oled display
    # Raspberry Pi logo as 32x32 bytearray
    buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

    # Load the raspberry pi logo into the framebuffer (the image is 32x32)
    fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)
    # Clear the oled display in case it has junk on it.
    oled.fill(0)

    # Blit the image from the framebuffer to the oled display
    oled.blit(fb, 96, 0)

    # Add some text
    oled.text("Init ...",5,5)

    # Finally update the oled display so the image & text is displayed
    oled.show()
    return oled

def show_text(text, start_w=0, start_h=0, clean=True):
    if clean:
        oled.fill(0)
    oled.text(text, start_w, start_h)
    oled.show()
    

