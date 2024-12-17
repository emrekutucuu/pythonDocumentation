# Dictionary, set'lere benzer ve set'ler gibi verileri sırasız tutar
sozluk = {
    "dirty" : "kirli",
    "early" : "erken",
    "enough" : "yeterli"
    }
print(sozluk)
# print(sozluk[2]) Sözlükte index diye bir kavram yoktur
# Bunun yerine key'lere göre arama yapılır. Sol taraf key karşılığı value
print(sozluk["early"])
sozluk["enough"] = "yeteri kadar" # Bir keyin değerini değiştirme
sozluk["fire"] = "yangın" # Dictionary'e yeni bir veri ekleme
# Bir veriyi değiştirirken key ifadesini yanlış yazmak, keyin valuesini
# değiştirmek yerine yeni bir veri eklemeye sebep olur. Dikakt edilmeli

sozluk2 = dict(fall = "düşmek", divorced = "boşanmış") # Farklı
# şekilde dictionary oluşturma yöntemi
del(sozluk2["fall"]) # Dictionary'den bir veriyi silme işlemi.
# Dictionary'de remove fonksiyonu kullanılmıyor.
print(sozluk2)