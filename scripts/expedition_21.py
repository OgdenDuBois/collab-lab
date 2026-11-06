import re, sys
def format_phone(raw):
    digits = re.sub(r"\D", "", raw)
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
if __name__ == "__main__":
    print(format_phone(sys.argv[1]))
