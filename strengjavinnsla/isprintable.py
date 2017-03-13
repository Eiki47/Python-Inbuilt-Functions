#skilar True ef strengurinn inniheldur aðeins prentanlega bókstafi
x = "foobar"
y = ""
z = "foo\nbar" #\n er skilgreint sem ný lína
print (x.isprintable()) #skilar True
print (y.isprintable()) #skilar True
print (z.isprintable()) #skilar False