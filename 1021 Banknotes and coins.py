A=float(input())
N=A
a=N/100
b=N%100
c=b/50
d=b%50
e=d/20
f=d%20
g=f/10
h=f%10
i=h/5
j=h%5
k=j/2
l=j%2

E=A*100
B=(int(E))
m=B%100
n=m/50
o=m%50
p=o/25
q=o%25
r=q/10
s=q%10
t=s/5
u=s%5
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(a)))
print("{} nota(s) de R$ 50.00".format(int(c)))
print("{} nota(s) de R$ 20.00".format(int(e)))
print("{} nota(s) de R$ 10.00".format(int(g)))
print("{} nota(s) de R$ 5.00".format(int(i)))
print("{} nota(s) de R$ 2.00".format(int(k)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(l)))
print("{} moeda(s) de R$ 0.50".format(int(n)))
print("{} moeda(s) de R$ 0.25".format(int(p)))
print("{} moeda(s) de R$ 0.10".format(int(r)))
print("{} moeda(s) de R$ 0.05".format(int(t)))
print("{} moeda(s) de R$ 0.01".format(int(u)))