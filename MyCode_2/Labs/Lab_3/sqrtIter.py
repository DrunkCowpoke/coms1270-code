# Trevor Bentley      06-28-2025
# Lab Week 3 - This code gets the approximate sqrt of input value 

#----- Function(parent) -----
def sqrtIter(x, iterations):
    y = (x + 1) / 2  # Initial guess
    for _ in range(iterations):
        y = ((x / y) + y) / 2
    return y
#----- Main FXN (iterations) -----
def main():
    x = int(input("Enter a number to estimate the square root of: "))
    iterations = int(input("Enter the number of iterations to perform: "))
    answer = sqrtIter(x, iterations)
    print("The estimated square root is:", answer)

if __name__ == "__main__":
    main()