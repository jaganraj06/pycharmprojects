#sortingwithkey
items=[( "Arni","Cheyyar",102256),("Caddalore","Kurinchipadi",102134,),("Dindukkal","Athoor",102247),("Erode","Modakurichi",102178)]
items.sort()
print(items)
items.sort(key=lambda item:item[1])
print(items)
items.sort(key=lambda item:item[2])
print(items)
items.sort(key=lambda item:item[2],reverse=True)
print(items)
items.sort(key=lambda item:item[0])
print(items)

print(sorted(items, key=lambda item:item[1]))
print(items)
print(sorted(items, key=lambda item:item[2]))
print(sorted(items, key=lambda item:item[0]))
