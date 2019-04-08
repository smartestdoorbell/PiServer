import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
ControlPin = [7,11,13,15]

directionalCounter = 0

def moveCam(dir, count)
  for pin in ControlPin:
          GPIO.setup(pin, GPIO.OUT)
          GPIO.output(pin, 0)

  seq = [[1,0,0,0], [1,1,0,0,], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1],[1,0,0,1]]

  if dir == 'l':
    hsstart = 0
    hsrng = 8
    pinstart=0
    pinrng = 4
    direction = 1
  elif dir = 'r':
    hsstart = 7
    hsrng = -1
    pinstart=3
    pinrng = -1
    direction = -1


  for i in range(40):
          for halfstep in range(hsstart, hsrng, direction):
                  for pin in range(pinstart, pinrng, direction):
                          GPIO.output(ControlPin[pin], seq[halfstep][pin])
                  time.sleep(0.001)
  GPIO.cleanup()


moveCam('l', count)
moveCam('r', count)
moveCam('l', count)
moveCam('r', count)
