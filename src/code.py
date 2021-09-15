import board
import busio
import adafruit_ssd1306
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_jp import KeyboardLayoutJP
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import board
import digitalio
import config

# Circuit Configlation
PIN_SHIFT = board.GP13
PIN_BUTTON1 = board.GP10
PIN_BUTTON2 = board.GP7
PIN_BUTTON3 = board.GP4
PIN_BUZZER = board.GP16
PIN_SCK_DISPLAY = board.GP21
PIN_SDA_DISPLAY = board.GP20
DISPLAY_WIDTH = 32
DISPLAY_HEIGHT = 128

# ready keyboard
keyboard = Keyboard(usb_hid.devices)
layout = None

# ready buttons
btn_shift = digitalio.DigitalInOut(PIN_SHIFT)
btn_shift.direction = digitalio.Direction.INPUT
btn_shift.pull = digitalio.Pull.DOWN

btn1 = digitalio.DigitalInOut(PIN_BUTTON1)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(PIN_BUTTON2)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(PIN_BUTTON3)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

# ready buzz
buzzio = digitalio.DigitalInOut(PIN_BUZZER)
buzzio.direction = digitalio.Direction.OUTPUT

# ready display
i2c = busio.I2C(PIN_SCK_DISPLAY, PIN_SDA_DISPLAY)
display = adafruit_ssd1306.SSD1306_I2C(DISPLAY_HEIGHT, DISPLAY_WIDTH, i2c)

def buzz(times):
    global buzz
    if not config.buzzer:
        return
    for i in range(times):
        buzzio.value = 1
        time.sleep(0.001)
        buzzio.value = 0
        time.sleep(0.1)

def textShow(text1,text2,text3):
    display.fill(0)
    display.text(text1, 0,0, 1)
    display.text(text2, 0,10, 1)
    display.text(text3, 0,20, 1)
    display.show()

def isPressed(currentVal, preVal):
    if preVal == 0 and currentVal == 1:
        return True
    else:
        return False

def lockLoop():
    if config.uselock == False or len(config.lockpin) == 0:
      setLayout()
      return

    pin = []
    passText(len(pin), "*")
    buzz(1)
    time.sleep(0.1)
    preBtnValS = btn_shift.value
    preBtnVal1 = btn1.value
    preBtnVal2 = btn2.value
    preBtnVal3 = btn3.value

    while True:
        stateS = isPressed(btn_shift.value, preBtnValS)
        state1 = isPressed(btn1.value, preBtnVal1)
        state2 = isPressed(btn2.value, preBtnVal2)
        state3 = isPressed(btn3.value, preBtnVal3)
        
        preBtnValS = btn_shift.value
        preBtnVal1 = btn1.value
        preBtnVal2 = btn2.value
        preBtnVal3 = btn3.value

        if stateS:
            buzz(1)
            if checkPin(pin):
              setLayout()
              return
            pin = []
            passText(len(pin), "*")
        elif state1 and state2:
            pass
        elif state1 and state3:
            pass
        elif state2 and state3:
            pass
        elif state1:
            pin.append(1)
            passText(len(pin), "*")
        elif state2:
            pin.append(2)
            passText(len(pin), "*")
        elif state3:
            pin.append(3)
            passText(len(pin), "*")
        else:
            pass

        time.sleep(0.05)  

def passText(times, subtext):
    ts = ""
    for i in range(times):
        ts = ts + subtext
    textShow("Locked.","Enter Pin and Shift.", ">> " + ts)

def checkPin(pin):
    if len(pin) != len(config.lockpin):
      return False
    for i in range(len(config.lockpin)): 
      if pin[i] != config.lockpin[i]:
        return False
    return True

def setLayout():
    global layout
    if config.layoutType == "jp":
      layout = KeyboardLayoutJP(keyboard)
    else:
      layout = KeyboardLayoutUS(keyboard)
    textShow("You got it.","Welcome to customkey","           ( ^_^)b")
    buzz(2)
    time.sleep(3)

def next(current):
    for i in range(len(config.keymap)):
        if i <= current:
            continue
        if config.keymap[i]["enabled"] == True:
            return i
    for i in range(len(config.keymap)):
        if config.keymap[i]["enabled"] == True:
            return i
    return current

def getKeyCodes(idx, btnIdx):
    return config.keymap[idx]["data"][btnIdx]["value"]
        
def keysend(strVal):
    global layout
    layout.write(strVal)
    time.sleep(0.1)

def titleShow(sidx):
    sidxStr = str(sidx)
    textShow(sidxStr + "1. " + config.keymap[sidx]["data"][0]["label"]
            ,sidxStr + "2. " + config.keymap[sidx]["data"][1]["label"]
            ,sidxStr + "3. " + config.keymap[sidx]["data"][2]["label"])

def mainLoop():
    lockLoop()
    sidx = 0
    titleShow(sidx)
    
    preBtnValS = btn_shift.value
    preBtnVal1 = btn1.value
    preBtnVal2 = btn2.value
    preBtnVal3 = btn3.value
    
    while True:
        stateS = isPressed(btn_shift.value, preBtnValS)
        state1 = isPressed(btn1.value, preBtnVal1)
        state2 = isPressed(btn2.value, preBtnVal2)
        state3 = isPressed(btn3.value, preBtnVal3)
        
        preBtnValS = btn_shift.value
        preBtnVal1 = btn1.value
        preBtnVal2 = btn2.value
        preBtnVal3 = btn3.value

        if stateS:
          sidx = next(sidx)
          titleShow(sidx)
        elif state1:
          if btn_shift.value == 1:
            lockLoop()
            sidx = 0
            titleShow(sidx)
            continue
          else:
            keysend(getKeyCodes(sidx, 0))
        elif state2:
          keysend(getKeyCodes(sidx, 1))
        elif state3:
          keysend(getKeyCodes(sidx, 2))
        
        time.sleep(0.05)

mainLoop()



