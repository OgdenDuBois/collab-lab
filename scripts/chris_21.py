def with_tax(price, tax_percent):
    return price * (1 + tax_percent / 100)

def tax_amount(price, tax_percent):
    return price * tax_percent / 100

if __name__ == "__main__":
    print(f"Total with 8% tax on $50: ${with_tax(50, 8):.2f}")
    print(f"Tax amount: ${tax_amount(50, 8):.2f}")
