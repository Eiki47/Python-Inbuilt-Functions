#svipað og .find() en skilar villu ef ekkert er fundið
x = "foobar"
print (x.index("o")) #skilar "1"
print (x.index("oba")) #skilar "2"
print (x.index("lol")) #skilar valueError