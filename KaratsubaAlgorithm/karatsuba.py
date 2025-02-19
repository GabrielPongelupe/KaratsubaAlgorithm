import unittest

def karatsuba(numberOne, numberTwo):
    if numberOne < 10 or numberTwo < 10:
        return numberOne * numberTwo
    
    maxLenght = max(len(str(numberOne)), len(str(numberTwo)))
    half = maxLenght // 2
    a = numberOne // (10 ** (half))
    b = numberOne % (10 ** (half))
    c = numberTwo // (10 ** (half))
    d = numberTwo % (10 ** (half))
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd

