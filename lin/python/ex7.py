from sys import argv
script,textfile=argv
#textfile=raw_input("the path of file")
#text=open(textfile)
#print "The content of %s:"%textfile
#print text.read()
text=open(textfile,'a+')
line1="I have some food."
line2="But I am not hungry."
line3="How odd!"
line5="unknown to life,and unkown to death "
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")



text.write("\n")
text.write(line5)
text.close()
