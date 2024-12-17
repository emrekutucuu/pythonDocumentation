# set'lerde tuple'lar gibi bir liste türüdür. Farkları ise indexsizdir
# ve sırasızdır. tuple'lara kıyasla daha yüksek performans gösterirler
# herhangi bir veri silinemez veya değiştirilemez ama yeni veriler eklenebilir
# {} ile oluşturulur

kahveler = {"latte","mocha","filtre"}
print(kahveler) # Rastgale sıralar

print("icelatte" in kahveler) # Belirilen veri set içerisinde var mı true/false
# Büyük küçük harf duyarlılığına dikkat etmek gerekir

if "mocha" in kahveler:
    print("Listede var") # True ifade döndürürse işlemi gerçekleştirecek.

kahveler.add("icelatte") # Set'e beliritilen veriyi ekle
print(kahveler)
kahveler.update(["çay","Türk kahvesi","americano"]) # Belirtilen verileri
# Set'e ekle
print(kahveler)
kahveler.remove("americano") # Belirtilen veriyi sil. Eğer belirtilen
# veriyi set içerisinde bulamazsa hata verir
# Veriyi bulamazsa hata vermeden program çalışmaya devam etsin diye :
kahveler.discard("espresso")
print(kahveler)
kahveler.clear() # Set'in içindeki verileri siler set durmaya devam eder
del kahveler # Set'i tamamen siler
# Başka bir set oluşturma yöntemi :
caylar = set(("çay","adaçayı","papatya"))

# Set union : İki farklı set'i birleştirme ve ortak verileri bir 
# kez yazma
a = {1,2,3,4}
b = {3,4,5,6}
print(a | b)
# Bir başka birleştirme (union) yöntemi
print(a.union(b))

print(a & b)
print(a.intersection(b)) # Set'ler içerisindeki ortak verileri gösterme
# yöntemleri

print(a - b)
print(a.difference(b))
print(b.difference(a)) # Set'ler içerisindeki birbirinden farklı verileri
# gösterne yöntemidir

print(a ^ b)
print(a.symmetric_difference(b)) # Set'lerde ortak veriler haricindeki 
# verileri birleştirme
    








