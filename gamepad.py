import math
from micropython import const
from yolobit import *
from ble import *

# robot control command codes
CMD_SYS_PREFIX = const(0x11)
CMD_STOP = const(0x01)
CMD_DRIVE = const(0x10) # move by direction

class GamePad:
  def __init__(self):

    # Joystick
    self.jx_adc = pin0
    self.jy_adc = pin1
    

    self.last_dir = -1
    self.last_speed = 0

    # Buttons
    self.btn_joystick = pin2
    self.btn_left_f = pin16
    self.btn_right_d = pin14
    self.btn_up_e = pin15
    self.btn_down_c = pin13

    self.btn_joystick.set_pull('up')
    self.btn_left_f.set_pull('up')
    self.btn_right_d.set_pull('up')
    self.btn_up_e.set_pull('up')
    self.btn_down_c.set_pull('up')


  def calculate_direction(self, angle):
    # calculate direction based on angle
    #         90(3)
    #   135(4) |  45(2)
    # 180(5)---+----Angle=0(dir=1)
    #   225(6) |  315(8)
    #         270(7)
    dir = 1
    if 0 <= angle < 22.5 or angle >= 337.5:
      dir = 1
    elif 22.5 <= angle < 67.5:
      dir = 2
    elif 67.5 <= angle < 112.5:
      dir = 3
    elif 112.5 <= angle < 157.5:
      dir = 4
    elif 157.5 <= angle < 202.5:
      dir = 5
    elif 202.5<= angle < 247.5:
      dir = 6
    elif 247.5 <= angle < 292.5:
      dir = 7
    elif 292.5 <= angle < 337.5:
      dir = 8

    return dir

  def read_drive(self):
    ''' 
    Logic handling control message from robot (xBot or Yolo:Bit Robot Shield)
    if data[0] == CMD_SYS_PREFIX:
        cmd = data[1:]
        if cmd[0] == CMD_DRIVE:
            # get dir and speed
            dir = cmd[1]
            if len(cmd) > 2:
                speed = cmd[2]
                robot.move(dir, speed)
            else:
                robot.move(dir)

    '''
    changed = False

    # ready analog joysticks
    x = round(translate(self.jx_adc.read_analog(), 3600, 150, 100, -100))
    y = round(translate(self.jy_adc.read_analog(), 3600, 150, 100, -100))
    j_distance = int(math.sqrt(x*x + y*y)) # joystick drag distance (robot speed)

    angle = int((math.atan2(y, x) - math.atan2(0, 100))  * 180 / math.pi)
    if angle < 0: 
      angle += 360

    dir = self.calculate_direction(angle)

    if j_distance < 25:
        j_distance = 0
        dir = -1

    if dir != self.last_dir:
        self.last_dir = dir
        changed = True
    
    if j_distance != self.last_speed:
        self.last_speed = j_distance
        changed = True

    if changed:
        # send new command
        if ble._ble_uart.is_connected():
            if self.last_speed > 0:
                cmd = bytearray(4)
                cmd[0] = CMD_SYS_PREFIX
                cmd[1] = CMD_DRIVE
                cmd[2] = self.last_dir
                cmd[3] = self.last_speed
                ble.send(cmd)
            else:
                cmd = bytearray(2)
                cmd[0] = CMD_SYS_PREFIX
                cmd[1] = CMD_STOP
                ble.send(cmd)

  def read_joystick(self):
    x_adc = self.jx_adc.read_analog()
    if x_adc > 3450:
      x_adc = 3450
    y_adc = self.jy_adc.read_analog()
    if y_adc > 3450:
      y_adc = 3450
    
    x = round(translate(x_adc, 3450, 0, 100, -100))
    if x>-5 and x<5:
      x = 0
    y = round(translate(y_adc, 3450, 0, 100, -100))
    if y>-5 and y<5:
      y = 0
    
    j_distance = int(math.sqrt(x*x + y*y)) # joystick drag distance (robot speed)

    angle = int((math.atan2(y, x) - math.atan2(0, 100))  * 180 / math.pi)
    if angle < 0: 
      angle += 360

    if j_distance < 25:
        j_distance = 0
        angle = -1
    elif j_distance > 100:
        j_distance = 100

    return(
        x, 
        y,
        angle,
        j_distance
    )

  def read_buttons(self):
    # button status order: Joystick - C (down) - D (right) - E (up) - F (left)
    return (1-self.btn_joystick.read_digital(),
      1-self.btn_down_c.read_digital(), 
      1-self.btn_right_d.read_digital(), 
      1-self.btn_up_e.read_digital(), 
      1-self.btn_left_f.read_digital(),
      )

  def check_dir(self, direction=-1):
    angle = gamepad.read_joystick()[2]

    # calculate direction based on angle

    #         90(3)

    #   135(4) |  45(2)

    # 180(5)---+----Angle=0(dir=1)

    #   225(6) |  315(8)

    #         270(7)

    dir = 0
    if 0 <= angle < 22.5 or angle >= 337.5:
      dir = 1
    elif 22.5 <= angle < 67.5:
      dir = 2
    elif 67.5 <= angle < 112.5:
      dir = 3
    elif 112.5 <= angle < 157.5:
      dir = 4
    elif 157.5 <= angle < 202.5:
      dir = 5
    elif 202.5<= angle < 247.5:
      dir = 6
    elif 247.5 <= angle < 292.5:
      dir = 7
    elif 292.5 <= angle < 337.5:
      dir = 8
      
    if dir == direction:
      return True
    else:
      return False

gamepad = GamePad()