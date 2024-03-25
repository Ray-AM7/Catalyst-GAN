import os
import re

def remove_brackets_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Remove brackets using regular expressions
    text_without_brackets = re.sub(r'\[|\]', '', text)
    
    with open(file_path, 'w') as file:
        file.write(text_without_brackets)

def remove_brackets_from_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.txt'):  # Process only text files
                file_path = os.path.join(root, file_name)
                remove_brackets_from_file(file_path)

# Replace 'folder_path' with the path to your folder containing text files
folder_path = 'S:/SmallBobbyAI/bulk-cartesian/'
remove_brackets_from_folder(folder_path)