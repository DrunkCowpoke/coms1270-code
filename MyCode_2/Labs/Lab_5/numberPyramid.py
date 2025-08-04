# Trevor Bentley            7-6-2025
# Lab 5: This script prints a centered number pyramid based on input.

# ----- Thanks MatLab for this lift -----

def pyramid(num):
    for i in range(1, num + 1):
        spaces = ' ' * (num - i)
        numbers = ' '.join(str(x) for x in range(1, i + 1))
        print(spaces + numbers)
        
# ----- the main entree? -----

def main():
    print("-1-2-3-- Number Pyramid Generator --3-2-1-")
    num = int(input("Enter the number of pyramid rows: "))
    pyramid(num)
    print("et al")

if __name__ == "__main__":
    main()