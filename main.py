#%%
n = int(input("sayi :"))
yildiz = ""
for x in range(n):
    yildiz = yildiz + "*"
    print(yildiz)
    
#%%
sayi = int(input("sayi:"))
asalMi = True
for x in range(2,10):
    if sayi % x == 0:
        asalMi = False
        break
if asalMi: # Default true algılar
    print("sayı asal")
else:
    print("sayı asal değil")

#%%
# Array toplama
x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[9,8,7],[6,5,4],[3,2,1]]
sonuc = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        sonuc[i][j] = x[i][j]+y[i][j]
        
print(sonuc)
#%%

class Islemler:
    def __init__(self, s1, s2):
        self.s1=s1
        self.s2=s2
    def topla(self):
        return self.s1+self.s2
    def cikar(self):
        return self.s1-self.s2
    def carp(self):
        return self.s1*self.s2
    def bol(self):
        return self.s1/self.s2
    
tercih = input("Bir tercih yapınız : \n 1 : Topla \n 2 : Çıkar \n 3 : Çarp \n 4 : Böl")
s1 = int(input("sayi 1 ="))
s2 = int(input("sayi 2 = "))
islem = Islemler(s1, s2)

if tercih == 1:
    islem.topla()
    


      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      