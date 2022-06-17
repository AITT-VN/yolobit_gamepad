from ble import *
from yolobit import *
import time
from gamepad import *

def on_ble_connected_callback():
  display.show(Image.YES)

ble.on_connected(on_ble_connected_callback)

def on_ble_disconnected_callback():
  display.show(Image.NO)
  display.clear()

ble.on_disconnected(on_ble_disconnected_callback)

if True:
  display.clear()
  display.show(Image.HEART)
  ble.connect_nearby()
  time.sleep_ms(200)

while True:
  if button_a.is_pressed():
    display.show(Image.HEART)
    ble.connect_nearby()
    time.sleep_ms(200)
  if button_b.is_pressed():
    ble.disconnect()
    time.sleep_ms(200)
  if gamepad.check_dir(1):
    say('R')
    ble.send_value('R', ((gamepad.read_joystick()[3]) / 2))
  elif gamepad.check_dir(3):
    say('F')
    ble.send_value('F', (gamepad.read_joystick()[3]))
  elif gamepad.check_dir(5):
    say('L')
    ble.send_value('L', ((gamepad.read_joystick()[3]) / 2))
  elif gamepad.check_dir(7):
    say('B')
    ble.send_value('B', (gamepad.read_joystick()[3]))
  else:
    ble.send_value('S', 0)
  if gamepad.read_buttons()[1]:
    ble.send_value('S1', 0)
  elif gamepad.read_buttons()[3]:
    ble.send_value('S1', 90)
  time.sleep_ms(50)
