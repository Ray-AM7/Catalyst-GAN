import os
import numpy as np

def adjust_coordinates_in_file(file_path, min_x, min_y, min_z):
    adjusted_coordinates = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        first_line = lines[0]  # Keep the first line from the original file
        for line in lines[1:]:
            elements = line.split()
            element_name = elements[0]  # Retain the element name
            coordinates = list(map(float, elements[1:]))
            adjusted_x = coordinates[0] + abs(min_x)
            adjusted_y = coordinates[1] + abs(min_y)
            adjusted_z = coordinates[2] + abs(min_z)
            adjusted_coordinates.append((element_name, adjusted_x, adjusted_y, adjusted_z))
    return first_line, adjusted_coordinates

def adjust_coordinates_in_folder(folder_path, min_x, min_y, min_z, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(output_folder, filename)
            first_line, adjusted_coordinates = adjust_coordinates_in_file(file_path, min_x, min_y, min_z)
            with open(output_file_path, 'w') as f:
                f.write(first_line)  # Write the first line from the original file
                for coord in adjusted_coordinates:
                    f.write(f"{coord[0]} {coord[1]} {coord[2]} {coord[3]}\n")  # Write element name and adjusted coordinates

# Pre-defined minimum values for each dimension
min_x = int(np.ceil(abs(-6.46794654))) * -1
min_y = int(np.ceil(abs(-3.74461383))) * -1
min_z = 0

input_folder_path = 'S:/SmallBobbyAI/bulk-cartesian/'
output_folder_path = 'S:/SmallBobbyAI/cartesianAdjusted/'

adjust_coordinates_in_folder(input_folder_path, min_x, min_y, min_z, output_folder_path)
