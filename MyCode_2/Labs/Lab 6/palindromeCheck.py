# Name: Trevor Bentley      7-9-2025
# Lab 6: Strings and things

# This Code checks for palindromes

# ----- I'm lazy so -----
import reverseString

# ----- Welcome to Flavor Town -----

# ----- Flavor 1 (V1) ------
# ----- Forward = Backword -----
def palindromeCheckV1(user_input):
    reversed_str = reverseString.reverseStringV1(user_input)
    return user_input == reversed_str

# ----- Flavor 2 (V2) -----
# ----- Beginning vs End -----
def palindromeCheckV2(user_input):
    length = len(user_input)
    for i in range(length // 2):
        if user_input[i] != user_input[length - 1 - i]:
            return False
    return True

# ----- Inputs / Main -----
def main():
    ui = input("Enter your suspected Palindrome")

    ans1 = palindromeCheckV1(ui)
    ans2 = palindromeCheckV2(ui)

    print("\n-=- Palindrome Check Results -=-")
    print(f"V1(Reverse String):{"Yep, thats a Palindrome" if ans1 else "Not a palindrome"}")
    print(f"V2(Mullet check):{"Yup, thats a Palindrome" if ans2 else "Not a palindrome"}")


# ----- cant for get the bow on top -----
if __name__ == "__main__":
    main()