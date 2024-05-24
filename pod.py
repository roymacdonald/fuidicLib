
from color import *

import json
import random

BLINK_DEFAULT_ON_DURATION = 4.0
BLINK_DEFAULT_FADE_DURATION = 2.0

POD_TYPE_FLOWER = 1
POD_TYPE_POD = 2


class Pod:
  def __init__(self, name:str, color: Color, podType:int, ledIDs:list):
    self.name = name
    self.podType = podType
    self.color = FadingColor(color)
    self.ledIDs = ledIDs
    
  def setOff(self):
    self.color.setOff()

  def setOn(self):
    self.color.setOn()

  def blink(self, fadeInDuration:float = BLINK_DEFAULT_FADE_DURATION, onDuration:float = BLINK_DEFAULT_ON_DURATION, fadeOutDuration:float = BLINK_DEFAULT_FADE_DURATION, startDelay = 0.0, onEndCallback = None):
    self.color.fadeInOut(fadeInDuration, onDuration, fadeOutDuration, startDelay, onEndCallback)

  def setOnWhite(self):
    self.color.setOnWhite()


def toPodType(podType:str):
  if podType == "pod":
    return POD_TYPE_POD
  elif podType == "flower":
    return POD_TYPE_FLOWER
  else:
    print("toPodType(type:str)  failed. passed " + podType)
    return 0

def loadPods(loadPath):
  strands = [{} for i in range(4)]
  f = open(loadPath)
  j_data = json.load(f)
  for comp in j_data['InstallationComponents']:
    ind = comp["groupID"]
    strands[ind] = [i for i in range(len(comp["fixtures"]))]
    i = 0
    for pod in comp["fixtures"]:
      # Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
      c = i%3
      i+=1
      strands[ind][pod["fixtureID"]] = Pod(pod["fixtureName"], Color(255 if c == 0 else 0, 255 if c == 1 else 0, 255 if c == 2 else 0), toPodType(pod["fixtureType"]), pod["LEDs"])
    # leds[led["LEDGroupID"]] = LED(led["LedIDs"][0], typeToSize(led["type"]), led["universe"], led["controllerID"])
  f.close()
  return strands
