dictionaryExample = {"name" : "adam",
                     "id" : "193-35-487",
                     "year" : "1st"}

print(dictionaryExample)

for x in dictionaryExample.values():
	print(x)


for x, y in dictionaryExample.items():
	print(x, "-",y)

for x in dictionaryExample.items():
	print(x)

del dictionaryExample["name"]

print(dictionaryExample)