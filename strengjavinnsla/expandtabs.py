#hækkar bil á milli tabba
#sjálfgefið bil á milli tabba er 8
x="foo\tbar" # \t er skilgreint sem tab
print (x.expandtabs(0)) #skilar foobar
print (x.expandtabs(5)) #skilar foo   bar þar