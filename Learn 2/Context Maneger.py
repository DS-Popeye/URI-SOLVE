with open('books.txt','r') as f:
	print(f.read())

f = open('books.txt','r')
print(f.read())
f.close()