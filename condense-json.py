import json

def printRec(r):
    r["t0"]=r["t0"].replace(" TDT","")
    print("{",end="")
    for i in range(len(fields)):

        f=fields[i]
        l=lengths[i]
        print(f"\"{f}\":{str(r[f]).rjust(l)}", end="")
        if(not f=="tanf2"):
            print(", ",end="")
    print("},")

j=json.load(open("FiveMillenniumCanonOfSolarEclipsesExtra.json"))


#{"year":     1, "month":  6, "day": 10, "jd": 1721583.780743, "t0":    7.0, "deltaT":  10519.6, "x1":    0.1477500, "x2":    0.5736369, "x3":   5.800e-06, "x4":  -9.270e-06, "y1":    0.3635400, "y2":    0.0040918, "y3":  -1.800e-04, "y4":   3.000e-08, "d1":   22.9475498, "d2":    0.0041820, "d3":  -5.000e-06, "m1":  286.5210266, "m2":   14.9997044, "m3":   0.000e-00, "l11":    0.5344440, "l12":   -0.0000878, "l13":  -1.230e-05, "l21":   -0.0116350, "l22":   -0.0000873, "l23":  -1.230e-05, "tanf1":    0.0045954, "tanf2":    0.0045725},
fields=["year","month","day","jd","t0","deltat","x1","x2","x3","x4","y1","y2","y3","y4","d1","d2","d3","mu1","mu2","mu3","l11","l12","l13","l21","l22","l23","tanf1","tanf2"]
lengths=[6, 3, 3, 15, 7, 9, 13, 13, 12, 12, 13, 13, 12, 12, 13, 13, 12, 13, 13, 12, 13, 13, 12, 13, 13, 12, 13, 13,1]

print("""{
"acknowledgement": "Permission is freely granted to reproduce this data when accompanied by an acknowledgment: 'Eclipse Predictions by Fred Espenak, NASA's GSFC' For more information, see: https://eclipse.gsfc.nasa.gov/SEpubs/copyright.html",
"data":
[""")

for i in range(len(j["data"])):
    printRec(j["data"][i])

print("]")
print("}")
