import serial
from time import sleep


class MainBoardMovement:
    def __init__(self):     # Initiate connection
        self.ser = serial.Serial("dev/ttyUSB0", timeout=0.03, baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        self.wheels = [0, 0, 0]

    def update_wheel_speed(self, w1, w2, w3):   # Also serves to store wheel speeds if further use needed.
        self.wheels = [w1, w2, w3]

    def wheel_speed_zero(self):     # NOTE: does not stop, use ser_write_wheel afterwards.
        self.wheels = [0, 0, 0]

    def ser_stop(self):     # Use to stop Serial connection. Don't forget to end your script with this.
        self.ser.close()

    def ser_write_wheel(self):      # Sends text file to Serial. Can comment out verbose.
        sot = ("sd:{0}:{1}:{2}\n".format(str(self.wheels[0]), str(self.wheels[1]), str(self.wheels[2])))
        self.ser.write(sot.encode('utf-8'))
        print("Output text ---> ")
        print(sot)

    def sleep(self, t):     # Will need to change this once we start threading.
        sleep(t)

    # Movement functions
    def move_forward(self, t):
        self.update_wheel_speed(10, -10, 0)
        self.ser_write_wheel()
        self.sleep(t)
        self.wheel_speed_zero()
        self.ser_write_wheel()

    def move_backward(self, t):
        self.update_wheel_speed(-10, 10, 0)
        self.ser_write_wheel()
        self.sleep(t)
        self.wheel_speed_zero()
        self.ser_write_wheel()

    def rotate_left(self, t):
        self.update_wheel_speed(10, 10, 10)
        self.ser_write_wheel()
        self.sleep(t)
        self.wheel_speed_zero()
        self.ser_write_wheel()

    def rotate_right(self, t):
        self.update_wheel_speed(-10, -10, -10)
        self.ser_write_wheel()
        self.sleep(t)
        self.wheel_speed_zero()
        self.ser_write_wheel()

    # Stride left/right might also be needed.


# Debugging Section.
LeBot = MainBoardMovement()

# Manual movement
LeBot.update_wheel_speed(20, -20, 0)
LeBot.ser_write_wheel()
LeBot.sleep(0.3)
LeBot.wheel_speed_zero()
LeBot.ser_write_wheel()

# Semi automatic movement
LeBot.move_forward(1)
LeBot.move_backward(1)
LeBot.rotate_right(1)
LeBot.rotate_left(1)

LeBot.ser_stop()
