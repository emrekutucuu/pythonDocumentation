# Listeler en çok kullanılan değişkendir
ogrenci = ["Emre", "Handan", "Lale"]
print(ogrenci)
print(ogrenci[1]) # 1.inexi göster
print(ogrenci[-3]) # sondan 3. elemanı (indexi değil) göster
ogrenci.append("Miray") # Listeye yeni veri ekle
ogrenci.remove("Lale") # Listede yazılı veriyi sil
ogrenci[0] = "Enre Can" # Seçili indexteki veriyi değiştir
# ogrenci.clear() # clear fonksiyonu listenin verilerini siler
print(ogrenci)

print("########################")
# List constructor
sehirler = list(("Ankara", "İstanbul"))
print(sehirler)
# Bazı fonksiyonlar ------------------------
print(len(sehirler)) # len fonksiyonu index sayısını değil eleman
# sayısını gösterir
print(sehirler.count("Ankara")) # Listenin içinde belirtilen veriden
# kaç tane var
print(sehirler.index("Ankara")) # Belirtilen veri kaçıncı indexte.
# Bu fonksiyon belirtilen verinin baştan itibaren ilk olarak kaçıncı
# indexte olduğunu gösterir. Yani belirtilen veriden birden çok
# varsa yalnızca ilkinin indexini gösterir
sehirler.pop(1) # Belirtilen indexteyi veriyi sil
sehirler.insert(0, "Izmir") # Belirtilen index'e belirtilen
# veriyi ekle
print(sehirler)
sehirler.reverse() # Listeyi terse çevir
print(sehirler)

sehirler2 = sehirler # Listeler referans tiptir. Yani sehirler2'yi
# sehirler listesine atadığımızda ve sehirler2 'de bir değişiklik
# yaptığımızda bu değişiklik sehirler listesinde de olacaktır
# Listelerin diğer değişkenlerden farkıdır bu
# Bundan dolayı eğer bir listeyi yedeklemek veya farklı bir değişkene
# atama yapmak istersek copy fonksiyonunu kullanmalıyız
sehirler3 = sehirler.copy()

digerSehirler = list(("Zonguldak", "Denizli"))
sehirler.extend(digerSehirler) # Belirtilen listi
# belirtilen listenin sonuna ekle
print(sehirler)
sehirler.sort() # Listeyi alfabetik ya da sayısal olarak
# sıralamayı sağlar
print(sehirler)
# ------------------------------------------




