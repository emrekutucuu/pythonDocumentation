# Modüller, başka yerdeki kodlara yani mevcut dosyadan farklı dosyalara erişmek demektir
# Buradan moduleTest.py ve moduleTest2.py dosyasına erişeceğiz

import moduleTest

print(moduleTest.topla(5, 5))
print(moduleTest.carp(5, 5))

import moduleTest2 as mTest # Burada modulümüzü isimlendirme işlemi yaptık
print(mTest.topla(7, 6))
print(mTest.carp(7, 6))

print(mTest.customer["firstName"])

from moduleTest import carp # Burada bir dosyaya tamamen erişmek yerine o dosyanın içindeki
print(carp(4,2))            # bir değere eriştik

# Hazır modüller var
