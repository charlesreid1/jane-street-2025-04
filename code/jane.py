import numpy as np
from scipy.optimize import fsolve

def equation(p):
    """
    Refined equation for p > 0.5 case
    P(A) = 3p^3 - 10p^2 + 12p - 4 = 0
    """
    # Our refined equation, set to 0 when P(A) = 1/2
    return 3*(p*p*p) - 10*(p*p) + 12*p - 4
    ###return p*(3/4) + 2*(1-p)/p - (1-p)/(p**2) - 1/2

def verify_solution(p):
    """Calculate P(A) directly to verify our solution"""
    # Calculate P(A₀)
    if p > 0.5:
        P_A0 = (2*p - 1)/p
    else:
        P_A0 = 0

    # Calculate P(A) in terms of P_A0 and p:
    P_A = (1-p)*(2-P_A0)*(P_A0) + (3/4)*p
    return P_A

# Initial guess - we know p is > 0.5
initial_guess = 0.6

# Solve the equation
solution = fsolve(equation, initial_guess)[0]

# Round to N decimal places
p_value = round(solution, 10)
print(f"The value of p is approximately: {p_value}")

# Verify the solution
P_A = verify_solution(solution)
print(f"Verification - P(A) with this p value: {P_A}")

# Binary search as secondary validation
def binary_search_for_p():
    """Find p using binary search in the interval [0.5, 1]"""
    low, high = 0.5, 1.0
    target = 0.50000000000000  # Target for P(A)
    epsilon = 1e-14  # Precision for convergence
    
    while high - low > epsilon:
        mid = (low + high) / 2
        P_A = verify_solution(mid)
        
        if P_A < target:
            low = mid
        else:
            high = mid
    
    return (low + high) / 2

# Find p using binary search
p_binary_search = binary_search_for_p()
p_value = round(p_binary_search, 10)
print(f"Result using binary search: {p_value}")
