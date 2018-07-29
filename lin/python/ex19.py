class food(object):
   # def implicit(self):
#	print"animal implicit()"
    def override(self):
	print"food override()"
class fruit(food):
  #  pass
    def override(self):
	print"fruit override()"
class meat(food):
    def override(self):
	print "meat override()"
####class vegetable(food):
   #### def altered(self):
####	super(vegetable,self).altered()
###tomato=vegetable()
#####vegetable.altered()
class ph(meat,fruit):
    pass
apple=fruit()
beaf=food()
#apple.implicit()
#meat.implicit()
apple.override()
beaf.override()


