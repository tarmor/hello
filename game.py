import random
a =  random.randint(1, 100)
minu_pakutu = int(input("Paku arv: "))
while a != minu_pakutu:
    if minu_pakutu < a:
       minu_pakutu = int(input("Paku suurem arvu: "))
    elif minu_pakutu > a:
        minu_pakutu = int(input("Paku vaiksem arv: "))
if a == minu_pakutu:
        print ("WIN!!!")

