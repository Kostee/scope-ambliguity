#!/bin/bash

echo "Bash file started successfully"

# OpenAI API key
OPENAI_API_KEY="<type Open AI API key here>"

# Paths to input files and output directory
INPUT_DIR="datasets/250127_chosen/after_AB_copying"
OUTPUT_DIR="datasets/250127_expanded"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# List of input files
FILES=("combinationA_20examples.csv" "combinationB_20examples.csv" "combinationC_20examples.csv")

# Iterate over input files and run the script for each
for FILE in "${FILES[@]}"
do
    BASENAME=$(basename "$FILE" .csv)
    echo "Processing $BASENAME..."

    python scripts/dataset_expansion/exp1_dataset_expansion_250127.py \
        --openai-api-key "$OPENAI_API_KEY" \
        --source-dataset-filepath "$INPUT_DIR/$FILE" \
        --generated-data-directory "$OUTPUT_DIR" \
        --n-sampled 20 \
        --random-seed 1613

    echo "$BASENAME completed!"
done

echo "All data has been processed!"