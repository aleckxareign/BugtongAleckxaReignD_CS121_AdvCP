n = int(input("Enter the number of terms: "))

first_term = 0
second_term = 1

if n <= 0:
    print ("Please enter a positive number.")
elif n == 1:
    print (f"Fibonacci Series: {first_term}")
else:
    print (f"Fibonacci Series: {first_term} {second_term}", end=" ")
    
for i in range (n - 2):
    next_term = first_term + second_term
    print (next_term, end=" ")
    first_term = second_term
    second_term = next_term


  
