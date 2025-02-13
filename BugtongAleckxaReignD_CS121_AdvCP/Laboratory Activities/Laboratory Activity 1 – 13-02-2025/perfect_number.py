num = int(input("Enter a number: "))

divisors_sum = 0

for i in range (1, num):
    if num % i == 0:
        divisors_sum += i
        
if divisors_sum == num:
    print (f"{num} is a perfect number.")
else:
    print (f"{num} is not a perfect number.")
  


    

    
