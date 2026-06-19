hydrophilic = "RKDEQN"

peptide = "RKDEQNRKK"

score = 0

for aa in peptide:
    if aa in hydrophilic:
        score += 1

print("Score:", score)
