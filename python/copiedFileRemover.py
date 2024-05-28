import os
import sys
import re
from typing import List

copiedFileMarkers: List[str] = []

def removeCopiedFiles(directoryPath: str):
    print('-' * 50)
    print("Checking directory: ", directoryPath)
    nestedDirectories: List[str] = []
    files: List[str] = os.listdir(directoryPath)
    for file in files:
        full_path = os.path.join(directoryPath, file)
        print(f'Checking file "{file}"')
        if os.path.isdir(full_path):
            print("Found directory: ", full_path)
            nestedDirectories.append(full_path)
            continue
        for marker in copiedFileMarkers:
            print(f'Checking marker "{marker}" for file "{file}"')
            if re.search(marker, file):
                markerCount = len(re.findall(marker, file))
                for _ in range(markerCount):
                    original_file = re.sub(marker, '', file)
                print(f'Found marker "{marker}" {markerCount} times in file "{file}"')
                print(f'Assumed original file name: "{original_file}"')
                if original_file in files:
                    print(f'Found original file "{original_file}" in the same directory')
                    try:
                        os.remove(full_path)
                        print(f'Removed file "{full_path}"')
                    except Exception as e:
                        print(f'Error removing file "{full_path}": {e}')
    
    for directory in nestedDirectories:
        removeCopiedFiles(directory)

# Check if the user has passed the path
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.getcwd()

# Define copied file markers with regex patterns
copiedFileMarkers = [r' - Copie', r' - Copy', r'\(\d+\)']

removeCopiedFiles(path)
