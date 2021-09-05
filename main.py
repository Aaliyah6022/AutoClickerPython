import ctypes
import random
from pypresence import Presence
import time
from time import sleep
from random import seed
from random import randint

seed(1)

# RPC = Presence("client_id")                                  add your own discord rich presence client id if you wanna have a cool status on discord!
# RPC.connect()

quotes = [
    "I code games, bots, software",
    "I know Python, C , C++, C#, ASM",
    "Dm me if you want help coding",
    "I play METIN2!"
]

SendInput = ctypes.windll.user32.SendInput


# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(1)
    print("Bot started!")


def main():
    # clicker?
    countdownTimer()

for _ in range(10):
    value =randint(0,10)


while(True):

    # RPC.update(details="Hello, i'm big hacker!", state=random.choice(quotes),
    #            buttons=[{"label": "Website", "url": "https://qtqt.cf"},                                                  if you wanna add Discord rich presence just unmark it
    #                     {"label": "Server", "url": "https://discord.gg/xxxx"}], large_image="big-image",
    #            large_text="Large Text Here!", small_image="small-image", small_text="Small Text Here!")
    PressKey(59)  # Press F1, F2, F3
    time.sleep(value)
    ReleaseKey(59)
    PressKey(60)
    time.sleep(value)
    ReleaseKey(60)
    PressKey(61)
    time.sleep(value)
    ReleaseKey(61)








