# w3school veritabanı bilgilerini geliştirmek için faydalı

import sqlite3 # Sqlite işlemlerini yapmamızı sağlayacak modül
# python'da çok fazla modül var, bunlar işleri yapmayı kolaylaştırıyor

def selectIslemleri(): 
    # Burada veritabanına ait select yani sorgulama işlemlerini yapacağız
    connection = sqlite3.connect("chinook.db") # Burada veritabanı dosyasına bağlantı sağladık
    # connection değişken ismini biz belirliyoruz
    # Eğer veritabanı ismini yanlış yazarsak yazdığımız adla yeni bir veritabanı oluşturur
    
    cursor = connection.execute("select * from customers") # Veritabanı içindeki customers
    # tablosunun tüm sutünlarını getir cursora ver. Burada * ifadesi tümü anlamına gelir
    
    for row in cursor:
        print("firstName : " + row[1]) # Customers'ın firstName'ini almak istiyoruz. firstName
        # birinci indexli sutünda o yüzden birinci sutünü belirtiyoruz
    # Eğer connection kısmına * yerine "FirstName,LastName yazarsak sadece bu iki sutünü getirecek
    # ve yukarıdaki for döngüsünde istediğimiz birinci index (FirstName 0. LastName 1) LastName'e
    # denk geleceği için bize LastName'i gösterecek
    print("--------")
    cursor2 = connection.execute("select FirstName,LastName from customers where city = 'Prague'")
    # Şehri Prague olan müşterilerin FİrstName ve LastName'ini al
    for row in cursor2:
        print(row[0] + " " + row[1])
        
    print("--------")
    # Veritabanındaki tüm tabloları getir ve bunu yaparken FirstName sutünunu alfabetik
    # olarak getir
    cursor3 = connection.execute("select * from customers order by FirstName")
    for row in cursor3:
        print("FİrstName : " + row[1])
    # Eğer coonnection aşamasında FirstName'in ardından desc yazarsak bu da tersten sırala demektir
    # Eğer FirstName, LastName yazarsak bu da FİrstName'e göre sırala FİrstName'i aynı olanları
    # LastName'e göre sırala demek
    print("--------")
    
    # Veritabanında bir veriden kaç tane var
    cursor4 = connection.execute("select city,count(*) from customers group by city")
    for row in cursor4:
        print(row[0] + " " + str(row[1])) # row[1] bir int getiriyor, print ederken str'ye dönüştürüyoruz
    # Bunu alfabatik veya tersine sıralamak istersek sorgu sonuna order by eklemek gerekir. Önemli nokta
    # order by her zaman sorgunun sonuna yazılmalı. order by 'ı count için yapıp sayıya göre sıralama da yapabiliriz
    print("--------")
    # having sorgusu ile sorguya şart koyuyoruz. Burada city'ye göre sırala ve 1 den büyük olanları ver dedik
    cursor5 = connection.execute("select city,count(*) from customers group by city having count(*) > 1")
    for row in cursor5:
        print(row[0] + " " + str(row[1])) 
    print("--------")
    # like komutu verinin içindeki ifadelere göre arama yapma
    # FirstName'inde j harfi geçen müşterilerin tüm özelliklerini getir
    cursor6 = connection.execute("select * from customers where FirstName like '%j%'")
    for row in cursor6:
        print(row)
        
    """ '%j%' : içinde j olan
        'j%'  : j ile başlayan
        '%j'  : j ile biten """
    
    connection.close()
selectIslemleri()

def insertIslemleri():
    # Burada veritabanına ait insert yani veri ekleme işlemlerini yapacağız
    connection = sqlite3.connect("chinook.db")
    connection.execute("insert into customers(FirstName, LastName, City, Email) values('Emre','Kutucu','Zonguldak','emmrekutucu@gmail.com')")
    # select işlemlerinde cursor ifadesi kullanırken burada kullanma gereği yoktur
    connection.commit() # Verimizi veritabanına commit ettik yani gönderdik
    # Bu işlemleri yaparak veritabanına veri ekledik. Burada normalde Email'i eklemiyorduk
    # fakat veritabanında Email kısmı zorunlu alan tutulduğu için ekleme işlemi için bizden 
    # Email istedi bu yüzden Email ekledik
    connection.close()
    
# insertIslemleri()

def updateIslemleri():
    # Burada update yani güncelleme işlemleri yapacağız
    connection = sqlite3.connect("chinook.db")
    connection.execute("update customers set city = 'Ankara' where city = 'Zonguldak'")
    # Burada where ifadesi çok önemli yoksa bütün şehirleri değiştirir
    connection.commit()
    
    connection.close()

# updateIslemleri() # Burada databa is locked hatası aldım ve bilgisayarı kapatıp açmak işe yaradı

def deleteIslemleri():
    # Burada delete işlemlerini yapacağız
    connection = sqlite3.connect("chinook.db")
    connection.execute("delete from customers where city = 'Ankara'")
    # customers tablosunda şehri ankara olanları sil
    connection.commit()
    
    connection.close()
    
# deleteIslemleri()

def joinIslemleri():
    """ join işlemleri denilen işlemler var, bu şudur ; kullandığımız veritabanları
    ilişkisel veri tabanıdır yani tablolar birbiri ile bağlantılıdır. Bizim örnek 
    veritabanımızda albums ve artists tabloları biribiriyle bağlantılıdır. Albums
    tablosunda albümlerin hangi sanatçıya ait olduğu artistsId ile gösterilmektedir.
    Bu durumda bu birbiri ile ilişkili iki tabloyu bir araya getirme işlemine join etme
    demekteyiz. join işlemleri için sqlite uygulamamızda "Execute SQL" kısmına gidiyoruz
    ve kodlarımızı buraya yazıyoruz
        select * from artists inner join albums 
        on artists.ArtistId = albums.ArtistId
    Bu kod albums ve artists tablolarını artistId'ye göre join eder
        select albums.Title, artists.Name from artists inner join albums 
        on artists.ArtistId = albums.ArtistId
    Bu kod albüm başlıkları ile sanatçı isimlerini yanyana getirir """
    
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select albums.Title, artists.Name from artists inner join albums on artists.ArtistId = albums.ArtistId""")
    for row in cursor:
        # print(type(row), row)
        print("Albüm ismi : " + row[0] + " Sanatçısı : " + row[1])
    connection.close()
    # Buradaki kod bloğu ile ilişkili iki tabloyu birbiriyle ilişkili şekilde gösterdik
        
joinIslemleri()
















