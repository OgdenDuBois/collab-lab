import re, sys
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
def is_valid_email(addr):
    return bool(EMAIL_RE.match(addr))
if __name__ == "__main__":
    print(is_valid_email(sys.argv[1]))
