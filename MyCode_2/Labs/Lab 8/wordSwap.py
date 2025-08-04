# Trevor Bentley        7-20-2025
# Lab 8 

# this code randomly swaps words form an available dictionary


# ----- Inport Module -----
import random

def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()

# ----- I am merriam webster -----
    swap_dict = {}
    for word in set(words):
        swap_dict[word] = random.choice(words)

# ----- Sentence formation -----
    swapped_sentence = ' '.join(swap_dict[word] for word in words)

    print(swap_dict)
    print(swapped_sentence)

# ----- Closing hymn -----

if __name__ == "__main__":
    main()