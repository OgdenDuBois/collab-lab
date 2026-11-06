def monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 100 / 12
    n = years * 12
    return principal * monthly_rate * (1 + monthly_rate) ** n / ((1 + monthly_rate) ** n - 1)

if __name__ == "__main__":
    payment = monthly_payment(200000, 5.0, 30)
    print(f"Monthly payment: ${payment:.2f}")
    print(f"Total paid: ${payment * 360:.2f}")
