# Classları bir klasör gibi düşünmek gerek
# Belirli fonksiyonları, kodları, işlemleri bir arada tutan, sınıflandıran yapılardır
# class isimlendirilirken büyük harfle başlanır

class Matematik:
    def topla(self,s1,s2):
        return s1+s2
    def cikar(self,s1,s2):
        return s1-s2
    def carp(self,s1,s2):
        return s1*s2
    def bol(self,s1,s2):
        return s1/s2

matematik = Matematik() # Burada Matematik classını bir nesneye atadık
# Bu nesne Matematik classı için bellekte yer açtı. Bu şekilde classımızı kullanabileceğiz
print(matematik.carp(2,5))

# *** Önemli *** 
# classları içerisinde fonksiyon kullanırken self ifadesini kullanmamız gerekiyor yoksa
# program hata veriyor

class MatematikX:
    def __init__(self,s1,s2): # Her classta böyle bir fonksiyon bulunur fakat gözükmez. Üstteki
                        # classta da mevcuttur. Buna constructar denir. Bu classı 
                        # tamamen kapsayan global bir fonksiyondur. Örneğin şu an
                        # olduğu gibi class içindeki her fonksiyonda ortak parametreler
                        # kullanılıyor ise bunu globala birkez yazarak yazım kolaylığı elde
                        # edebiliriz.
        self.s1 = s1
        self.s2 = s2       
    def topla(self):
        return self.s1+self.s2
    def cikar(self):
        return self.s1-self.s2
    def carp(self):
        return self.s1*self.s2
    def bol(self):
        return self.s1/self.s2

matematik = MatematikX(4,5)
matematik2 = MatematikX(3,4)
print(matematik.carp())
print(matematik2.carp())

print("--------------------------------")
# Özellik barındıran classlar, içerisinde özellikleri tutan ve gerektiğinde bu özellikler
# kullanılarak nesneler oluşturmayı sağlayan classlardır

class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName # Bu şekilde self etmemizin amacı parametrelerin
        self.lastName = lastName   # class dışından görünebilir olmasını sağlamak
        self.age = age

person1 = Person("Emre", "Kutucu", 25)
person2 = Person("Akın", "Taşbek", 25)
print(person2.lastName)

# Bir çalışan ve bir müşteri de bir insandır fakat ikisinin farklı özellikleri vardır
# Örneğin çalışanın maaşı, müşterinin ise kredi kartı numarası vardır. Bu işlemler için
# çalışan ve müşteri olarak iki farklı class oluşturuyoruz fakat bu classlara person
# classının özelliklerini eklemek için bunları person classına bağlıyoruz
# Buna inheritance (miras yapısı) denir

class Worker(Person):
    def __init__(self, firstName, lastName, age, salary):
        super().__init__(firstName, lastName, age)
        self.salary = salary
class Customer(Person):
    def __init__(self, firstName, lastName, age, cardNumber):
        super().__init__(firstName, lastName, age)
        self.cardNumber = cardNumber

handan = Worker("handan","erdem",21,7500)
cemil = Customer("cemil","tugay",45,56462)
print(f"{handan.firstName} {handan.lastName} maaşı: {handan.salary}")
print(f"{cemil.firstName} {cemil.lastName} kart numarası: {cemil.cardNumber}")
# print içerisindeki f ifadesi print içerisine değişken yerleştirmeye yarar. Eğer 
# f kullanmıyor olsaydık print ifadesini şu şekilde yazmamız gerekecekti : 
    # print(cemil.firstName + " " + cemil.lastName + " kart numarası: " + str(cemil.cardNumber))


















