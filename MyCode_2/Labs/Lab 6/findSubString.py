# Name: Trevor Bentley      7-9-2025
# Lab 6: Strings and things

# This code pulls small strings out of bigger string, 3 ways

# ----- finders keepers -----
def findSubStringV1(ogString, sub_string):
    return ogString.find(sub_string)

# ----- indexed -----
def findSubStringV2(ogString, subString):
    if subString in ogString:
        return ogString.index(subString)
    else:
        return -1
    
# ----- the Rolo-dex -----
def findSubStringV3(ogString, subString):
    ogLen = len(ogString)
    subLen = len(subString)

    for i in range(ogLen - subLen + 1):
        match = True
        for j in range(subLen):
            if ogString[i + j] != subString[j]:
                match = False
                break
        if match:
            return i
    return -1

# ----- Main Migrane -----
def main():
    ogString = input("Enter the full string: ")
    subString = input("Enter the substring to search for: ")

    result1 = findSubStringV1(ogString, subString)
    result2 = findSubStringV2(ogString, subString)
    result3 = findSubStringV3(ogString, subString)


    print("\n--- String Search Result ---")
    print(f"V1(.find):{result1}")
    print(f"V2(.index):{result2}")
    print(f"V3(manual):{result3}")

# ----- Nombre -----
if __name__ == "__main__":
    main()