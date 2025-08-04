# Trevor Bentley                7-2-2025
# 
#lab 4: this code can solve for APR and Compounding interest

# -----Import Module -----
import math

# ----- APR FXN -----

def annualPercentageRate(rate, fees, p, ti):
#----------------------------------------------------------------------
# CITATION - URL:https://qualifications.pearson.com/content/dam/pdf/Functional-skills/teaching-support/Maths%20Level%202_Chapter%202%20Teacher%20Notes.pdf?
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: august 18 2010
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------------------------------------
    return ((rate + fees) / p) / ti * 100

def main():
    rate = int(input("Enter interest charges: "))
    fees = int(input("Enter fees: "))
    p = int(input("Enter loan amount: "))
    ti = int(input("Enter days in term: "))
    result = annualPercentageRate(rate, fees, p, ti)
    print("The APR is:", result)

if __name__ == "__main__":
    main()

# ----- Compound Amount FXN -----

def compoundAmount(p, rate, tx, ti):
#--------------------------------------------------
# CITATION - URL: https://www.pearson.com/channels/college-algebra/asset/c5709b1e/use-the-compound-interest-formulas-to-solve-exercises-10-11-suppose-that-you-hav
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: Unknown
# CITATION - Date Accessed: 2025-06-28
#--------------------------------------------------
    return p * (1 + (rate / 100) / tx) ** (tx * ti)

def main():
    p = int(input("Enter principal: "))
    rate = int(input("Enter annual interest rate (%): "))
    tx = int(input("Enter number of compounds per year: "))
    ti= int(input("Enter time in years: "))
    result = compoundAmount(p, rate, tx, ti)
    print("The compound amount is:", result)

if __name__ == "__main__":
    main()