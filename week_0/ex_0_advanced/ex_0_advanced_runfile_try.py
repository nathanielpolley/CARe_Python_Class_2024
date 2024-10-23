#YOUR CODE FOR EX_0 ADVANCED HERE
DNA=input("Enter a DNA string: ")

# Change to upper because it does not capture lowercase
uppercase_text = DNA.upper()

#Stablish conditions
bases=["A", "C", "G", "T"]

#Verification
verification=set(uppercase_text).issubset(bases)

if verification is False:
        print("not valid DNA string, only A,C,T or G accepted")
elif verification is True:
        # Measure string
        length = int(len(DNA))
        #For counting
        aden = "A"
        timin = "T"
        citos = "C"
        guan = "G"
        number_aden = int(uppercase_text.count(aden))
        number_timin = int(uppercase_text.count(timin))
        number_citos = int(uppercase_text.count(citos))
        number_guan = int(uppercase_text.count(guan))
        GC = (number_guan + number_citos) / (number_aden + number_guan + number_timin + number_citos) * 100
        print(f"The number of bases in your input DNA string is {length}.",
                  f"It is composed by {number_aden} adenosine, {number_timin} thymine, {number_citos} cytosine and {number_guan} guanine.",
                  f"The GC content of your string is {GC}%")