import json

def printLine(l):
	l["t0"]=l["t0"].replace(" TDT","")
	for i in range(len(fields)):
		print(str(l[fields[i]]).rjust(lengths[i])+",",end='')
	
	print()

lengths=[5, 3, 3, 14, 7, 9, 12, 13, 12, 12, 12, 13, 12, 12, 12, 13, 12, 12, 13, 12, 12, 13, 12, 12, 13, 12, 12, 13,1]
fields=["year","month","day","jd","t0","deltat","x1","x2","x3","x4","y1","y2","y3","y4","d1","d2","d3","mu1","mu2","mu3","l11","l12","l13","l21","l22","l23","tanf1","tanf2"]
text=open("FiveMillenniumCanonOfSolarEclipsesExtra.json").read()
js=json.loads(text)

print('''#acknowledgement: Besselian Elements for Solar Eclipses from: "Five Millennium Canon of Solar Eclipses: -1999 to +3000", Fred Espenak and Jean Meeus, NASA/TP-2006-214141, October 2006
#year, mon, day, jd, t0, deltaT, x1, x2, x3, x4, y1, y2, y3, y4, d1, d2, d3, m1, m2, m3, l11, l12, l13, l21, l22, l23, tanf1, tanf2''')

for i in range(len(js["data"])):
	t=js["data"][i]
	printLine(t)


