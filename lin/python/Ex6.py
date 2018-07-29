pi=3.14     #pi,3.14159...
#r=6378000   #radius
r=float(raw_input("please input radius of the earth?"))
c=2*pi*r    #console
s=4*pi*r*r    #surface area
print"\tthe console: %s m\n\tsurface aera= %d m2"%(c,s)
