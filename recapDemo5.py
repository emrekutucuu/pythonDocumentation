# Listelerde hata yönetimi ile ilgili çalışma

import sys # Karşılaşılan hataların nedenlerini göstermeye yarayacak kütüphane

list = [7,"emre",8,0,"6"]

for i in list:
    try:
        print("gelen sayı: " + str(i))
        sonuc = 1/int(i)
        print(sonuc)
    # except ValueError:
    #     print(str(i) + " sayı değil")
    # except ZeroDivisionError:
    #     print(str(i) + " payda sıfır olamaz")
    except:
        print("hesaplanamadı")
        print("hesaplanamama sebebi" + str(sys.exc_info()[0])) # sys.exc_info() array olarak gelir
        # bu yüzden [] kullanarak gösterim sağlıyoruz.
# listeden gelen değerleri 1'in paydasına koyarak hesaplama yaptık, 1'e bölünemeyecek verileri
# hata olarak gösterdik
