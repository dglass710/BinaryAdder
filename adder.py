def xor(a, b):
    return (a or b) and (not (a and b))
def binToBool(val):
    'Converts a binary value to a boolean'
    if val > 0:
        return True
    return False
def boolToBin(val):
    'Converts a boolean value to a binary'
    if val:
        return 1
    return 0
def bit(a, b, c):
    '''takes three inputs and returns two outputs
    suum is 1 if 1 or 3 of the inputs are 1 and 0 otherwise
    carry is 1 if 2 or 3 of the inputs are 1 and 0 otherwise'''
    a = binToBool(a)
    b = binToBool(b)
    c = binToBool(c)
    suum = xor(a, xor(b, c))
    carry = xor(a, b) and c or (a and b)
    suum = boolToBin(suum)
    carry = boolToBin(carry)
    return suum, carry
def cushionZeros(strg, val):
    '''takes a string representing a binary number and
    an integer specifying the desired number of digits
    It puts zeros at the begining of the string until len(strg) == val'''
    while len(strg) < val:
        strg = '0' + strg
    return strg
def nBit(a, b, n):
    '''nBits first checks to make sure a and b are binary
    Next it calls cushionZeros on a and b so they both contain n digits
    It then calls bit n times using the carry of the previous bit for the current one
    It also appends the value of suum to sums from least to most significant
    After checking for an overflow by looking at the final value of carry,
    each value from sums is popped off, cast to a str, and concatonated to numStr from most to least significant
    Finally numStr is cast to an int and returned'''
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
    'Determines the largest number of bits needed and uses nBits to add a to b and cleanly print everything to the terminal'
    n = max(len(str(a)), len(str(b))) + 1
    val = nBit(a, b, n)
    print((len(str(val)) - len(str(a))) * ' ' + f'   {a}\n+  ' + (len(str(val)) - len(str(b))) * ' ' +  f'{b}\n=  {val}') 

## Example Usage:
# main(110101, 10110)
## Expected Output:
#     110101
# +    10110
# =  1001011
