from random import randint


print("Willkommen zum Geisterspiel")
print(" Es gibt 3 Türen, wähle eine von diesen Türen und hoffe das sich der Geist nicht dahinter befindet")
print("====================================================================================================")

Geistertuer = True
score = 0

while Geistertuer:
    geist = randint(1, 3)
    print(" ")
    print("vor dir sind drei Türen")
    print("wähle eine davon aus.")
    tuer = input("1, 2 oder 3  ")
    tuer_nummer = int(tuer)
    if tuer_nummer == geist:
        print(tuer)
        print("Hinter der tür ist der GEIST")
        print("Lauf schnell weg")
        Geistertuer = False
    else:
        print("Der Geist ist nicht hinter der Tür")
        print("gehe eine Tür weiter.")
        score = score + 1

print(" ")
print("GAME OVER", score)

input("drück ENTER zum schließen")