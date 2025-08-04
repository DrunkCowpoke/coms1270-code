# Trevor Bentley        8-3-2025
# Lab 11: Reverse String

# This code nReverses a str via iteration and recursive methods


# ----- iterative -----
def riterative(s):
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string

# ----- Recursive -----
def rrecursive(s):
    if len(s) <= 1:
        return s
    return rrecursive(s[1:]) + s[0]
# ----- main -----
def main():
    pistachio = input("Please Enter a String: ")

    walnut1 = riterative(pistachio)
    print("Iterative:", walnut1)

    walnut2 = rrecursive(pistachio)
    print("Recursive:", walnut2)

# ----- main recall -----
if __name__ == "__main__":
    main()