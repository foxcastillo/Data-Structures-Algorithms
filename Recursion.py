# Edgar Barrera / Github: https://github.com/hellocastillo
# Copyright (c) 2021 Edgar Barrera

# Basic Recursion

def openRussiandoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussiandoll(doll-1)
        
# Bigger to Smaller (just like russian dolls)
