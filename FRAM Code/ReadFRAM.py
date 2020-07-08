import board
import busio
import adafruit_fram
import RPi.GPIO as GPIO
import time,datetime
from contextlib import contextmanager
import signal

#initial
GPIO.setmode(GPIO.BCM)
branch_pins = [17,22,27]
for pin in branch_pins:
    GPIO.setup(pin,GPIO.OUT)


# try changing these to BCM
i2c = busio.I2C(board.SCL, board.SDA)
fram = adafruit_fram.FRAM_I2C(i2c)


def _Enable_Bus_Branch(list_of_branches,branch_num):
    """ Enable the specified branch number and disable other
    branches as only one should be active at a time

    :param list_of_branches: (list(ints)) list of branch BCM pins
    :param branch_num: (int) branch to be enabled
    :Return: none
    """

    # disable all branches
    pin_to_disable = []
    for pin in range(len(list_of_branches)):
        pin_to_disable.append(pin)
    _Disable_Bus_Branch(list_of_branches, pin_to_disable)
    # enable the target branch
    GPIO.output(list_of_branches[branch_num],True)
    print("Pin ",list_of_branches[branch_num], " is active")       
    

def _Disable_Bus_Branch(list_of_branches,branch_num):
    """ Disable the specified branch number

    :param list_of_branches: (list(ints)) list of branch BCM pins
    :param branch_num: (int)/(list(int)) branch to be disabled
    :Return: none

    """

    # if a list is sent, turn all in the list off
    if type(branch_num) == list:
        for branch in branch_num:
            GPIO.output(list_of_branches[branch], False)
    # otherwise only turn the singular pin off
    else:
        GPIO.output(list_of_branches[branch_num], False)       

@contextmanager
def _time_limit(time_length):
    def signal_handler(signum, frame):
        raise TimeoutError("timed out!")
    signal.signal(signal.SIGALRM,signal_handler)
    signal.alarm(time_length)
    try:
        yield
    finally:
        signal.alarm(0)



def Scan_for_Devices(list_of_branches,branch_num):
    devices = []
    # _Enable_Bus_Branch(list_of_branches,branch_num)
    try:
        with _time_limit(3):
            devices = i2c.scan()
    except TimeoutError as e:
        print(e)

    return devices

def Write_to_FRAM(message):
    fram[0] = bytearray(message,encoding="UTF-8")

def Read_from_FRAM(start_byte, bytes_to_read):
    read_message = ""
    for byte in range(start_byte,bytes_to_read):
        read_message += str(fram[byte], "UTF-8")
    return read_message



print(Read_from_FRAM(0,10))


