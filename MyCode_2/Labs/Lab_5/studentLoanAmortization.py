# Trevor Bentley            7-6-2025
#Lab 5: this code breaks a loan into monthly payments based on term, principle and interest rate

#----- Importing Module(s) -----

import math

# ----- thanks to rasberry pi i know this fancey move -----
"""
#----- Recalling Former Code to assist -----

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


# ----- Student Loan FXN -----
def studentLoanAmortization(Principle, apr, loan_length):
    # ----- For some reason I need this in decimal form to picture this -----
    monthlyrate = apr / 12 / 100
    months = int(loan_length * 12)

    if monthlyrate > 0:
        # ----- I drew a picture this formula should work -----
        monthlypayment = Principle * (monthlyrate * (1 + monthlyrate) ** months) / ((1 + monthlyrate) ** months - 1)
    else:
        monthlypayment = Principle / months

    balance = Principle

    # ----- here for the print -----
    print(f"\n{'Period':<8}{'Payment':<12}{'Interest':<12}{'Principal':<12}{'Balance':<12}")
    
    for period in range(1, months + 1):
        interest = balance * monthlyrate
        principal_paid = monthlypayment - interest
        balance -= principal_paid

        if balance < 0:
            balance = 0.0

        # ----- here for my ref f"{xyz=19.3} left align, xyz to 3 dec
        print(f"{period:<8}{monthlypayment:<12.2f}{interest:<12.2f}{principal_paid:<12.2f}{balance:<12.2f}")

# ----- The "main" event -----
def main():
    print("--- Student Loan Calculation ---")

    principal = float(input("Enter loan amount: "))
    apr = float(input("Enter annual interest rate (APR) as percent: "))
    loan_length = float(input("Enter loan duration (in years): "))
    compounds_per_year = int(input("Enter number of compounds per year (e.g., 12): "))

    #----- Compound part -----
    total_owed = compoundAmount(principal, apr, compounds_per_year, loan_length)

    print(f"\n[Compound Total]: ${total_owed:.2f}")

    #----- Amortization part -----
    print("\n--- Amortization Schedule ---")
    studentLoanAmortization(principal, apr, loan_length)

if __name__ == "__main__":
    main()
"""


# ----- should be the working model -----

# ----- Function thats getting nested -----

def studentLoanAmortization(principal, annual_rate, loan_years):
# ----- For some reason i cant figure out months as a whole number so -----
    monthly_rate = annual_rate / 12 / 100  
    months = int(loan_years * 12)

    if monthly_rate > 0:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        
    else:
        monthly_payment = principal / months
# ----- I broke the code somewhere this fixed it -----

    balance = principal


# ----- Structuring formulas -----

    print(f"\n{'Period':<8}{'Payment':<12}{'Interest':<12}{'Principal':<12}{'Balance':<12}")
    for period in range(1, months + 1):
        interest = balance * monthly_rate
        principal_paid = monthly_payment - interest
        balance -= principal_paid
        if balance < 0:
            balance = 0.0
        print(f"{period:<8}{monthly_payment:<12.2f}{interest:<12.2f}{principal_paid:<12.2f}{balance:<12.2f}")

# ----- the Main move -----

def main():
    print("$$$ Simple Student Loan Calculator $$$")
    principal = float(input("Enter loan amount ($): "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    loan_years = float(input("Enter loan duration (years): "))

    studentLoanAmortization(principal, annual_rate, loan_years)

if __name__ == "__main__":
    main()
