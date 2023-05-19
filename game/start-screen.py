import os
import time

print("1. start")
print("2. LICENSE")
print("3. quit")
print("4. info")

Q = int(input())


if(Q == 1):
    print("cat ball is starting")
    time.sleep(1)
    print("done")
    time.sleep(0.7)
    os.startfile('game.py')
    quit()

if(Q == 2):
    os.startfile("LICENSE.py")

if(Q == 3):
    quit()

if(Q == 4):
    pass