import os, sys
def tree(root, prefix=""):
    lines = []
    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name)
        lines.append(prefix + name)
        if os.path.isdir(path):
            lines.extend(tree(path, prefix + "  "))
    return lines
if __name__ == "__main__":
    print("\n".join(tree(sys.argv[1])))
