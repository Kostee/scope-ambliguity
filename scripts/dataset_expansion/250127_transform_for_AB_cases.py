import os
import csv

# Define constants for file naming and directories
COMBINATION_ID = "LETTET FOR COMBINATION"  # Set the first constant; A, B & C for three runs
EXAMPLES_NUM = '20'  # Set the second constant

INPUT_DIR = 'datasets/250127_chosen/before_AB_copying/'  # Path to the input directory
OUTPUT_DIR = 'datasets/250127_chosen/after_AB_copying/'  # Path to the output directory

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Construct input and output file paths
input_filename = f"combination{COMBINATION_ID}_{EXAMPLES_NUM}examples.csv"
output_filename = input_filename
input_filepath = os.path.join(INPUT_DIR, input_filename)
output_filepath = os.path.join(OUTPUT_DIR, output_filename)

# Open the input file for reading and the output file for writing
with open(input_filepath, mode='r', encoding='utf-8', newline='') as infile, \
     open(output_filepath, mode='w', encoding='utf-8', newline='') as outfile:
    
    # Read the input CSV file
    reader = csv.DictReader(infile)
    
    # Define the headers for the output file
    fieldnames = [
        'idx',
        'sentence',
        'Option A',
        'Option B',
        'gold_ans',
        'gold_scope_label',
        'OP1',
        'OP1_type',
        'OP2',
        'OP2_type'
    ]
    
    # Write the output file headers
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    # Process each row in the input file
    for row in reader:
        # First row: identical to the input
        output_row_a = {
            'idx': row['idx'],
            'sentence': row['sentence'],
            'Option A': row['Option A'],
            'Option B': row['Option B'],
            'gold_ans': row['gold_ans'],
            'gold_scope_label': row['gold_scope_label'],
            'OP1': row['OP1'],
            'OP1_type': row['OP1_type'],
            'OP2': row['OP2'],
            'OP2_type': row['OP2_type']
        }
        writer.writerow(output_row_a)
        
        # Second row: swap Option A and Option B, update gold_ans
        swapped_ans = 'B' if row['gold_ans'] == 'A' else 'A'
        output_row_b = {
            'idx': row['idx'],
            'sentence': row['sentence'],
            'Option A': row['Option B'],
            'Option B': row['Option A'],
            'gold_ans': swapped_ans,
            'gold_scope_label': row['gold_scope_label'],
            'OP1': row['OP1'],
            'OP1_type': row['OP1_type'],
            'OP2': row['OP2'],
            'OP2_type': row['OP2_type']
        }
        writer.writerow(output_row_b)

# Print completion message
print(f"Processed file: {input_filename}")
print("Transformation completed.")