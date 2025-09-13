#number_analyzer

l1 =[]
total = 0
odd_sum = 0
even_sum = 0

value = int(input("Enter the number of values:"))

for i in range(value):
    N = int(input("Enter a number:"))
    total += N
    l1.append(N)
    
    if N % 2 == 0:
        even_sum += N
    else:
        odd_sum += N
    
max_num = max(l1)
min_num = min(l1)
average = total / value

print("the sum of even numbers is:",even_sum)
print("the sum of odd numbers is:",odd_sum)
print("the min value is:",min_num)
print("the max_value is:",max_num)
print("the average number is:",average)

