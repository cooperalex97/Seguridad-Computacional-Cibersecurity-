def aqui(archivo):
	f = open(archivo+".txt",encoding="utf8")
	g = open("HERALDOSNEGROS_pre9.txt","w")
	cont=0
	contotal=0
	for linea in f:
		for j in linea:
			cont=cont+1
			contotal=contotal+1
			if(cont==21):
				cont=1
				contotal=contotal+4
				g.write("AQUI")
				g.write(j)
			else:
				g.write(j)
	contotal=contotal%4
	if(contotal!=0):
		g.write("X"*contotal)
	g.close()
	f.close()

aqui("HERALDOSNEGROS_pre")
