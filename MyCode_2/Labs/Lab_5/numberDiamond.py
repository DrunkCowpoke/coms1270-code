# Trevor Bentley            7-6-2025
# Lab 5: This script prints a centered number diamond from the given row count? the crown jewel if you will

#  ----- the i of the storm
def diamond(num):

# ----- loop (outter) -----
    for i in range(1, num + 1):
        spaces = ' ' * (num - i)
        numbers = ' '.join(str(x) for x in range(1, i + 1))
        print(spaces + numbers)

# ----- Loop (inner) -----
    for i in range(num - 1, 0, -1):
        spaces = ' ' * (num - i)
        numbers = ' '.join(str(x) for x in range(1, i + 1))
        print(spaces + numbers)
# ----- the main man -----
def main():
    print("-1--2--3-- Number Diamond Generator --3--2--1-")
    rows = int(input("Enter the max belt size: "))
    diamond(rows)
    print("shiny and symmetrical.")

if __name__ == "__main__":
    main()
