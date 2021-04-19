f=open('b.txt',"r")
while True :
	line=f.readline()
	if len(line) < 60 :
		pass
	else :
		line = line.split()
		try :
			line = int(str("".join(line[10:])))
			if line < 1000 :
				print("bala")
		except :
			pass
