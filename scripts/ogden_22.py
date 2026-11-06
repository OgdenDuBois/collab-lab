import sys
MORSE = {"A": ".-", "B": "-...", "C": "-.-.", "S": "...", "O": "---", "E": ".", "H": "....", "L": ".-.."}
text = " ".join(sys.argv[1:]).upper() if len(sys.argv) > 1 else "SOS"
print(f"Text: {text}")
print("Morse: " + " ".join(MORSE.get(c, "?") for c in text if c != " "))
print("Done.")
