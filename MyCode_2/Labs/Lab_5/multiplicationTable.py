# Trevor Bentley            7-6-2025
# Lab 5: This script generates a multiplication table between two integers.

def multiplicationTable(lowNum, highNum):

# ---- might be a header might be a mess -----
    header = ''
    for i in range(lowNum, highNum + 1):
        header += str(i).rjust(4)
    print(header)


# ----- Just like corn heres rows -----
    for row in range(lowNum, highNum + 1):
        line = ''
        for col in range(lowNum, highNum + 1):
            line += str(row * col).rjust(4)
        print(line)

#----- the Main attraction

def main():
    print("--- Multiplication Table-anator ---")
    low = int(input("Enter the smaller number: "))
    high = int(input("Enter the larger number: "))

    if low > high:
        print("Fair Warning I am Swapping values so the low comes first.")
        low, high = high, low

    multiplicationTable(low, high)

    print("ta-dah")

# ----- the closing Statements -----

if __name__ == "__main__":
    main()
