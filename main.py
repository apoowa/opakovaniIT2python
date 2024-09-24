import random
#jmeno
jmeno = "laura"
#prijmeni
prijmeni = "hanackova"
#vypis
print ("jmeno:", jmeno)
print ("prijmeni:", prijmeni)
#vstup pro jmeno
user_input = input("vypiste sve jmeno")
#delky promennych
print ("delka jmena:",
len (jmeno))
print ("delka prijmeni", len(prijmeni))
#promenna
cislo = 6
#cyklus
for i in range (5):
    cislo -= 3
#vypis
print ("vysledna hodnota:", cislo)
#podminka pro vek
try:
    vek = int(input("vypiste svuj vek"))
    print("dekuji")
except ValueError:
    print("zadejte celociselnou hodnotu")
#nahodne cislo 
print(random.randint(1,10))
