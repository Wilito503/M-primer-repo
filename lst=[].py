lst=[]
x= input("Escriba la coordenada x del punto P: ")
y= input("Escriba la coordenada y del punto P: ")
Key1=input("Cual es su clave: ")
modd=input("Ingrese el modulo del numero primo a utilizar: ")
modd=int(modd)
x=int(x)
y=int(y)
key1=int(Key1)
t=format(key1, '0b')
for i in t:
    lst.append(int(i))
n=(len(lst))
lst.reverse()
#print("para calcular ",key1,"P sera de la siguiente forma:\n")
#for i in  range (0,n):
 #   if lst[i]==1:
#        print(2**i,"(",lst[i],")","(",x,",",y,") +")
k=int(key1/2)
if k%2==0:
    for i in range (0,k):
        num=3*(x**2)-3
        den=2*y
        for j in range (1,modd):
            if (den*j % 13)==1:
                b=j
        m=num*b%13
         
    
        