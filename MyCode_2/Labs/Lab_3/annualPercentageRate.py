# Trevor Bentley      06-28-2025
# Lab Week 3 - This code caculated accrued interest amounts based on the user inputs.


#----- Module Import -----
import math

def annualPercentageRate(interest_charges, fees, loan_amount, days_in_term):
#----------------------------------------------------------------------
# CITATION - URL:https://qualifications.pearson.com/content/dam/pdf/Functional-skills/teaching-support/Maths%20Level%202_Chapter%202%20Teacher%20Notes.pdf?
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: august 18 2010
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------------------------------------
    return ((interest_charges + fees) / loan_amount) / days_in_term * 100

def main():
    interest_charges = int(input("Enter interest charges: "))
    fees = int(input("Enter fees: "))
    loan_amount = int(input("Enter loan amount: "))
    days_in_term = int(input("Enter days in term: "))
    result = annualPercentageRate(interest_charges, fees, loan_amount, days_in_term)
    print("The APR is:", result)

if __name__ == "__main__":
    main()
