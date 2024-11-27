from datetime import *
from calendar import *
from random import *
from math import *


#Ülesanne 1
tana=date.today() #название() - функция (требует скобки)
tanaf=date.today().strftime("%B %d,%Y")

print(f"Tere! Täna on {tanaf}")
d=tana.day #название - свойство (без скобок)
m=tana.month
y=tana.year
print(d)
print(m)
print(y)

novP=monthrange(2024,11)[1]
jaaknov=novP-d

detsP=monthrange(2024,12)[1]
jaakdets=novP+detsP-d

print(f"Kuu lõppuni on {jaaknov} päeva")
print(f"Aasta lõppuni on {jaakdets} päeva")

\n
#Ülesanne 2
vastus1=3 + 8 / (4 - 2) * 4
vastus2=3 + 8 / 4 - 2 * 4
vastus3=(3 + 8) / (4 - 2) * 4
print(vastus1,"\n",vastus2,"\n",vastus3)


#Ülesanne 3
#Ruudu sees asub ring. Ringi raadius on R.
#Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.
try: 
    R=float(input("sisesta R: "))
    Sk=pi*R**2 #** - степень
    Lk=2*pi*R
    Skv=R*2**2
    Lkv=2*R*4
    print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")
except:
    print("On vaja number")


R=int(random()*100) #генерирует значения от 0.0...1.0
print(f"R={R}")
Sk=pi*R**2 #** - степень
Lk=2*pi*R
Skv=R*2**2
Lkv=2*R*4
print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")