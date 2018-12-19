nimi= input ("Mis on sinu nimi: ")
print ("Tere " + nimi + "!")
elukoht= input ("Koht kus sa elad? ")
if elukoht== ("Saaremaa"):
    print ("Parim koht elamiseks, Sul on hea maitse!")
else:
    print ("Sa peaksid Saaremaale kolima!")
vanus= int (input ("Kui vana sa oled?: "))
if vanus < 18:
    print ("Oled liiga noor, et autot juhtida!")
elif vanus == 18:
    print ("Palju onne sunnipaevaks!")
elif vanus > 18:
    print ("Tohid autot juhtida!")

