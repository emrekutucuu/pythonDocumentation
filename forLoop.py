sehirler = ["İzmir", "Ankara", "İstanbul"]
for sehir in sehirler:
    print(sehir[0:3]) # for döngüsüde if yapısı gibi
# blok yapıya sahiptir. Yani bir tab boşluk bırakıldığı
# takdirde o blok çalışmaya devam eder.
# Buradaki kodta sehir keyinde tutulan verinin ilk üç
# indexini göster komutu veriyoruz

print("----------------------")
sehirler = ["İzmir", "Ankara", "İstanbul"]
for sehir in sehirler:
    if sehir == "Ankara":
        break
    print(sehir[0:3])
# break komutu döngü belirtilen şartı sağladıysa
# döngüyü bitirir
print("----------------------")
sehirler = ["İzmir", "Ankara", "İstanbul"]
for sehir in sehirler:
    if sehir == "Ankara":
        continue
    print(sehir[0:3])
# continue komutu döngü belirtilen şartı sağladıysa
# döngünün o an ki dönme durumunu bitiriyor ve döngü devam ediyor
#%% # Bu ifade kodu bloklamaya yarar
for x in range(10): # range fonksiyonu belirtilen sayı kadar döngünün çalışmasını sağlar
    print(x)





    