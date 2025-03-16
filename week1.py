def simple_interest(principal, rate, time):
    """Calculate simple interest"""
    amount = principal * (1 + (rate / 100) * time)
    return amount

def compound_interest(principal, rate, n, time):
    """Calculate compound interest"""
    amount = principal * (1 + rate / n) ** (n * time)
    return amount

def annuity_plan(payment, rate, n, time):
    """Calculate annuity plan"""
    r_n = rate / n
    amount = payment * (((1 + r_n) ** (n * time) - 1) / r_n)
    return amount

# Example usage
P = 1000  # Principal amount
R = 5     # Interest rate in percentage
T = 3     # Time in years
n = 12    # Compounded monthly
PMT = 200 # Monthly annuity payment

# Calculate results
si_result = simple_interest(P, R, T)
ci_result = compound_interest(P, R/100, n, T)
annuity_result = annuity_plan(PMT, R/100, n, T)

print(f"Simple Interest Amount: {si_result:.2f}")
print(f"Compound Interest Amount: {ci_result:.2f}")
print(f"Annuity Plan Amount: {annuity_result:.2f}")
