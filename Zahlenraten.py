from random import randint
n = randint(1, 100)

print("Zahlenrate spiel")
print("-----------------")

while True:
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht")
    versuch = int(input("Versuch diese Zahl zu erraten: "))
    if versuch == n:
        print(" ")
        print("Glueckwunsch, du hast die Zahl erraten.\nDie Zahl war %d\n" % n )
        break
    if versuch < n:
        print(" ")
        print("Zu Klein\n \n")
    if versuch > n:
        print(" ")
        print("Zu Gross\n \n")
    


P = input("Drueck ENTER zum schliessen")
