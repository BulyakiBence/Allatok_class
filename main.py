from allat import Allat
from emlos import Emlos
from emlos import Macska
from emlos import Kutya
# Állat 1: Bodri, faj: kutya, életkor: 5 év
# Állat 2: Cirmi, faj: macska, életkor: 3 év

allat1 = Allat("Bodri", "kutya", 5, "kert", "közepes")
allat2 = Allat("Cirmi", "macska", 2, "ház", "közepes")

print(allat1)
print(allat2)

emlos1 = Emlos("Morzsi", "kutya", 5, "kert", "barna")
emlos2 = Emlos("Cicó", "macska", 2, "kert", "cirmos")

print(emlos1)
print(emlos2)

macska1 = Macska("Hubert", 4, "ház", "fehér")
print(macska1)
macska1.dorombol()

kutya1 = Kutya("Cézár", 7, "udvar", "fekete")
print(kutya1)
kutya1.ugat()