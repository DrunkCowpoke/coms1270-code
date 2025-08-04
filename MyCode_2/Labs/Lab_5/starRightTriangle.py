# Trevor Bentley            7-6-2025
# Lab 5: code generates a right triangle of stars using input #

# ----- I've seen this somewhere before ----

def srt(num):
    for i in range(1, num + 1):
        print("*" * i)

# ----- The water main -----

def main():
    print("***** Star Triangle Generator *****")
    num = int(input("Enter the desired number of rows: "))
    srt(num)
    print("a real rise to star-dom")

if __name__ == "__main__":
    main()