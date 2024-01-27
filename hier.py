class Mtca:
    chairman='Mr.sunil'
    location='palamaner'
    college='MTCA'
     
    def __init__(self,name,mobile):
         self.name=name
         self.mobile=mobile

class Mca(Mtca):
      principal='Mr.Prabhakar naidu'
      strength=240
      staff=9
class Btech(Mtca):
    principal='Ms.Sravani'
    strength=350
    staff=35

Navitha=Mca('Navitha',2365478965)
Rajashekar=Btech('Rajashekar',4561237895)
    