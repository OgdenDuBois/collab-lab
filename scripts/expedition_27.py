import re, sys
from collections import Counter
def word_frequency(path):
    with open(path) as f:
        words = re.findall(r"[a-z0-9]+", f.read().lower())
    return dict(Counter(words).most_common(10))
if __name__ == "__main__":
    print(word_frequency(sys.argv[1]))
