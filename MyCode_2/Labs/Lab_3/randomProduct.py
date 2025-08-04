# Trevor Bentley      06-28-2025
# Lab Week 3 - This code does random things with input a,b,c integers
import random

#-----function(parent)-----
def randomProduct(a, b, c):
    product = 1
    for _ in range(a):
        product *= random.randrange(b, c + 1)
    return product
#----- Use of Main FXN -----
def main():
    a = int(input("Enter how many random numbers to multiply (a): "))
    b = int(input("Enter the start of the range (b): "))
    c = int(input("Enter the end of the range (c): "))
    
    answer = randomProduct(a, b, c)
    print("The answer is:", answer)

if __name__ == "__main__":
    main()