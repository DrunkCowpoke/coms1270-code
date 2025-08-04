# Trevor Bentley        8-3-2025
# Lab 11: FizzBuzz

# This code checks for repeats
# Replaces repeats with Fizz, Buzz, Bazz

# ----- divisable check -----
def fizzinbuzz(n):
    result = []
    for i in range(1, n + 1):
        word = ""
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"
        if i % 7 == 0:
            word += "Bazz"
        result.append(word if word else str(i))
    return result

#----- Rule book -----
def fizzbutt(n):
    result = []
    rules = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
    for i in range(1, n + 1):
        word = ""
        for key in rules:
            if i % key == 0:
                word += rules[key]
        result.append(word if word else str(i))
    return result

# ----- Input to List -----
def main():
    valu = int(input("Please enter a number: "))

    bingo1 = fizzinbuzz(valu)
    print("Modulus:", bingo1)

    bingo2 = fizzbutt(valu)
    print("Dictionary:", bingo2)

if __name__ == "__main__":
    main()