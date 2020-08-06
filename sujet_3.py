							
Plateau= [ [True , False , False , False ] ,
                 [ False , True , True , False ] ]

l=[]

def chemin(Plateau):
	x = Plateau[1][3]
	y = Plateau[0][1]
	l.append(x)
	l.append(y)
	print(x)
	print(l)
	if True in l:
	    print(True)
	else:
	    print(False)

	
chemin(Plateau)
