thisdict = {
    "eesnimi": "Andre",
    "perenimi": "Leppik",
    "sünniaasta": 2005,
    "elukoht": "Kuressaare",
    "magustoit": "küpsis"
}

x = thisdict.get("elukoht")
print(x)



for x in thisdict:
    print(thisdict[x])


def checkKey(thisdict, isikukood):
    if isikukood in thisdict.keys():
        print("Present, ", end =" ")
        print("value =", thisdict[isikukood])
    else:
        print("Isikukood puudub")

print("Dictionary suurus:", len(thisdict))

thisdict.update({"pikkus": "185 cm"})

del thisdict["sünniaasta"]
print(thisdict)