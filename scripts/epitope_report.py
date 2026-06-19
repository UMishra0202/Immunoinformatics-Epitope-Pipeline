with open("results/ranked_peptides.txt", "r") as file:
    peptides = file.readlines()

top_peptides = peptides[:20]

with open("results/epitope_report.txt", "w") as report:

    report.write("Top Candidate Epitopes\n")
    report.write("=" * 30 + "\n\n")

    report.write("Rank\tPeptide\tScore\n")
    report.write("-" * 30 + "\n")

    rank = 1

    for line in top_peptides:

        peptide, score = line.strip().split("\t")

        report.write(f"{rank}\t{peptide}\t{score}\n")

        rank += 1

print("Epitope report generated.")
print("Output: results/epitope_report.txt")
