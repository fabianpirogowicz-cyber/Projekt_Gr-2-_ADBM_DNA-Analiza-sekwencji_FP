from Bio import Entrez

Entrez.email = "twoj_email@example.com"

def fetch_sequence(accession):
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
    data = handle.read()

    sequence = "".join(data.split("\n")[1:])
    return sequence