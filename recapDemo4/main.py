""" Liste verilerinin dosyaya yazdırılması """
ogrenciler = ["Engin","Emre","Barlas","Asil"] # Genelde bu veriler dışarıdan gelecek

fileToAppend = open("ogrenciler.txt","a")
for i in ogrenciler:
    fileToAppend.write(i)
    fileToAppend.write("\n")

fileToAppend.close()