import math

def heron(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

if __name__ == "__main__":
    print(heron(3, 4, 5))
