# Trevor Bentley        7-20-2025
# Lab 8 

#This code cleans a .txt file analyze book.txt files


# ----- Cleaner -----
import string

def clean_word(word):
    return word.strip(string.punctuation)

# ----- Analytics -----
def analyzeBook(filename):
    count = {}
    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                word = clean_word(word)
                if word.isalpha():
                    word = word.lower()
                    count[word] = count.get(word, 0) + 1
    return count

# ----- outro -----
def outputAnalysis(counts, filename):
    title = filename.replace(".txt", "")
    output_file = title + "_analysis.txt"
    with open(output_file, "w") as out:
        for word in sorted(counts.keys()):
            out.write(word + " " + str(counts[word]) + "\n")

# ----- Main FXN -----
def main():
    filename = input("Enter the name of the book file: ")
    try:
        counts = analyzeBook(filename)
        outputAnalysis(counts, filename)
        print(f"Analysis saved to {filename.replace('.txt', '')}_analysis.txt")
    except FileNotFoundError:
        print("File not found. Please check your filepath.")

# ----- Main reroute -----
if __name__ == "__main__":
    main()
