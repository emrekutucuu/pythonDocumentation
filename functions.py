# Fonksiyonlar bir kodu tekrar tekrar yazmak yerine bir kez yazıp çağrılarak
# kullanabilmeyi sağlar

sehir = "ankara"
print(sehir.upper())
print(sehir.endswith("a")) # endswith fonksiyonu değişkenin son harfini kontrol eder
# Fonksiyonlar burada olduğu gibi parametreli ve parametresiz olabilir
# Bunlar hazır fonksiyonlardır. Kendimizde fonksiyon oluşturacağız
print("2------------------------")

def selamla():
    """Fonksiyon açıklama alanı"""
    print("selam")
    
# Burada parametresiz bir fonksiyon oluşturduk

selamla()

def selamla2(isim):
    print("selam " + isim)
    
# Burada ise parametreli bir fonksiyon oluşturduk

selamla2("emre")
    
def selamla3(isim = "kullanıcı"):
    print("selam " + isim)
    
# Default parametreli fonksiyon, eğer hiçbir parametre belirtilmezse hata verme
# ve belirtilen parametreyi kullan

selamla3("can")
selamla3()

print("3---------------------------")

# Birden fazla parametreye sahip fonksiyon olabilir. Bu fonksiyonun 
# parametrelerinden bazıları default değer alabilirken bazıları almayabilir
# Default değer alanları sona yazmak gerekir

def selamla4(isim, soyIsim = "kullanici"):
    print("selam " + isim + " " + soyIsim)
    
selamla4("emre")
selamla4("emre","kutucu")

print(" 4 ----------------------------")

# değer return eden fonksiyonlar belirli bir işlemi gerçekleştirip sonuç veren fonksiyonlardır

def dikUcgenAlanHesapla(a,b):
    return a*b/2

alan = dikUcgenAlanHesapla(2, 3)
print(alan)

# Tek satırlı ve return eden fonksiyonları lambda fonksiyonu ile kısaca yazabiliriz
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesapla2(3,6))

x = dikUcgenAlaniHesapla2
print(x(4,5))

# Fonksiyonu bir değişken gibi isimlendirdim































