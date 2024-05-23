
from color import *



BLINK_DEFAULT_DURATION = 4.0

POD_TYPE_FLOWER = 1
POD_TYPE_POD = 2


class Pod:
  def __init__(self, name:str, color: Color, type:int, ledIDs:list[int]):
    self.name = name
    self.type = type
    self.color = FadingColor(color)
    self.ledIDs = ledIDs
    
  def setOff(self):
    self.color.setOff()

  def setOn(self):
    self.color.setOn()

  def blink(self, fadeInDuration:float = BLINK_DEFAULT_DURATION, onDuration:float = BLINK_DEFAULT_DURATION, fadeOutDuration:float = BLINK_DEFAULT_DURATION, startDelay = 0.0):
    self.color.fadeInOut(fadeInDuration, onDuration, fadeOutDuration, startDelay)




def toPodType(type:str):
  if type == "pod":
    return POD_TYPE_POD
  elif type == "flower":
    return POD_TYPE_FLOWER
  else:
    print("toPodType(type:str)  failed. passed " + type)
    return 0

def loadPods(loadPath):
  strands = [{} for i in range(4)]
  f = open(loadPath)
  j_data = json.load(f)
  for comp in j_data['InstallationComponents']:
    ind = comp["groupID"]
    strands[ind] = [i for i in range(len(comp["fixtures"]))]
    for pod in comp["fixtures"]:
      strands[ind][pod["fixtureID"]] = Pod(pod["fixtureName"], Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), toPodType(pod["fixtureType"]), pod["LEDs"])
    # leds[led["LEDGroupID"]] = LED(led["LedIDs"][0], typeToSize(led["type"]), led["universe"], led["controllerID"])
  f.close()
  return strands
