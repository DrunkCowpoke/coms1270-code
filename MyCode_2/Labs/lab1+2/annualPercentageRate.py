# Trevor Bentley      06-28-2025
# Lab Week 2 - This code caculated accrued interest amounts based on the user inputs.

# CITATION - URL:https://qualifications.pearson.com/content/dam/pdf/Functional-skills/teaching-support/Maths%20Level%202_Chapter%202%20Teacher%20Notes.pdf?
# CITATION - Author: Pearson Education, Inc.
# CITATION - Date Written/Posted: august 18 2010
# CITATION - Date Accessed: 2025-06-28
#----------------------------------------------------------------------

#----- Module Import -----
import math

#----- Get interest, fees, loan amt,and days-----
interest_charges = int(input("Enter the interest charges: "))
fees = int(input("Enter the fees: "))
loan_amount = int(input("Enter the loan amount: "))
days_in_term = int(input("Enter the number of days in the loan term: "))

#----- Calc APR -----
apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100

#----- Output -----
print("The annual percentage rate (APR) is", apr, "percent.")