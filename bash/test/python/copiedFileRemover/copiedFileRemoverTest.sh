#!/bin/bash

# Function to create files and directories
create_files() {
  local base_path=$1
  mkdir -p "$base_path"

  # Files without copies
  touch "$base_path/file1.txt"
  touch "$base_path/file2.txt"
  touch "$base_path/file3.txt"

  # Files with copies (original and copy)
  touch "$base_path/file4.txt"
  touch "$base_path/file4 - Copy.txt"
  
  touch "$base_path/file5.txt"
  touch "$base_path/file5 - Copie.txt"

  touch "$base_path/file6.txt"
  touch "$base_path/file6.txt"

  touch "$base_path/file7.txt"
  touch "$base_path/file7(1).txt"

  # Files containing the marker but without the original
  touch "$base_path/file8 - Copy.txt"
  touch "$base_path/file9 - Copie.txt"
  touch "$base_path/file10.txt"
  touch "$base_path/file11(2).txt"

  # Create nested directories and files
  mkdir -p "$base_path/nested_dir1"
  touch "$base_path/nested_dir1/file12.txt"
  touch "$base_path/nested_dir1/file12 - Copy.txt"
  
  mkdir -p "$base_path/nested_dir2"
  touch "$base_path/nested_dir2/file13.txt"
  touch "$base_path/nested_dir2/file13 - Copie.txt"

  mkdir -p "$base_path/nested_dir3"
  touch "$base_path/nested_dir3/file14.txt"
  touch "$base_path/nested_dir3/file14.txt"
  
  mkdir -p "$base_path/nested_dir4"
  touch "$base_path/nested_dir4/file15.txt"
  touch "$base_path/nested_dir4/file15(1).txt"
}

# Check if a directory path is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <directory_path>"
  exit 1
fi

# Base directory path from argument
base_dir="$1"

# Remove the base directory if it exists
if [ -d "$base_dir" ]; then
  rm -rf "$base_dir"
fi

# Create files and directories
create_files "$base_dir"

echo "File structure created successfully at $base_dir."
