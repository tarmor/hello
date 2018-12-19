aasta= int (input("Palun sisesta positiivne aasta arv: "))
if aasta % 4==0 and aasta % 100 != 0:
    print ("Tegemist on liigaastaga!")
elif aasta % 4 != 0:
    print ("Tegemist on lihtaastaga")
