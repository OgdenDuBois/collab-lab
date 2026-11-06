def discounted_price(price, discount_percent):
    return price * (1 - discount_percent / 100)

def savings(price, discount_percent):
    return price - discounted_price(price, discount_percent)

if __name__ == "__main__":
    print(f"Price after 25% off $80: ${discounted_price(80, 25):.2f}")
    print(f"You save: ${savings(80, 25):.2f}")
