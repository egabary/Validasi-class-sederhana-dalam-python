import pandas as pd
import numpy as np

#validasi
np="jhonsmith"
yo=20
is_new_pasien=True

print("Nama Pasien: \n",np,"age: \n",yo,"pasien baru: \n",is_new_pasien)

#input sederhana
name = input("siapa lu?")
print(name+ "Hai")
umur=input("tahun berapa lu lahir? ")
age = 2020 - int(umur)
print (age)

#input penambahan angka folat 
#penulisan cara 1 
first = input("angka pertama lu ? ")
second = input("angka kedua lu ? ")
sum= float(first) + float(second)
print ("jumlahnye : " + str(sum))

#penulisan cara 2 
pertama =float(input("angka yang pertama lu ? "))
kedua =float(input("angka yang kedua lu ? "))
sum = pertama + kedua
print ("jumlahnya nih : "+str(sum))

#validasi benar atau tidak
a=9
print(a>8 and a>10)

#pencobaan class 
class hero(object):
    emphero=0
    status = "This general status of hero"
    def __init__(self,nama,power,agi,intel,damage,mos):
        self.nama  = nama
        self.power = power
        self.agi   = agi
        self.intel = intel
        self.damage= damage
        self.mos   = mos
        hero.emphero +=1
    def tampilan (self):
        print("nama hero : ",self.nama,"power: ",self.power,"agi: ",self.agi, "intel: ",self.intel,"damage: ",self.damage, " mos: ",self.mos)
    
axe = hero("Axe",50,26,21,90,35)
am =  hero("anti mage",25,50,24,35,50)
axe.tampilan()
am.tampilan()
print("Jumlah hero yang ada: ",hero.emphero)
