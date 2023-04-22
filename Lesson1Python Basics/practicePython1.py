class Classy(object):
    classCount = 0
    def __init__(self):
        self.items = []
        
    def addItem (self,itemName):
        if self.items is None:
            self.items = []
        self.items.append(itemName)
        
    def getClassiness (self):
        for i in range(len(self.items)):
            if self.items[i] == "tophat":
                Classy.classCount = Classy.classCount + 2
            elif self.items[i] == "bowtie":
                Classy.classCount = Classy.classCount + 4
            elif self.items[i] == "monocle":
                Classy.classCount = Classy.classCount + 5
        classiness = Classy.classCount 
        Classy.classCount  = 0
        return classiness
        
# Test cases
me = Classy()

# Should be 0
print (me.getClassiness())

me.addItem("tophat")
# Should be 2
print (me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print (me.getClassiness())

me.addItem("bowtie")
# Should be 15
print (me.getClassiness())