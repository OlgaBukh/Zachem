import RPi.GPIO as G

import time

dac = [10, 9, 11, 5, 6, 13, 19, 26]

G.setmode(G.BCM)

G.setup(dac, G.OUT)

def dec2bin(val):

    return[int(bit) for bit in bin(val)[2:].zfill(8)]

def voltage(val):

    list = dec2bin(val)

    list.reverse()

    sum = 0

    for i in range(8):

        sum += list[i] * pow(2, i)

    max = pow(2, 8)

    return 3.3*sum/max

try:

    print("Enter number from 0 to 255:")

    num = input()

    if (num == 'q'):

        print("quitting...")

        quit()

    if num.isdigit() == False :

        print("not a number")

        quit()

    if (float(num) % 1 != 0) :

        print("is float")

        quit()

    num = int(num)

    if (num > 255) or (num < 0): 

        print("wrong range")

        quit()

    list = dec2bin(num)

    list.reverse()

    G.output(dac, list)

    print(voltage(num))

    time.sleep(2)

finally:

    G.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])

    G.cleanup()