#!/bin/bash
if [[ $3 == "--max_depth" ]]; then
    input_dir="$1"
    output_dir="$2"
    max_depth="$4"
else
    input_dir="$1"
    output_dir="$2"
    max_depth=""
fi
export input_dir output_dir max_depth
python3 collect_files.py
