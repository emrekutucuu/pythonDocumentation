""" Dosya işlemleri yakın veya uzak masaüstlerindeki dosyaları okuma, üzerinde işlem yapma
 işlemleridir """
f = open("musteriler.txt") # dosya işlemleri için open fonksiyonu kullanmaktayız 
# Burada "w" komutu ile musteriler.txt isimli bir dosyayı oluşturma komutu verdik.
# Bu default olarak "r" dir.
# Komutlar ve işlevleri : 
    # r : oku 
    # w: yoksa oluştur,varsa üzerine yaz 
    # a : mevcut dosyaya ekleme yap 
    # x : yoksa oluştur, varsa hata ver

# f.read() # Dosyanın return ettiği değeri göster
# print(f.read()) # Dosyanın içeriğini göster
# f.read(), print(f.read()), f.readline() bunlar aynı anda kod içerisinde çalıştırıldığında
# düzgün çalışmıyor, birinin çalışması diğerini etkiliyor bu yüzden aynı anda kullanılmazlar
print(f.readline()) # Satır okuma. Otomatik olarak birinci satırı okur bir daha yazarsan 
# ikinci satırı okur
print(f.readline())

for l in f:
    print(l) # Tüm satırları okuma

f.close() # Açılan dosya bellekte açık durur. Kapatmak için kapatma kodu verilir

fileToAppend = open("ogrenciler.txt","a")
fileToAppend.write("\n")
fileToAppend.write("Vahide") # ogrenciler.txt isimli bir dosya oluşturduk ve write
# fonksiyonu ile içerisine veri ekledik. Üst satırda \n kullanmamızın sebebi
# Emre verisini silip yeni veri yazdığımızda bu veriyi Emre nin yanına değil de 
# alt satırına yazmasını istediğimiz için
# Eğer dosyayı açma işleminde a yı silip w yazar ve bir veri eklersem mevcut verileri
# silip yerine yeni veriyi yazar
fileToAppend.close()

# import os # Dosya silme işlemleri için os modulünü import ediyoruz
# os.remove("ogrenciler.txt")
# print(os.path.exists("ogrenciler.txt")) # Gösterilen dosya var mı
# os.rmdir("empty") # Belirtilen klasörü sil











