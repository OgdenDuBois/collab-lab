import hashlib, os, sys
from collections import defaultdict
def find_duplicates(root):
    seen = defaultdict(list)
    for dirpath, _, files in os.walk(root):
        for name in files:
            path = os.path.join(dirpath, name)
            with open(path, "rb") as f:
                seen[hashlib.md5(f.read()).hexdigest()].append(path)
    return {h: ps for h, ps in seen.items() if len(ps) > 1}
if __name__ == "__main__":
    print(find_duplicates(sys.argv[1]))
