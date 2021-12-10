print("This is read mood")
f = open('books.txt', 'r')
print(f.read(6))
print(f.readline())

print("This is Write mood. When you're writing then all documents are gone")
g = open('books.txt','w')
f.write('new document in writing mood \n')

print("when you're using append mood then all documents are saved and Add new document")
h = open('books.txt','a')
h.write('Previous document and new document \n')