def xor(a, b):
    return (a or b) and (not (a and b))
def bit(a, b, c):
    return int(xor(bool(a), xor(bool(b), bool(c)))), int(xor(bool(a), bool(b)) and bool(c) or (bool(a) and bool(b)))
def cushionZeros(strg, val):
    while len(strg) < val:
        strg = '0' + strg
    return strg
def nBit(a, b, n):
    'returns the sum of binary values a and b using n bits if there is no overflow and a message otherwise'
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
    if bool(carry):
        return 'There was an overflow'
    numStr = ''
    for val in range(len(sums)):
        numStr += str(sums.pop())
    return int(numStr)
def main(a, b):
    n = max(len(str(a)), len(str(b))) + 1
    val = nBit(a, b, n)
    print((len(str(val)) - len(str(a))) * ' ' + f'   {a}\n+  ' + (len(str(val)) - len(str(b))) * ' ' +  f'{b}\n=  {val}') 
def mult(a, b):
    'returns the product of a with b using nBit iteratively' 
    n = max(len(str(a)), len(str(b))) * 2
    i = 1
    val = a
    bBaseTen = 0
    power = 0
    for digit in reversed(str(b)):
        bBaseTen += 2 ** power * int(digit)
        power += 1
    while i < bBaseTen:
        val = nBit(val, a, n)
        i += 1
    return val
def mainMult(a, b):
    val = mult(a, b)
    print((len(str(val)) - len(str(a))) * ' ' + f'   {a}\nx  ' + (len(str(val)) - len(str(b))) * ' ' +  f'{b}\n=  {val}') 
def exp(a, b):
    'returns the product of a with b using nBit iteratively' 
    n = 1000 #max(len(str(a)), len(str(b))) * 2
    i = 1
    val = a
    bBaseTen = 0
    power = 0
    for digit in reversed(str(b)):
        bBaseTen += 2 ** power * int(digit)
        power += 1
    while i < bBaseTen:
        val = mult(val, a)
        i += 1
    return val
def mainExp(a, b):
    val = exp(a, b)
    print(f'{a}^{b} =  {val}') 
    
# Sample input:
# main(101, 11)  ## adds 101 + 11 with and, or, and not operations and prints the result
# mainMult(111, 10)  ## multiplies 111 * 10 through repetetive addition and prints the result
# mainExp(111, 100)  ## produces the result of 111^100 through repetetive multiplication and prints the result
