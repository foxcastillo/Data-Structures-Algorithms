# Edgar Castillo / Github: https://github.com/hellocastillo
# Copyright (c) 2021 Edgar Castillo

def sum(n):
    if n<=0:
        return 0
    else:
        return n + sum(n-1)
