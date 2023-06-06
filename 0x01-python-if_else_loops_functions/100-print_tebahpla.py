#!/usr/bin/python3
c = 0
for b in range(ord('z'), ord('a') - 1, -1):
    print(f"{chr(b - c)}", end="")
    c = 32 if c == 0 else 0
