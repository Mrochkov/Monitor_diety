
from biblioteki import sortuj as s

lista = ["Izab","Iza Z"]
lista2= [("Izab",0),("Iza Z",0)]

#lista = ["Zupa pomidorowa","Zupa", "Zupa grzybowa"]
print(lista)
print(sorted(lista))
print(list(reversed(sorted(lista))))
print()
#lista2 = [("Zupa pomidorowa", 0),("Zupa", 0),("Zupa grzybowa", 0)]
print(lista2)
s.quickSort(lista2,0,len(lista2)-1,0,s.letter_greater, s.letter_less, reverse=False)
print(lista2)
s.quickSort(lista2,0,len(lista2)-1,0,s.letter_greater, s.letter_less, reverse=True)
print(lista2)



print(lista)
lista[0] ='XDD'
print(lista)
