import RPi.GPIO as G
import time

dac = [10, 9, 11, 5, 6, 13, 19, 26]

dac.reverse()

G.setmode(G.BCM)

G.setup(dac, G.OUT)

def dec2bin(val):

    return[int(bit) for bit in bin(val)[2:].zfill(8)]

try:
    per = int(input())
    t = per/512

    while True:
        for i in range(255):
            G.output(dac, dec2bin(i))
            time.sleep(t)
        for i in range(255):
            G.output(dac, dec2bin(255-i))
            time.sleep(t)
        

finally:

    G.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])

    G.cleanup()