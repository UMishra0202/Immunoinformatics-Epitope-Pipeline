hydrophilic = "RKDEQN"

with open("results/peptides.txt", "r") as file:
    peptides = file.readlines()

print("Peptides loaded:", len(peptides))


scores = []

for peptide in peptides:

    peptide = peptide.strip()

    score = 0

    for aa in peptide:

        if aa in hydrophilic:
            score += 1

	scores.append((peptide, score))

	print("Scores calculated:", len(scores))

	print(scores[:5])

	scores.sort(key=lambda x: x[1], reverse=True)

with open("results/ranked_peptides.txt", "w") as output:

    for peptide, score in scores:
        output.write(f"{peptide}\t{score}\n")

print("Top 10 Peptides:\n")

for peptide, score in scores[:10]:
    print(peptide, score)
