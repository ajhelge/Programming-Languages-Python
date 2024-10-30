import math

base, low = 0, 0
high = 10000
mid = (high + low) / 2

base = float(input("Please input a number between 0 - 10000: "))#GATHER INPUT


def FindSqrRt(base, high, mid, low):
    root = mid * mid
    while not math.isclose(root, base, rel_tol=1e-09, abs_tol=0):#use math.isclose() to compare floats
        root = mid * mid

        if(root) < base: #if guess is less than base, move low up, recalibrate the middle variable.
            low = mid
            mid = (high + low) / 2

        elif(root) > base: #if guess is greater than base, move high down, recalibrate the middle variable.
            high = mid
            mid = (high + low) / 2

    print("----------> ", round(mid, 2)) #round the final value to prevent the square root of 25 from being 4.999. (it should be 5)


FindSqrRt(base, high, mid, low)

