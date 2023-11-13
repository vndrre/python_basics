t = ["Kivi", "Paber", "Käärid"]

from random import randint

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Kivi, Paber või Käärid?: ")
    if player == computer:
        print("Viik!")

    elif player == "Kivi":
        if computer == "Paber":
            print("Sa kaotasid..", computer, "katab", player)
        else:
            print("Sina võitsid!", player, "purustab", computer)

    elif player == "Paber":
        if computer == "Käärid":
            print("Sa kaotasid..", computer, "lõikab", player)
        else:
            print("Sa võitsid!", player, "katab", computer)

    elif player == "Käärid":
        if computer == "Kivi":
            print("Sa kaotasid..", computer, "purustab", player)
        else:
            print("Sa võitsid!", player, "lõikab", computer)

    else:
        print("See ei ole kehtiv näidend. Kontrolli oma õigekirja!")

player = False
computer = t[randint(0,2)]