import termcolor
import time
import sys

def write(text, end = "\n", color = None, delay = .02):
  for char in text:
    if color != None:
      sys.stdout.write(termcolor.colored(char, color))
      sys.stdout.flush()
      time.sleep(delay)

    else:
      sys.stdout.write(termcolor.colored(char, color))
      sys.stdout.flush()
      time.sleep(delay)

  sys.stdout.write(end)
  sys.stdout.flush()

def verify_input(allowed, errorMSG = "input error"):
  while True:
    write(">", "","yellow")
    chc = input()
    if chc not in allowed:
      write(errorMSG, "\r", "red")
      time.sleep(.5)
      write(" " * (len(errorMSG) + 3), "\r")
    
    else:
      return chc