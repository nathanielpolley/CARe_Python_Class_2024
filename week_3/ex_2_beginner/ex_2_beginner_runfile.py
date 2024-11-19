from Bio import SeqIO
from Bio.SeqUtils import gc_fraction, molecular_weight
import csv

class FastaParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse_file(self):
        sequences_data = []

        #Part of code that reads the content of the file and performs appropriate function
        for record in SeqIO.parse(self.file_name, "fasta"):
            # Extracting required information
            seq_name = record.id
            seq_description = record.description
            seq_length = len(record.seq)
            gc_content = gc_fraction(record.seq)*100
            mol_weight = molecular_weight(record.seq, seq_type='DNA')


            sequences_data.append({
                "Name": seq_name,
                "Description": seq_description,
                "Length": seq_length,
                "GC Content (%)": round(gc_content, 2),
                "Molecular Weight (g/mol)": round(mol_weight, 2)
            })

            # # Verify if the code is running uptil here
            # print(f"Name: {seq_name}, Description: {seq_description}, Length: {seq_length}, "
            #       f"GC Content: {gc_content:.2f}%, Molecular Weight: {mol_weight:.2f} g/mol")

        return sequences_data

    def data_to_csv(self, sequences_data, file_out): #function that writes data from previous file into csv
        with open (file_out, mode='w') as csvfile:
            fieldhead = ["Name","Description", "Length", "GC Content(%)", "Molecular Weight(g/mol)"]
            writer = csv.DictWriter(csvfile,fieldnames=fieldhead)
            writer.writeheader()
            writer.writerows(sequences_data)



if __name__ == "__main__":
    fasta_file = "sequences_beginner.fasta"
    output_csv = "ex_2_beginner_submit.csv"
    print("Job done Master!")

    parser = FastaParser(fasta_file)
    sequences_info = parser.parse_file()