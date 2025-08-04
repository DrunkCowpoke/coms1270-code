# Trevor Bentley      06-28-2025
# Lab Week 3 - This code caculated accrued interest amounts based on the user inputs.

#----- Import Module -----
import math

def compoundAmount(principal, rate, compounds_per_year, time):
#--------------------------------------------------
# CITATION - URL: https://www.pearson.com/channels/college-algebra/asset/c5709b1e/use-the-compound-interest-formulas-to-solve-exercises-10-11-suppose-that-you-hav
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#--------------------------------------------------
    return principal * (1 + (rate / 100) / compounds_per_year) ** (compounds_per_year * time)

def main():
    principal = int(input("Enter principal: "))
    rate = int(input("Enter annual interest rate (%): "))
    compounds_per_year = int(input("Enter number of compounds per year: "))
    time = int(input("Enter time in years: "))
    result = compoundAmount(principal, rate, compounds_per_year, time)
    print("The compound amount is:", result)

if __name__ == "__main__":
    main()
