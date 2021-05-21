# Edgar Barrera / Github: https://github.com/EdgarCastillo101/EdgarCastillo101
# Copyright (c) 2021 Edgar Barrera
def sum(n):
    if n<=0:
        return 0
    else:
        return n + sum(n-1)
