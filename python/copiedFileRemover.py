import os
import sys
import re
from typing import List

def removeCopiedFiles(directoryPath: str, copiedFileMarkers: List[str]):
    print('-' * 50)
    print("Checking directory: ", directoryPath)
    nestedDirectories: List[str] = []
    files: List[str] = os.listdir(directoryPath)
    
    for file in files:
        full_path = os.path.join(directoryPath, file)
        if os.path.isdir(full_path):
            nestedDirectories.append(full_path)
        else:
            for marker in copiedFileMarkers:
                if re.search(marker, file):
                    original_file = re.sub(marker, '', file)
                    if original_file in files:
                        try:
                            os.remove(full_path)
                            print(f'Removed file "{full_path}"')
                        except OSError as e:
                            print(f'Error removing file "{full_path}": {e}')
                    break
    
    for directory in nestedDirectories:
        removeCopiedFiles(directory, copiedFileMarkers)

# Check if the user has passed the path
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.getcwd()

# Define copied file markers with regex patterns
copiedFileMarkers = [r' - Copie', r' - Copy', r'\(\d+\)']

removeCopiedFiles(path, copiedFileMarkers)
