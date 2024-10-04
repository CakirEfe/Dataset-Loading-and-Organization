import os
import numpy as np
from scipy.signal import resample

# Function to resample the dataset
def resample_data(data, original_rate, target_rate):
    # Calculate the number of data points after resampling
    num_samples = int(len(data) * target_rate / original_rate)
    # Resample the data to match the target rate
    resampled_data = resample(data, num_samples)
    return resampled_data

# Define the source and target directories
source_folder = 'C:\\Users\\Efe\\Desktop\\HUST Zero csv\\'  # Path to your source folder containing the 51 kHz files
target_folder = 'C:\\Users\\Efe\\Desktop\\HUST Zero undersampled csv\\'  # Path to your target folder for 42 kHz files

# Ensure the target folder exists, if not, create it
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Define the original and target sampling rates
original_rate = 51200  # 51 kHz
target_rate = 42000  # 42 kHz

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.csv'):  # Process only CSV files
        # Construct the full file path
        file_path = os.path.join(source_folder, filename)

        # Load the 51 kHz dataset
        data_51khz = np.loadtxt(file_path, delimiter=',')

        # Resample the data
        data_resampled = resample_data(data_51khz, original_rate, target_rate)

        # Construct the full output file path
        output_file_path = os.path.join(target_folder, filename)

        # Save the resampled data to the new file in the target folder
        np.savetxt(output_file_path, data_resampled, delimiter=',')

        print(f"Resampled {filename} and saved to {output_file_path}")
