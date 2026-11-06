def split_bill(total, tip_percent, people):
    tip = total * tip_percent / 100
    return (total + tip) / people

if __name__ == "__main__":
    each = split_bill(120, 15, 4)
    print(f"Each person pays: ${each:.2f}")
    print(f"With no tip: ${120 / 4:.2f} each")
