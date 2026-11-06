def compound(principal, rate, years, n=12):
    return principal * (1 + rate / n) ** (n * years)

if __name__ == "__main__":
    print(round(compound(1000, 0.05, 3), 2))
