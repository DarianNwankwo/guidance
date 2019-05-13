"""
Sofya Pugach (sp2535)
Darian Nwankwo (don4)
Lab Assignment 1
February 20, 2019
"""
import RPi.GPIO as GPIO

import subprocess
import time


PATH_TO_FIFO = "/home/pi/Development/guidance/log_fifo"


GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...


def execute(action, path_to_fifo):
    """Sends the action to the fifo at <path_to_fifo>."""
    cmd = 'echo "{}" > {}'.format(action, path_to_fifo)
    subprocess.check_output(cmd, shell=True)


if __name__ == "__main__":
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    try:
        GPIO.wait_for_edge(27, GPIO.FALLING)
        execute("Arrived", PATH_TO_FIFO)
    except KeyboardInterrupt:
        GPIO.cleanup()
    GPIO.cleanup()
