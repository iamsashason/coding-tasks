#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def to_rna(dna_strand): # Function to convert a DNA strand to its RNA complement.
    transcription = { # Dictionary mapping DNA nucleotides to their RNA complements.
        'G': 'C', 
        'C': 'G',
        'T': 'A',
        'A': 'U'
    } 
# The transcription dictionary maps each DNA nucleotide to its corresponding RNA nucleotide.
    return ''.join(transcription[nucleotide] for nucleotide in dna_strand) # Joins the RNA nucleotides into a single string and returns it.

def main(): # Main function to execute the program.
    dna = 'ACGTGGTCTTAA' # Example DNA strand to be converted.
    print(to_rna(dna)) # Expected result 'UGCACCAGAAUU' is printed to the console.

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.