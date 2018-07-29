from sys import argv
print "input your number:"
script,bijiao=argv
pi=3.14159
mars_r=3396
earth_r=6738
bijiao=float(bijiao)


#function
def suanzi(x):
	return 2*pi*x
	
	
mars=suanzi(mars_r)
earth=suanzi(earth_r)
if abs(bijiao-mars)<=1000:
	print "more mars"
elif abs(bijiao-earth)<=1000:
	print "more earth"
else:
	print "too far"
	#print mars,"\t",earth
