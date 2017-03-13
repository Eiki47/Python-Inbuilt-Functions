#skilar rétt ef strengurinn inniheldur aðeins tölur
x = "foobar"
y = "f00b4r"
z = "84"
a = "0.84"

print (x.isdecimal()) #skilar False
print (y.isdecimal()) #skilar False
print (z.isdecimal()) #skilar True
print (a.isdecimal()) #skilar False