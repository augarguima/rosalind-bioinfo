import sys
from collections import Counter

# lê arquivo passado no terminal
file_path = sys.argv[1]

with open(file_path) as f:
    s = f.read().strip()

# conta bases automaticamente
counts = Counter(s)

print(
    counts["A"],
    counts["C"],
    counts["G"],
    counts["T"]
)
