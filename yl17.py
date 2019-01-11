from random import randint

do_continue = "jah"
choices = ["Kivi", "Paber", "Käärid"]

while do_continue == "jah":
    player = input("Kivi, Paber, Käärid? ")
    computer = choices[randint(0,2)]
    if player == computer:
        print("Viik!")
    elif player == "Kivi" and computer == "Paber" or player == "Paber" and computer == "Käärid" or player == "Käärid" and computer == "Kivi":
        print("Sina kaotasid ja arvuti võitis!")
    elif player == "Paber" and computer == "Kivi" or player == "Käärid" and computer == "Paber" or player == "Kivi" and computer == "Käärid":
        print("Sina võitsid ja arvuti kaotas!")
    else:
        print("Kirjutasid midagi valesti, vaata üle!")

    do_continue = input("Kas soovid jätkata? ")   

print("Mäng läbi!")