import random
##13.1
#a.

n = int(input("n="))
m = []
s = 0
for i in range(1,n+1):
    a=random.randint(1,n)
    m.append(a)
print(m) 
for j in m:
    s=s+j 
print(s)

#b

n = int(input("n="))
m = []
p = 1
for i in range(1,n+1,1):
    a=random.randint(1,n)
    m.append(a)
    
print(m)

for j in m:
    p=p*j

print(p)

#v

import math
n = int(input("n="))
m = []
s = 0
for i in range(-n,n+1):
    a=random.randint(1,n)
    m.append(a)
print(m)
for j in m:
    s=s+(math.fabs(j))
print(s)

#g

n = int(input("n="))
m = []
p = 1
for i in range(-n,n+1):
    a=random.randint(1,n)
    m.append(a)
print(m)
for j in m:
    p=p*(math.fabs(j))
print(p)


##d
while True:
    n = int(input("n="))
    b = { 
        1 : "dushanba" ,
        2 : "seshanba" , 
        3 : "chorshanba" ,
        4 : "payshanba" , 
        5 : "juma" ,
        6 : "shanba" ,
        7 : "yakshanba" 
        }
    if a in b:
        print(b[a])
    else:
        print("bunday kun yoq")
while True:
    n = int(input("n=")) 
    uzunlik = len(str(n))  
    son = { 
         1 : "bir xonali" ,
         2 : "ikki xonali" , 
         3 : "uch xonali" ,
         4 : "tort xonali" , 
         5 : "besh xonali" ,
         }
    if uzunlik in son:
        print(son[uzunlik])




n = int(input("n="))  
birlik = { 
        1 : "bir " ,
        2 : "ikki " , 
        3 : "uch " ,
        4 : "tort " , 
        5 : "besh " ,
        6 : "olti" ,
        7 : "yetti" ,
        8 : "sakkiz",
        9 : "toqqiz",
        0 : " "
        }
unlik = { 
        1 : "o'n " ,
        2 : "yigirma " , 
        3 : "o'ttiz " ,
        4 : "qirq " , 
        5 : "ellik " ,
        6 : "oltmish" ,
        7 : "yetmish" ,
        8 : "sakson",
        9 : "toqson",
        0 : " "
        }
yuzlik = { 
        0 : " " ,
        1 : "yuz " ,
        2 : "ming " , 
        3 : "milliom " ,
        4 : "milliard " , 
        }
suz=str(n)
len_suz = len(suz)
if len_suz ==1:
    
    chiqish=birlik[int(suz[0])]
    
elif len_suz ==2:
    
    chiqish=unlik[int(suz[0])]+"  "+birlik[int(suz[1])]
    
elif len_suz ==3:
    
    chiqish=birlik[int(suz[0])]+ " "+yuzlik[int(suz[1])]+ " " +unlik[int(suz[2])]+" " +birlik[int(suz[3])]
elif len_suz ==4:
    
    chiqish=birlik[int(suz[0])]+ " "+yuzlik[int(suz[1])]+ " " +birlik[int(suz[0])]+ " "+yuzlik[int(suz[0])]+ " " +unlik[int(suz[3])]+" " +birlik[int(suz[0])]
print(chiqish)


