# tuple yalnızca python'da kullanılan diğer dillerde genellikle
# olmayan bir liste türü
# Özellik olarak tuple'lar değiştirilemez ve sabittir. Bu bellek
# performansı sağlar

x = (5,7,"sinop",20.0) # listeler [] ile oluşturulurken tuple'lar 
# () ile oluşturulur
y = (4,8,9,"mouse",[10,20,30],5) # tuple içinde liste, liste içinde tuple
# tutmak mümkündür
print(y)
print(len(y))
print(y[1:2]) # virgüllü gösterim, tuple'a özgü

z = ("Emre") 
print(type(z)) # z'nin tipini str olarak verir çünkü tuple'ları tek
# eleman olarak oluşturduğumuzda program bunun tuple olduğunu 
# algılayamaz. Bunun tuple olduğunu belirtmek için tek verinin sonuna
# virgül koyarız
z=("emre",)
print(type(z))
