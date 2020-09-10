import sys

def xor(a, b):
    return (a or b) and (not (a and b))
def binToBool(val):
    if val > 0:
        return True
    return False
def boolToBin(val):
    if val:
        return 1
    return 0
def bit(a, b, c):
    a = binToBool(a)
    b = binToBool(b)
    c = binToBool(c)
    suum = xor(a, xor(b, c))
    carry = xor(a, b) and c or (a and b)
    suum = boolToBin(suum)
    carry = boolToBin(carry)
    return suum, carry
def cushionZeros(strg, val):
    while len(strg) < val:
        strg = '0' + strg
    return strg
def nBit(a, b, n):
    aStr = str(a)
    bStr = str(b)
    for string in (aStr, bStr):
        for char in string:
            if char not in ('0', '1'):
                raise Exception(f'One of the numbers contains the character {char} which is not 0 or 1')
    aStr = cushionZeros(aStr, n)
    bStr = cushionZeros(bStr, n)
    sums = []
    carry = 0
    for val in range(n):
        suum, carry = bit(int(aStr[(n - 1) - val]), int(bStr[(n - 1) - val]), carry)
        sums.append(suum) 
    if binToBool(carry):
        return 'There was an overflow'
    numStr = ''
    for val in range(len(sums)):
        numStr += str(sums.pop())
    return int(numStr)
def main(a, b):
    n = max(len(str(a)), len(str(b))) + 1
    val = nBit(a, b, n)
    print((len(str(val)) - len(str(a))) * ' ' + f'   {a}\n+  ' + (len(str(val)) - len(str(b))) * ' ' +  f'{b}\n=  {val}') 
main(int(sys.argv[1]), int(sys.argv[2]))
