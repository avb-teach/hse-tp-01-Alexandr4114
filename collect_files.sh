#!/bin/bash
input_dir=$1
output_dir=$2
max_depth=$3
export input_dir output_dir max_depth
python3 collect_files.py