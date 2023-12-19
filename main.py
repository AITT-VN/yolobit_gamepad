from _thread import start_new_thread
from ble import *
from yolobit import *
import time
from gamepad import *

scanning = False

def blink_led_matrix():
  global scanning
  while scanning:
    display.set_all('#00ff00')
    time.sleep(0.5)
    display.set_all('#ff0000')
    time.sleep(0.5)

def on_ble_connected_callback():
  display.set_all('#00ff00')

ble.on_connected(on_ble_connected_callback)

def on_ble_disconnected_callback():
  display.set_all('#ff0000')

ble.on_disconnected(on_ble_disconnected_callback)

display.set_brightness(20)
display.set_all('#ff0000')
scanning = True
start_new_thread(blink_led_matrix, ())
ble.connect_nearby()
scanning = False
time.sleep_ms(200)

while True:
  if button_a.is_pressed():
    if not ble.is_connected():
      display.set_all('#ff0000')
      scanning = True
      start_new_thread(blink_led_matrix, ())
      ble.connect_nearby()
      scanning = False
      time.sleep_ms(500)
  
  if button_b.is_pressed():
    if ble.is_connected():
      ble.disconnect()
      time.sleep_ms(500)
  
  # read gamepad joystick to detect direction
  # we use only 4 directions to be simple
      
  angle = gamepad.read_joystick()[2]

  # calculate direction based on angle

  #         90(2)
  #   135    |    45
  # 180(3)---+----Angle=0 (dir=1)
  #   225    |    315
  #         270(4)

  dir = 0
  if 0 <= angle < 40 or angle >= 320:
    dir = 1
  elif 50 <= angle < 130:
    dir = 2
  elif 140 <= angle < 220:
    dir = 3
  elif 230 <= angle < 310:
    dir = 4
  
  # button status order: Joystick - C (down) - D (right) - E (up) - F (left)
  
  if gamepad.read_buttons()[1]:
    ble.send(('!B318'))
    display.scroll('C')
  elif gamepad.read_buttons()[3]:
    ble.send(('!B219'))
    display.scroll('B')
  elif gamepad.read_buttons()[4]:
    ble.send(('!B11:'))
    display.scroll('A')
  elif gamepad.read_buttons()[2]:
    ble.send(('!B417'))
    display.scroll('D')
  elif dir == 2: # Forward
    ble.send(('!B516'))
    display.show(Image("00100:01110:10101:00100:00100"))
  elif dir == 4: # Backward
    ble.send(('!B615'))
    display.show(Image("00100:00100:10101:01110:00100"))
  elif dir == 1: # Turn right
    ble.send(('!B814'))
    display.show(Image("00100:00010:11111:00010:00100"))
  elif dir == 3: # Turn left
    ble.send(('!B714'))
    display.show(Image("00100:01000:11111:01000:00100"))
  else:
    ble.send(('S'))
    if ble.is_connected():
      display.set_all('#00ff00')
    else:
      display.set_all('#ff0000')

  time.sleep_ms(100)
