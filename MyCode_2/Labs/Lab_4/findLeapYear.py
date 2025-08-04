# Trevor Bentley                7-2-2025
# 
#lab 4: this code determines if the year input is a leap year


#----- FXN -----
def findLeapYear(yr):
    if yr % 4 != 0:
        return False
    elif yr % 100 != 0:
        return True
    elif yr % 400 == 0:
        return True
    else:
        return False
# ----- Main -----    
def main():
    yr=int(input("Enter a year: "))
    leapy= findLeapYear(yr)

    if leapy:
        print("YES")
    else:print("NO")

if __name__=="__main__":
    main()