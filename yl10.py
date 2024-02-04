name = input("Sisesta oma nimi: ")
print("Tere", name)

location = input("Elukoht: ")

age = input("Vanus: ")
age = int(age)

if age < 18:
    print("Liiga noor..")
else:
    print("Palju õnne täiskasvanuks saamise eest!")
    

