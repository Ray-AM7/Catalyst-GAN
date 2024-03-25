import os
import shutil

def process_file(filename, min_values, max_values, min_files, max_files, count_gt_32, destination_folder):
    with open(filename, 'r') as file:
        next(file)  # Skip the first line
        for line_number, line in enumerate(file, start=1):
            if line_number == 1:  # Skip element name line
                continue
            coordinates = [float(coord) for coord in line.split()[1:]]  # Skip first element name
            for i, coord in enumerate(coordinates):
                if coord < min_values[i]:
                    min_values[i] = coord
                    min_files[i] = filename
                if coord > max_values[i]:
                    max_values[i] = coord
                    max_files[i] = filename
            if any(coord > 32 for coord in coordinates):
                count_gt_32[0] += 1
                move_file(filename, destination_folder)
                return

def move_file(filename, destination_folder):
    try:
        shutil.move(filename, destination_folder)
        print(f"Moved {filename} to {destination_folder}")
    except Exception as e:
        print(f"Error moving {filename}: {e}")

def find_extremes(folder, destination_folder):
    min_values = [float('inf')] * 3
    max_values = [float('-inf')] * 3
    min_files = [''] * 3
    max_files = [''] * 3
    count_gt_32 = [0]

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):  # Assuming all files have .txt extension
            filepath = os.path.join(folder, filename)
            process_file(filepath, min_values, max_values, min_files, max_files, count_gt_32, destination_folder)

    return min_values, max_values, min_files, max_files, count_gt_32[0]

folder_path = 'S:/SmallBobbyAI/cartesianAdjusted/'
destination_folder = 'S:/SmallBobbyAI/'

min_values, max_values, min_files, max_files, count_gt_32 = find_extremes(folder_path, destination_folder)

print("Smallest values:", min_values)
print("Smallest values found in files:", min_files)
print("Largest values:", max_values)
print("Largest values found in files:", max_files)
print("Number of files with values greater than 32:", count_gt_32)
