# exceptions hata yönetimi anlamına gelmekte

try:
    sayi = int(input("sayı = "))
except ValueError: # ValueError type uyuşmazlığı demektir
    print("sayı girmediniz")
except ZeroDivisionError: # Paydanın sıfır olması hatası
    print("payda sıfır olamaz")
except: # Geriye kalan tüm hatalar. Diğerleri kullanılmadan sadece bu da kullanılabilir
    print("hatalı giriş")
finally:
    print("dosyayı kapat")
    # finally bloğu try ve except bloklarından biri çalıştıktan sonra çalışır. Dosya
    # kapatma işlemleri gibi işlemlerde kullanılır

print("işlem")

# Hata yönetimi için try ve except bloklarını kullanıyoruz. İkisinden biri çalışır
# Burada da yazdığımız gibi farklı farklı hata türleri vardır. Bunların ne olduğunu öğrenmek gerek
# except (ValueError, ZeroDivisionError): şeklinde ikili hata gösterimi de olabilir