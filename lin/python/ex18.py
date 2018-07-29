class organism(object):
    def __init__(self):
	self.carbon=True
class animal(organism):
    def __init__(self):
    	super(animal,self).__init__()
        self.move=True
	self.meat=False
    def food(self):
	print "meat and something"
class vertebrate(animal):
    def __init__(self):
    	super(vertebrate,self).__init__()
        self.vertebrate=True
        self.meat=False
    def food(self):
        print "meat and something"

class mammal(vertebrate):
    def __init__(self):
    	super(mammal,self).__init__()
        self.viviparity=True
        self.meat=False
    def food(self):
	print "most meat"
class dog(mammal):
    def __init__(self):
    	super(dog,self).__init__()
        self.move=True
        self.meat=True
    def food(self):
        print "meat and cat"

