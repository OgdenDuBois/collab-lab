def monthly_payment(principal, annual_rate, months):
    r = annual_rate / 12
    return principal * r / (1 - (1 + r) ** -months)

if __name__ == "__main__":
    print(round(monthly_payment(10000, 0.06, 36), 2))
