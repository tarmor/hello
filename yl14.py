text = "Mu isamaa mu õnn ja rööm...."
th = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
count = 0
for item in text:
    if item in th:
        count = count + 1
        print (item)
print ("Tekstis on " + str (count) + " täishäälikut.") 

