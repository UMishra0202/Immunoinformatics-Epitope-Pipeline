import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "input_file",
    help="Input FASTA protein sequence"
)

args = parser.parse_args()

sequence = ""

with open(args.input_file, "r") as fasta_file:
    for line in fasta_file:
        if not line.startswith(">"):
            sequence += line.strip()

print("Protein Length:", len(sequence))

peptides = []

for i in range(len(sequence) - 8):
    peptide = sequence[i:i+9]
    peptides.append(peptide)

print("Number of peptides:", len(peptides))

with open("results/peptides.txt", "w") as output_file:
    for peptide in peptides:
        output_file.write(peptide + "\n")

print("Peptides saved to results/peptides.txt")
