#  Yazılım giderek standartlaşmakta. Json bu standartlaşmayı sağlayarak verileri
# tutma yöntemi diyebiliriz. 
# jsonplaceholder sitesinde data örneklerine ulaşabiliriz

import json

data = '{"firstName":"Emre","lastName":"Kutucu"}' # string ifadeyi json formatında yazdık
# Bu format string tipinde gözükecektir. Bunu json tipinde göstermek için :
y = json.loads(data)
print(y["firstName"])
print(y["lastName"])

customer = {
        "firstName":"Emre",
        "email":"emmrekutucu@gmail.com"
    }
customerJson = json.dumps(customer) # Bir sözlüğü json formatına çevirdik
print(customerJson)














