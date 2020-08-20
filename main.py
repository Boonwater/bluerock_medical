import random

import ui

def main():
  ui.write(".bluerock medical.", "\n", "red")
  ui.write("1 - generate random pawn", "\n", "green")
  ui.write("2 - generate random pawn (injured)", "\n", "green")
  ui.write("3 - generate two pawns and battle", "\n", "green")
  ui.write("4 - exit", "\n", "red")

  chc = ui.verify_input(["1", "2", "3", "4"])

  if chc == "1":
    test = Pawn()
    test.quickDamage()
    test.bodyCheck()
  
  elif chc == "2":
    ui.write("placeholder")
  
  elif chc == "3":
    ui.write("placeholder")

  elif chc == "4":
    return

class Pawn:
  def __init__(self, name = "guy mcgee"): 
    self.brainFunction = 100

    self.bloodVolume = 5000
    self.bloodFiltration = 100
    self.systolic = 80 + random.randint(-10, 10)
    self.diastolic = 120 + random.randint(-10, 10)
    self.currentBleedFactor = 0

    self.movement = 100
    self.manipulation = 100
    self.walking = 100
    self.pain = 0

    self.breathing = 100
    self.metabolism = 100

    self.body = []

    self.head = [Part("skull", 1000, True, False, "N/A"), Part("brain", 2500, False, True, "skull", "brainFunction", 100), Part("neck", 2500, False, True, "N/A", "breathing", 100)]
    self.spine = [Part("upper spine", 1000, True, True, "neck", "movement", 100), Part("lower spine", 1000, True, True, "upper spine", "walking", 100)]
    
    self.upperTorso = [Part("ribcage", 500, True, True, "upper spine", "breathing", 50), Part("heart", 5000, False, True, "N/A", "diastolic", 100),
    Part("left lung", 500, False, True, "neck", "breathing", 50), Part("right lung", 500, False, True, "neck", "breathing", 50)]

    self.lowerTorso = [Part("hips", 1000, True, True, "lower spine", "walking", 100), Part("left kidney", 750, False, True, "N/A", "bloodFiltration", 50),
    Part("left kidney", 750, False, True, "N/A", "bloodFiltration", 50), Part("stomach", 500, False, True, "N/A", "metabolism", 100),
    Part("intestines", 1000, False, True, "stomach", "metabolism", 100), Part("kidney", 500, False, True, "N/A", "bloodFiltration", 75)]

    self.leftArm = [Part("left humerus", 500, True, True, "N/A", "manipulation", 50), Part("left radius", 250, True, True, "left humerus", "manipulation", 25),
    Part("left ulna", 250, True, True, "left humerus", "manipulation", 25), Part("left hand", 250, True, True, "left ulna", "manipulation", 50)]

    self.rightArm = [Part("right humerus", 500, True, True, "N/A", "manipulation", 50), Part("right radius", 250, True, True, "right humerus", "manipulation", 25),
    Part("right ulna", 250, True, True, "right humerus", "manipulation", 25), Part("right hand", 250, True, True, "right ulna", "manipulation", 50)]

    self.leftLeg = [Part("left femur", 1000, True, True, "hips", "walking", 75), Part("left tibula", 500, True, True, "left femur", "walking", 50),
    Part("left fibula", 500, True, True, "left femur", "walking", 50), Part("left foot", 500, True, True, "left tibula", "walking", 40)]

    self.rightLeg = [Part("right femur", 1000, True, True, "hips", "walking", 75), Part("right tibula", 500, True, True, "right femur", "walking", 50),
    Part("right fibula", 500, True, True, "right femur", "walking", 50), Part("right foot", 500, True, True, "right tibula", "walking", 40)]
  
    self.body.append(self.head)
    self.body.append(self.spine)
    self.body.append(self.upperTorso)
    self.body.append(self.lowerTorso)
    self.body.append(self.leftArm)
    self.body.append(self.rightArm)
    self.body.append(self.leftLeg)
    self.body.append(self.rightLeg)

  def quickDamage(self):
    trgtSection = random.randint(0, len(self.body) - 1)
    trgtPart = random.randint(0, len(self.body[trgtSection]) - 1)

    self.body[trgtSection][trgtPart].hp -= random.randint(15, self.body[trgtSection][trgtPart].maxHP)

  def bodyCheck(self):

    for section in self.body:
      for part in section:
        ui.write("checking {}".format(part.name))
        tempcheck = (part.bleedFactor * (1 - (part.hp / part.maxHP)))
        
        if tempcheck > 0:
          ui.write("bleeding increased to {}".format(tempcheck), "\n", "red")
          self.currentBleedFactor += tempcheck

        if part.bone is True:
          if part.fractured is False and part.broken is False:
            if 1 - (part.hp / part.maxHP) < .8 and 1 - (part.hp / part.maxHP) < .6:
              part.fractured = True
              self.pain += 10

            elif 1 - (part.hp / part.maxHP) < .6:
              part.broken = True
              self.pain += 15

        if part.effect is True:
          effectConversions = {"brainFunction" : self.brainFunction, "bloodFiltration" : self.bloodFiltration, "diastolic" : self.diastolic, "movement" : self.movement,
          "manipulation" : self.manipulation, "walking" : self.walking, "breathing" : self.breathing, "metabolism" : self.metabolism}

          ui.write("{} : {}%".format(part.effectType, effectConversions[part.effectType]))
          effectConversions[part.effectType] *= (1 - (part.importance * (1 - (part.hp / part.maxHP))))
          ui.write("{} : {}%".format(part.effectType, effectConversions[part.effectType]))



class Part:
  def __init__(self, name, bleedFactor, bone, effect, reliance = "N/A", effectType = "", importance = 0):
    self.name = name
    self.bleedFactor = bleedFactor
    self.reliance = reliance
    self.effect = False

    if bone is True:
      self.bone = True
      self.fractured = False
      self.broken = False
      self.hp = 2500
      self.damageAbsorption = 50
    
    elif bone is False:
      self.bone = False

    if effect is True:
      self.effect = True
      self.effect = effectType
      self.effectImportance = importance
      self.hp = 100
      self.damageAbsorption = 0

    if not bone and not effect:
      self.hp = 1000
      self.damageAbsorption = 15

    self.maxHP = self.hp

    

    


if __name__ == "__main__":
  main()