def print_none():
    print"hello world"
def print_one(argv):
    print"I like %s."%argv
def print_two(argv1,argv2):
    print "I like %s and %s."%(argv1,argv2)
print_none()
print_one("apple")
print_two("apple","banana")
