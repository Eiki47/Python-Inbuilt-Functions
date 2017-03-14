#svipað og find nema leitar frá hægri
#finnur fyrsta indexið af gefnum hlutstreng
#skilar -1 ef hlutstrengurinn er ekki fundinn
x = "foobar"
print (x.rfind("o")) #skilar "2"
print (x.rfind("oba")) #skilar "2"
print (x.rfind("lol")) #skilar "-1"