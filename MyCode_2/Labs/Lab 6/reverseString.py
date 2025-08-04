# Name: Trevor Bentley      7-9-2025
# Lab 6: Strings and things

# this code reverses strings in 5 flavors


# ----- Slice and Dice -----
def reverseStringV1(user_input):

    return user_input[::-1]

# ----- Reverse -----
def reverseStringV2(user_input):
    
    return ''.join(reversed(user_input))

# ----- Moon walk (-range) -----
def reverseStringV3(user_input):
    
    reversed_str = ""
    for i in range(len(user_input) - 1, -1, -1):
        reversed_str += user_input[i]
    return reversed_str

# ----- Premeditated -----
def reverseStringV4(user_input):
    
    reversed_str = ""
    for char in user_input:
        reversed_str = char + reversed_str
    return reversed_str

# ----- the Demon Loop -----
def reverseStringV5(user_input):
    
    reversed_str = ""
    index = len(user_input) - 1
    while index >= 0:
        reversed_str += user_input[index]
        index -= 1
    return reversed_str

# ----- The Main FXN -----
def main():
    user_input = input("Enter a string to reverse: ")

# ----- Establishing Control of Variables -----
    rev1 = reverseStringV1(user_input)
    rev2 = reverseStringV2(user_input)
    rev3 = reverseStringV3(user_input)
    rev4 = reverseStringV4(user_input)
    rev5 = reverseStringV5(user_input)

# ----- the Print Sector -----
    print("\n--- Reversed Strings ---")
    print(f"V1 (slice):        {rev1}")
    print(f"V2 (reversed()):   {rev2}")
    print(f"V3 (range loop):   {rev3}")
    print(f"V4 (for loop):     {rev4}")
    print(f"V5 (while loop):   {rev5}")

# ----- Fin -----
if __name__ == "__main__":
    main()
