"""
Enter a number to find all prime numbers up to and including that number."
"""

primeList = []

for num in range(2,int(input("Enter a number: "))):

    for i in range(2,int((num**0.5))+1):
    
        if num % i  == 0:
            break        
    else:
        primeList.append(num)


print(primeList)        