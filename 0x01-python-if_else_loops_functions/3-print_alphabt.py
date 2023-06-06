#!/usr/bin/python3
alph = 97
while alph <= 122:
    if alph == 101 or alph == 113:
        alph += 1
        continue
    print("{}".format(chr(alph)), end="")
    alph += 1
