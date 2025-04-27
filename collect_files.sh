#!/bin/bash
if [[ $3 == "--max_depth" ]]; then
    input_dir=$1
    output_dir=$2
    max_depth=$4
elif [[ $1 == "--max_depth" ]]; then
    max_depth=$2
    input_dir=$3
    output_dir=$4
else
    input_dir=$1
    output_dir=$2
    max_depth=$3
fi
export input_dir output_dir max_depth
python3 collect_files.py