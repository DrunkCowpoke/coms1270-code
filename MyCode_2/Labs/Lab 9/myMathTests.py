# Trevor Bentley    7-24-2025
# Lab 9: myMathTests.py

# myMath code has issues and I'm attempting to test and fix it. 
# Edits are in myMath.py

# ----------------------- ADD FXN ----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------

# ----- Importing from myMath -----
from myMath import add

def testadd():
    assert add(5, 3) == 8
    assert add(3, -5) == -2
    assert add(-4, 4) == 0
# -----Passed test-----

# ----------------------- SUB FXN -------------------------------------000
# ----------------------- Pt. 1: Test-------------------------------------

# ----- Importing from myMath -----
from myMath import subtract

def testsub():
    assert subtract(5,3) == 2
    assert subtract(3,5) == -2
    assert subtract(4,4) == 0
# ----- Passed test -----

# ---------------------- MULT FXN ----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import multiply

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 5) == 0
# ----- passed test

# ---------------------- DIV FXN -----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import divide
def test_divide():
    assert divide(6, 3) == 2
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
# ----- passed test

# ---------------------- PWR FXN -----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import power
def test_power():
    assert power(2, 3) == 8
    assert power(3, 2) == 9
    assert power(5, 0) == 1
# ----- passed test

# ---------------------- FACTORIAL FXN -----------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(4) == 24
# ----- passed test

# ---------------------- PRIME FXN ---------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
# ----- passsed test


# ---------------------- SUM FXN -----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import sum_of_digits

def test_sum_of_digits():
    assert sum_of_digits(12) == 3
    assert sum_of_digits(35) == 8
    assert sum_of_digits(7) == 7
#----- passed test


# ---------------------- GCD FXN -----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import gcd

def test_gcd():
    assert gcd(8, 4) == 4
    assert gcd(9, 3) == 3
    assert gcd(5, 2) == 1
# ----- passed test

# ---------------------- FIB FXN -----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import fib

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(5) == 5
#----- pased test

# ----------------------- LCM FXN ----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import lcm

def test_lcm():
    assert lcm(2, 3) == 6
    assert lcm(4, 5) == 20
    assert lcm(6, 9) == 18
# ----- passed test


# ---------------------- SQRT FXN ----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import square_root

def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(1) == 1
# ----- passed test


# ---------------------- ABS-DIF FXN -------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import abs_diff

def test_abs_diff():
    assert abs_diff(7, 2) == 5
    assert abs_diff(2, 7) == 5
    assert abs_diff(4, 4) == 0
# ----- passsed test


# ---------------------- LOG FXN -----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import log

def test_log():
    assert round(log(10), 2) == 1
    assert round(log(8, 2), 2) == 3
    assert round(log(10, 10), 2) == 1
# ----- passed test


# ---------------------- MOD FXN -----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import mod

def test_mod():
    assert mod(9, 4) == 1
    assert mod(6, 3) == 0
    assert mod(7, 5) == 2
# ----- passed test

# ---------------------- MEAN FXN ----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import mean

def test_mean():
    assert mean([1, 2, 3]) == 2
    assert mean([4, 4, 4]) == 4
    assert mean([2, 4, 6, 8]) == 5
# ----- passed test

# ---------------------- MEDIAN FXN --------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import median

def test_median():
    assert median([1, 3, 2]) == 2
    assert median([2, 4, 1, 3]) == 2.5
    assert median([5, 5, 5]) == 5
# ----- passed test

# ---------------------- MODE FXN-----------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import mode

def test_mode():
    assert mode([1, 2, 2, 3]) == 2
    assert mode([4, 4, 1, 1, 4]) == 4
    assert mode([3, 3, 3, 2]) == 3
# ----- passed test


#-------------------------------------------------------------------------
#----- FAILURES ----------------------------------------------------------
#-------------------------------------------------------------------------

# ---------------------- METRIC2IMPERIAL FXN -----------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(5) == 41
    assert celsius_to_fahrenheit(10) == 50
# ----- Failed test

# ---------------------- IMPERIAL2METRIC FXN -----------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import fahrenheit_to_celsius

def test_fahrenheit_to_celsius():
    assert round(fahrenheit_to_celsius(32), 2) == 0
    assert round(fahrenheit_to_celsius(50), 2) == 10
    assert round(fahrenheit_to_celsius(41), 2) == 5
# ----- Failed test

# ------------------------------------------------------------------------
# ----- FAILURES ---------------------------------------------------------
# ------------------------------------------------------------------------


# ---------------------- INVERSE FXN -------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import inverse

def test_inverse():
    assert inverse(2) == 0.5
    assert inverse(4) == 0.25
    assert inverse(1) == 1
# ----- passed test

# ---------------------- TRINO FXN ---------------------------------------
# ----------------------- Pt. 1: Test-------------------------------------
from myMath import triangular_number

def test_triangular_number():
    assert triangular_number(1) == 1
    assert triangular_number(3) == 6
    assert triangular_number(5) == 15
# ----- passed test

