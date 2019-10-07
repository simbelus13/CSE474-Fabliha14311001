n = 4540866601440822
print("Example shown with a valid credit card number generated from the web, to input the n, simply replace line 1 with n = int(input())")
print()
c = []
while (n > 0):
    c.append( n % 10)
    n = int(n / 10)
print('\033[0;34m 1. Reversing the number, treating the number as an array of digits:')
print('\033[0;30m')
print(c)
print()
print('\033[0;34m 2. Doubling the value of even-indexed digits. If a doubled digit results in a number greater than 10, adding the two digits (e.g., the digit 6 becomes 12 and hence 1 + 2 = 3).')
print('\033[0;30m')
for i in range(1, len(c)):
  if i%2!=0:
    c[i]=c[i]*2
    if c[i]%10!=c[i]:
      c[i]=1+(c[i]%10)
print(c)
print()
print('\033[0;34m 3. Summing this modified array:')
sumC = sum(c)
print('\033[0;30m')
print (sumC)
print()
print('\033[0;34m 4. Credit Card Number Validity Check:')
if sumC%10==0:
  print("\033[0;32m Credit Card Number is Valid")
else:
  print("\033[0;31m Credit Card Number is Invalid")
