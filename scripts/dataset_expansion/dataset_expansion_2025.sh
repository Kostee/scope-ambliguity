#!/bin/bash

echo "Bash file started successfully"

# OpenAI API key
OPENAI_API_KEY="<type Open AI API key here"

# Paths to input files and output directory
INPUT_DIR="datasets/2025_chosen/after_AB_copying"
OUTPUT_DIR="datasets/2025_expanded"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# List of input files
FILES=("combinationA_10examples.csv" "combinationB_10examples.csv" "combinationC_10examples.csv")

# Iterate over input files and run the script for each
for FILE in "${FILES[@]}"
do
    BASENAME=$(basename "$FILE" .csv)
    echo "Processing $BASENAME..."

    python scripts/dataset_expansion/exp1_dataset_expansion_2025updated.py \
        --openai-api-key "$OPENAI_API_KEY" \
        --source-dataset-filepath "$INPUT_DIR/$FILE" \
        --generated-data-directory "$OUTPUT_DIR" \
        --n-sampled 20 \
        --n-generated 10 \
        --random-seed 1613

    echo "$BASENAME completed!"
done

echo "All data has been processed!"
