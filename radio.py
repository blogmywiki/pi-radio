#!/usr/bin/env python
# Bare bones simple internet radio
# www.suppertime.co.uk/blogmywiki

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

# sets initial station number to channel 8
station = 8

os.system("mpc play " + str(station))

#initialise previous input variable to 0
prev_input = 0
while True:
  #take a reading from pin 23
  input = GPIO.input(23)
  #if the last reading was low and this one high, do stuff
  if ((not prev_input) and input):
    # assumes you have 8 radio stations configured
    station += 1
    if station > 8:
       station = 1
    os.system("mpc play " + str(station))

  #update previous input
  prev_input = input

  #slight pause to debounce
  time.sleep(0.05)
