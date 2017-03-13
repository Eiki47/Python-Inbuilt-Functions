# mjög svipað og isdigit og isdecimal nema þetta fer aðeins dýpra niður í unicode
x = "84\u00BD" #hálft veldi
print (x.isnumeric()) #skilar True