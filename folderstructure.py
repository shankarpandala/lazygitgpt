import os
from pathlib import Path

def create_folder_structure_md(path, indent=0):
    markdown = ""
    path = Path(path)
    if path.is_file() and not path.name.startswith('.') and path.name != 'folderstructure.py':
        markdown += "    " * indent + "- " + path.name + "\n"
    elif path.is_dir() and not path.name.startswith('.') and path.name != 'folderstructure.py':
        markdown += "    " * indent + "- " + path.name + "/\n"
        for child in path.iterdir():
            markdown += create_folder_structure_md(child, indent + 1)
    return markdown

# Replace 'your_directory_path' with the path of the directory you want to convert to markdown
print(create_folder_structure_md(os.getcwd()))
