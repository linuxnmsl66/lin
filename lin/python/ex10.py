def cha(s1,s2):
    return s1-s2
def cir(r):
   	pi=3.14159
	l=2*pi*r
	return l
earth=cir(6783)
mars=cir(3396)
cha1=cha(earth,mars)
print"earth:%d. km"%earth, "\n mars:%d. km"%mars, "\n cha=%d. km"%cha1
