from time import sleep
from machine import Pin

def blink(led, sequenceRepeat, sequence, sequenceSleep, sleepOne, sleepTwo):
  if isinstance(led, Pin):
    for i in range(0, sequenceRepeat):
      for y in range(sequence):
        led.value(1)
        sleep(sleepOne)
        led.value(0)
        sleep(sleepTwo)
      sleep(sequenceSleep)

  return