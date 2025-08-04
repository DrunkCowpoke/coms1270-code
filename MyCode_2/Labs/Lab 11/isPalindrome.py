# Trevor Bentley        8-3-2025
# Lab 11: Two sum

# This code checks palindromes with iteration and recursive techniques

# ----- iterative -----
def iterative(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# ----- Recursive -----
def recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return recursive(s[1:-1])

# ----- Main -----
def main():
    input_string = input("Please enter a string: ")

    yahtzee1 = iterative(input_string)
    print("Iterative:", yahtzee1)

    yahtzee2 = recursive(input_string)
    print("Recursive:", yahtzee2)

if __name__ == "__main__":
    main()