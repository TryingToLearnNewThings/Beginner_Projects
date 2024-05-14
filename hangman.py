import random

print("Hangman in python\n ------------")
print("Tipp: Es ist ein Tier\n")

somewords = """Hund Maus Katze Fuchs Pferd Kaninchen Vogel"""
somewords = somewords.split(" ")
ratewort = random.choice(somewords)
erraten = []
fehlversuche = 10
nutzereingabe = ""


for buchstaben in ratewort:
    erraten.append("_")

while nutzereingabe != "bye":
    for ausgabe in erraten:
        print(ausgabe, end=" ")
    print()
    nutzereingabe = input("Ihr Vorschlag:  ")
    x = 0
    for buchstaben in ratewort:
        if buchstaben.lower() == nutzereingabe.lower():
            print ("Treffer")
            erraten[x] = buchstaben
        x += 1
    print()
    #Kontrolle ob man gewonnen hat
    if "_" in erraten:
        fehlversuche -= 1
        print("Falcher Buchstabe. Du hast noch ", fehlversuche, " Versuche.")
        if fehlversuche == 0:
            print("Schade - Verloren!")
            break
    else:
        print("Gewonnen, das Wort war: ", ratewort)
        break
    