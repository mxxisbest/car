def on_received_number(receivedNumber):
    global a
    if receivedNumber == 1:
        a = -1
        OmniBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.RED))
        OmniBit.RGB_Program().show()
    elif receivedNumber == 2:
        OmniBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.GREEN))
        OmniBit.RGB_Program().show()
    elif receivedNumber == 3:
        OmniBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.BLUE))
        OmniBit.RGB_Program().show()
    elif receivedNumber == 4:
        a = 1
        OmniBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.YELLOW))
        OmniBit.RGB_Program().show()
    else:
        a = 0
        OmniBit.RGB_Program().clear()
        OmniBit.RGB_Program().show()
radio.on_received_number(on_received_number)

def on_received_string(receivedString):
    global saveString
    saveString = receivedString
radio.on_received_string(on_received_string)

y = 0
x = 0
flag2 = 0
flag1 = 0
saveString = ""
a = 0
OmniBit.motor_stop_all()
OmniBit.RGB_Program().clear()
OmniBit.RGB_Program().show()
basic.show_icon(IconNames.HAPPY)
radio.set_group(1)
radio.set_transmit_power(7)

def on_forever():
    global flag1, flag2, x, y
    flag1 = parse_float(saveString.char_at(1))
    flag2 = parse_float(saveString.char_at(2))
    x = parse_float(saveString.substr(4, flag1))
    y = parse_float(saveString.substr(4 + flag1, flag2))
    OmniBit.handle(x, y, a)
basic.forever(on_forever)
