# Trevor Bentley        7-20-2025
# Lab 8 

#This code cleans a .txt file to a usable python format


# ----- Litteracy -----
def read_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents

# ----- Cleaning -----
def removeNonASCII(text):
    clean = ""
    for char in text:
        if ord(char) < 128:
            clean += char
    return clean

# ----- Rewrite -----
def write_clean_file(original_filename, clean_text):
    output_filename = original_filename.replace(".txt", "") + "_clean.txt"
    with open(output_filename, "w") as f:
        f.write(clean_text)

# ----- Main FXN -----
def main():
    filename = input("Enter the filename to clean (.txt file): ")
    try:
        file_text = read_file(filename)
        cleaned_text = removeNonASCII(file_text)
        write_clean_file(filename, cleaned_text)
        print(f"Cleaned file saved as {filename.replace('.txt', '')}_clean.txt")
    except FileNotFoundError:
        print("File not found, check directory.")

# ----- if name -----
if __name__ == "__main__":
    main()
