# Sequential Structure 5
import time
choose = int(input("To convert from centimeters to meters, type 1, to convert meters to centimeters type 2: "))
time.sleep(3)
if choose == 1:
    cm = int(input("Type the number to be converted: "))
    m = cm / 100
    print(cm, "centimeters equals to ", m, "meters")
elif choose == 2:
    m = int(input("Type the number to be converted: "))
    cm = m * 100
    print(m, "meters equals to ", cm, "centimeters")
else:
    print("Invalid code")