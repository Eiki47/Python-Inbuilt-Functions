#svipað og .index() nema leitar frá hægri
#svipað og .find() en skilar villu ef ekkert er fundið
x = "foobar"
print (x.rindex("o")) #skilar "2"
print (x.rindex("oba")) #skilar "2"
print (x.rindex("lol")) #skilar valueError