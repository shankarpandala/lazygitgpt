import os
import glob
import json

def read_repository_contents(directory_path=os.getcwd(), file_pattern="*"):
    """
    Reads all files in the specified directory matching the file pattern,
    and creates a JSON object with file names and their contents.

    Args:
    directory_path (str): Path to the directory containing the files.
    file_pattern (str): Pattern to match files. Defaults to '*' (all files).

    Returns:
    str: A JSON string containing the file names and their contents.
    """
    data = {}
    for file_path in glob.glob(f"{directory_path}/{file_pattern}"):
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data[file_path] = file.read()
            except Exception as e:
                print(f"Error reading file: {file_path} - {e}")
    
    return json.dumps(data, indent=4)
