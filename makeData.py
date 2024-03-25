import numpy as np
import os
from periodictable import elements

def create_array(input_file):
    # Initialize 32x32x32 numpy array
    arr = np.zeros((32, 32, 32), dtype=int)

    # Read coordinates from the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()[1:]  # Skip the first line
        for line in lines:
            # Split the line into element symbol and coordinates
            element, x, y, z = line.split()
            x, y, z = map(float, (x, y, z))
            # Round down the coordinates and ensure they are within bounds
            x, y, z = int(np.clip(np.floor(x), 0, 31)), int(np.clip(np.floor(y), 0, 31)), int(np.clip(np.floor(z), 0, 31))
            # Get the atomic number
            atomic_number = elements.symbol(element).number
            # Mark the coordinate in the array with the atomic number
            arr[x, y, z] = atomic_number

    return arr


def main():
    input_dir = 'S:/SmallBobbyAI/cartesianAdjusted/'
    output_dir = 'S:/SmallBobbyAI/cartArrs/'

    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each input file
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.txt'):
            input_file = os.path.join(input_dir, file_name)
            output_file = os.path.join(output_dir, file_name.replace('.txt', '_arr.npy'))

            # Create the array
            arr = create_array(input_file)

            # Save the array as a NumPy .npy file
            np.save(output_file, arr)

if __name__ == "__main__":
    main()
