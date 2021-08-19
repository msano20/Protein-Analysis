# -*- coding: utf-8 -*-
"""
Created on Mon May 31 13:11:28 2021
A simple script to calculate monoisotopic mass by organizing the principle masses of the amino acids into a dictionary.
"""

file = 'protein.fasta'

monoiso_mass = {
'A': 71.03711,
'C': 103.00919,
'D': 115.02694,
'E': 129.04259,
'F': 147.06841,
'G': 57.02146,
'H': 137.05891,
'I': 113.08406,
'K': 128.09496,
'L': 113.08406,
'M': 131.04049,
'N': 114.04293,
'P': 97.05276,
'Q': 128.05858,
'R': 156.10111,
'S': 87.03203,
'T': 101.04768,
'V': 99.06841,
'W': 186.07931,
'Y': 163.06333, 
}

def identify_format(file):
    with open(file, 'r') as f:
        
        prot = []
        header_count = 0
        for line in f:
            fasta_condition = line.startswith(">")
            if fasta_condition == False:
                try:
                    prot.append(line.strip('\n'))
                except StopIteration:
                    break
            elif fasta_condition == True:
                header_count += 1
 
    prot_combined = ''.join(prot)
    return prot_combined

def mass_calculation(prot_combined):
    mass_list = []
    for aa in prot_combined:
        for item in monoiso_mass:
            if aa in item:
                mass_list.append(monoiso_mass[item])
                
    #summing list elements:
    mass_sum = 0
    for mass in range(0, len(mass_list)):
        mass_sum += mass_list[mass]
    return mass_sum
                
def main(): 
    bare_seq = identify_format(file)
    p = mass_calculation(bare_seq)
    print(p)
    
if __name__ == "__main__":
    main()    
