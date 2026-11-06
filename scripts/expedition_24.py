import sys
UNITS = ["B", "KB", "MB", "GB", "TB"]
def human_size(n):
    n = float(n)
    i = 0
    while n >= 1024 and i < len(UNITS) - 1:
        n /= 1024
        i += 1
    return f"{n:.1f} {UNITS[i]}"
if __name__ == "__main__":
    print(human_size(sys.argv[1]))
