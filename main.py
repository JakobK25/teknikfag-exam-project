import pygame
import random
import time
import pyfirmata 

# Set up the Arduino board
board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()

# Set up the pins
led_pin = board.get_pin()
potentiometer_pin = board.get_pin()

