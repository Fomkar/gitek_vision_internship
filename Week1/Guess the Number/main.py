"""
Game Story:
    The UGM-27 Polaris is a nuclear missile designed in 1956–1960.
    One day Polaris get stuck at the launch point.
    A brave, smart and lucky soldier has to solve password of launch point.
    Otherwise, launch point and emplooyes will blow up.
    
Game Rule:
    The soldier has 5 chance to guess the password.
    
Password Trick:
    Computer can only generates number between 1 to 100.
"""

import time
from random import randint as generate_password

soldier_name = input("[Computer] Soldier Identity: ")
print("\t\t   Soldier Identity is Checking...")
time.sleep(2)
print("\t\t   Soldier Identity Confirmed...")

password = generate_password(1, 100)
chance = 5

def Boom(alert):
    countdown = 5
    print(alert + "\n\t\t   Countdown is starting...")
    while countdown > 0:
        print(f"\t\t   {countdown}...")
        countdown -= 1
        time.sleep(1)
    print("\nBOOOOOM!")
        

while True:
    if chance == 0:
        Boom("\n[Computer] All entered passwords rejected. Polaris is launching...")
        break
    else:
        try:
            guess = int(input("[Computer] Enter Password: "))
            time.sleep(1)
            if guess == password:
                print("\t\t   Password Confirmed. Launch is Aborted")
                break
            else:
                chance -= 1
                print("\t\t   Password Denied...")
                print(f"\t\t   Remaining Chance: {chance}")
                if chance != 0:
                    print(f"\t\t   {'Try Higher Values...' if guess < password else 'Try Lower Values...'}")
        except:
            Boom("\n[Computer] Wrong Format, Access Denied...")
            break