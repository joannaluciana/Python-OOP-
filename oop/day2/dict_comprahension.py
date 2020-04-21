our_dict = {1:"1", 2:"2", 3: "3"}

lista1=[1,2,3,0, 100]
lista2=["1","2","3","0", "dsdddda"]

print(dict(zip(lista1, lista2)))
print(list(zip(lista1, lista2)))
print(list(zip(lista1, lista2, lista1)))

list_of_tuples = [(1,1),(2,2)]
print(dict(list_of_tuples))


dict_from_zip= dict(zip(lista1,lista2))

print(dict_from_zip.items())

x = {k*10: v for (k,v) in dict_from_zip.items() if k<3 and v<"9"}

print(x)