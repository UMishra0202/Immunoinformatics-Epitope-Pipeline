import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument(
    "input_file",
    help="Input FASTA file"
)

args = parser.parse_args()

print("Generating peptides...")
subprocess.run([
    "python",
    "scripts/peptide_generator.py",
    args.input_file
])

print("\nScoring peptides...")
subprocess.run([
    "python",
    "scripts/peptide_scoring.py"
])

print("\nRanking peptides...")
subprocess.run([
    "python",
    "scripts/rank_peptides.py"
])

print("\nGenerating report...")
subprocess.run([
    "python",
    "scripts/epitope_report.py"
])

print("\nPipeline Complete")
