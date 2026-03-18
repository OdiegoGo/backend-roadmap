#Excercício 1:
lista=[1,2,3,4,5,6,7,8,9,10]
for i in lista:
    print(i)

#Excercício 2:
lista=input().split()
nums=[]
for i in lista:
    nums.append(int(i))
soma=sum(nums)

#ou

soma=0
for i in nums:
    soma+=i
print(soma)

#Excercício 3:

maior=0

for i in range(len(nums)):
    if i == 0:
        maior=nums[i]
    else:
        if nums[i]>maior:
            maior=nums[i]
    

#Excercício 4:

menor = 0

for i in range(len(nums)):
    if i == 0:
        menor = nums[i]
    else:
        if nums[i]<menor:
            menor = nums[i]


#Excercício 5:

lista=[1,2,3,4,5,6,7,8,9,10]
pares=[]
for i in lista:
    if i%2==0:
        pares.append(i)


#Excercício 6:

contador=0
for i in lista:
    contador+=1


#Excercício 7:

lista=[1,1,2,3,3,4,5]
sem_duplicados=[]

for i in lista:
    if i not in sem_duplicados:
        sem_duplicados.append(i)


#Excercício 8:

lista=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(lista)):
    lista[i]=lista[i]*2

#Excercício 9:

lista=[1,2,3,4,5,6,7,8,9,10]
soma=0
média=0
for i in lista:
    soma+=i
média=soma/len(lista)

#ou

média=sum(lista)/len(lista)

#Excercício 10:

lista=[1,2,3,4,5,6,7,8,9,10]
lista_invertida=[]
for i in range(len(lista),-1,-1):
    lista_invertida.append(lista[i])
