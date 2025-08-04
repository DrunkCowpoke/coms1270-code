# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculated accrued interest amounts based on the user inputs.

# CITATION - URL: https://www.pearson.com/channels/college-algebra/asset/c5709b1e/use-the-compound-interest-formulas-to-solve-exercises-10-11-suppose-that-you-hav
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#--------------------------------------------------

#----- Import Module -----
import math

# -----Get Principal, Interest, Cpy, and time -----
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the interest rate (as a percentage): "))
compounds_per_year = int(input("Enter how many times it compounds per year: "))
time = int(input("Enter the time in years: "))

#----- Calc Accrued amount -----
accrued_amount = principal * (1 + (rate / 100) / compounds_per_year) ** (compounds_per_year * time)

#----- Output -----
print("The accrued amount is", accrued_amount, "dollars.")