print("enter the number:")

number = int(input())

divisor = []

for x in range ((number - (number - 2)), (number - 1)):
  
	if number % x == 0:
    
		divide = int(number/x)
    
		divisor.append(x)
print("the divisors of the entered number :")

print(divisor)
  