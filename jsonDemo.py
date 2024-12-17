import json # json dosyalarını okumak içim modulümüz

with open("users.json") as users: # users.json dosyasını okuma işlemini gerçekleştirdik ve verileri
# users kısayoluna taşıdık. with kullanmamızın sebebi işlemler bittiğinde dosyayı otomatik kapaması
    data = json.load(users) # verileri data isimli bir değişkene atadık
    print(data[0]["username"])
    print(data[0]["email"])
    print(data[0]["address"])
    print(data[0]["address"]["street"])
    print("-------------")
    for i in range(6):
        print(data[i]["username"]) # İlk beş kişinin kullanıcı adına ulaş