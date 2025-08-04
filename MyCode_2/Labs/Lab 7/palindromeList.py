# Trevor Bentley        7-16-2025
# Lab 7 : Palindrome List sorter

# This code evaluates a list of strings to see if any are palindromes

# ----- Getting the Input set -----
def strInput():
    strList = []
    while True:
        item = input("Enter your string (Enter $ to stop):  ")
        if item == "$":
            break
        strList.append(item)
    return strList

# ----- The Palindrome checker -----
def tobeornottobe(I1):
    for i in range(len(I1)//2):
        if I1[i] != I1[-(i+1)]:
            return False
        
    return True

# ----- Main FXN -----
def main():
    words = strInput()
    result = tobeornottobe(words)
    print("Palindrome:", result)

if __name__ == "__main__":
    main()