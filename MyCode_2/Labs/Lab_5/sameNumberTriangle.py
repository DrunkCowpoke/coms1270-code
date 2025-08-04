# Trevor Bentley            7-6-2025
# Lab 5: This script prints a triangle where each row repeats the same number


# ----- getting the telescope -----
def sameNumberTriangle(num):
    for i in range(1, num + 1):
        row = ' '.join([str(i)] * i)
        print(row)
#----- im out of main jokes -----
def main():
    print("=== Echo Generator: Triangle Edition ===")
    rows = int(input("Enter the largest number desired: "))
    sameNumberTriangle(rows)
    print("thats a wild stutter")

if __name__ == "__main__":
    main()
