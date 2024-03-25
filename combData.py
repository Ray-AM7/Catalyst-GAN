import numpy as np
import os

def load_3d_array(file_path):
    # Load a 3D array from a file
    return np.load(file_path)

def prepare_dataset(input_dir, output_file):
    # Load all 3D arrays from separate files
    arrays = []
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.npy'):
            array = load_3d_array(os.path.join(input_dir, file_name))
            arrays.append(array)

    # Combine arrays into a single array
    dataset = np.stack(arrays, axis=0)

    # Save the combined dataset
    np.save(output_file, dataset)

def main():
    input_dir = 'S:/SmallBobbyAI/cartArrs/'
    output_file = 'S:/SmallBobbyAI/combined_dataset.npy'

    # Prepare and save the dataset
    prepare_dataset(input_dir, output_file)

if __name__ == "__main__":
    main()
