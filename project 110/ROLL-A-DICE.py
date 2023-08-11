import random

roll_again = "y"

while  roll_again == "y" :
    no=random.randint(1,6)

       
    if no==1:
      print("[-----]")
      print("[--0--]")
      print("[-----]")
    if no==2:
      print("[0----]")
      print("[-----]")
      print("[----0]")
    if no==3:
      print("[0----]")
      print("[--0--]")
      print("[----0]")
    if no==4:
      print("[0---0]")
      print("[-----]")
      print("[0---0]")
    if no==5:
      print("[0---0]")
      print("[--0--]")
      print("[0---0]")
    if no==6:
      print("[0---0]")
      print("[0---0]")
      print("[0---0]")

    roll_again = input("Roll the Dices Again?")      