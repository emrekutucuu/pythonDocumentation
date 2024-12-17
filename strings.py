# -*- coding: utf-8 -*-
# stringler char dizileridir
a = "Merhaba Dünya"
print(a[2]) # a değişkeninin 2. indexini ver
print(a[2:5]) # 2. indexten 5. indexe kadar (5 dahil değil) ver
print(a[2:]) # 2. index ve sonrasını ver
print(a[:5]) # 5. indexe kadar ver
# Yukarıdaki işlemlere substring denir
b = len(a) # len fonksiyonu uzunluk ölçer
print(b)
# değişkenin uzunluğunu bilmiyor fakat son harfi görmek istiyorsak:
print(a[len(a)-1:len(a)])
print("########################")
# Python'da küçük ve büyük harfler birbirinden farklıdır. Bu
# durumda karışıklığı önlemek için veri tabanından gelen
# değerleri genellikle tamamen küçük harfe çevirerek işlem yapılır.
# Küçük büyük harfe çevirme işlemleri lower ve upper fonksiyonları
# kullanılır
mesaj = "MerHabA DüNya"
print(mesaj.upper()) # Hepsi büyük
print(mesaj.lower()) # Hepsi küçük
print("########################")
# replace fonksiyonu değişkende ifadeleri değiştirmemizi sağlar
mesaj2 = "Merhaba Dünya üüüü"
print(mesaj2.replace("ü","u"))
print("########################")
# split fonksiyonu string değişkeni kelime kelime ayırmaya yarar
# genellikle veri tabanından gelen ifadeleri ayırmada kullanılır
mesaj = "Enre Kutucu 24 Zonguldak"
print(mesaj.split()) # default olarak boşluklardan itibaren ayırır
# fakat farklı şekilde ayırmak mümkündür. Veri tabanından gelen 
# ifadeler genellikle ; ile gelirler
mesaj = "Emre;Kutucu;24;Zonguldak"
print(mesaj.split(";"))
print(mesaj.split(";")[2]) # Değişkeni ; ifadesine göre ayır ve
# ikinci indexi göster
print("########################")
# input kullanıcıdan değer almayı sağlar. Alınan değer string'tir
ad = input()
print(ad)
sayi1 = input("sayi 1 = ")
sayi2 = input("sayi 2 = ")
print(int(sayi1)+int(sayi2))















