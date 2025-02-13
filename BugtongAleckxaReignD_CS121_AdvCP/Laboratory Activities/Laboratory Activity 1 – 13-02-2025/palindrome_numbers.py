num = int(input("Enter a number: "))

if num < 0:
    print ("Not a Palindrome")
else:
    original_num = num
    reversed_num = 0 


for i in range (10):
    if num == 0:
        break
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    num = num/10 - (last_digit/10)

if original_num == reversed_num:
    print ("Palindrome")
else:
    print ("Not a Palindrome")

   