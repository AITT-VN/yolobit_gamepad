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
    ble.send_value('R', (gamepad.read_joystick()[3]))
  elif gamepad.check_dir(2):
    say('FR')
    ble.send_value('FR', (gamepad.read_joystick()[3]))
  elif gamepad.check_dir(3):
    say('F')
    ble.send_value('F', (gamepad.read_joystick()[3]))
  elif gamepad.check_dir(4):
    say('FL')
    ble.send_value('FL', (gamepad.read_joystick()[3]))
  elif gamepad.check_dir(5):
    say('L')
    ble.send_value('L', (gamepad.read_joystick()[3]))
  elif gamepad.check_dir(6):
    say('BL')
    ble.send_value('BL', (gamepad.read_joystick()[3]))
  elif gamepad.check_dir(7):
    say('B')
    ble.send_value('B', (gamepad.read_joystick()[3]))
  elif gamepad.check_dir(8):
    say('BR')
    ble.send_value('BR', (gamepad.read_joystick()[3]))
  else:
    ble.send_value('S', 0)
  if gamepad.read_buttons()[1]:
    ble.send_value('S1', 0)
  elif gamepad.read_buttons()[3]:
    ble.send_value('S1', 90)
  elif gamepad.read_buttons()[4]:
    ble.send_value('S2', 0)
  elif gamepad.read_buttons()[2]:
    ble.send_value('S2', 90)
  time.sleep_ms(50)
