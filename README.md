# BinaryAdder
A module whose function's can calculate the sums, products, and powers of any two binary numbers and print them nicely to the screen. 
It is bootstrapped from only the and, or, and not gates typically available in assemblers, and here in python. 
I define an xor gate becuase it is not otherwise available without imports. 
Next I define a bit with three inputs and two outputs. The inputs include two digits of equal significance and a carry in from the next most significant digit. 
The input is three binary digits and it returns two binary digits.
The Truth tables are as follows: 
0,0,0 -> 0,0   
1,0,0/0,1,0/0,0,1 -> 1,0   
1,1,0/1,0,1/0,1,1 -> 0,1   
1,1,1 -> 1,1 
nBits uses n bits to add two binary numbers. It stores the carry of each bit for use in the next and checks its value for an overflow. 
The main function should be used to ovoid an overflow and print things nicely. 
mult multiplies two binary numbers by using nBits. It allocates enough bits to ovoid an overflow by considering the worse case (11...111 * 11...111 where both numbers are equal). 
Finally I define an exp method capable of calculating binary exponents of binary numbers using the mult function.
All numbers must be positive and large exponents are likely to take a very long time. The best way to do operations would be to convert to base ten, preform the arithmatic, and convert back. In priniciple this is how all computers preform arithmatic and it a very neat project in that regard. 
I made this by myself. You are free to go through my code and make changes, I only ask you share those changes with me. Enjoy :)!
