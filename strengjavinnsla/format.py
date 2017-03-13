#true
x = "foo{0}".format("bar")
y = "foo{0}{1}{2}".format("b",1+3,"r")

print (x) #skilar "foobar"
print (y) #skilar "foob4r"