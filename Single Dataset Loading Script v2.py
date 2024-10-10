import os
import pandas as pd

directory = 'C:\\Users\Efe\\Desktop\\UORED Labeled'
all_data = pd.DataFrame()
label_map = {}
label_index = 0

# Define a mapping for bearing conditions
condition_map = {
    'H': 'healthy',
    'I': 'inner_race_fault',
    'B': 'ball_fault',
    'O': 'outer_race_fault',
    'C': 'cage_fault'
}

# Function to extract condition and fault stage from filename
def extract_condition_and_stage(filename):
    parts = filename.split('_')  # Use underscores for splitting
    condition = parts[0]  # First part indicates the bearing condition
    stage = parts[2][0]  # Last part indicates the stage (0, 1, 2)

    # Map the condition
    if condition in condition_map:
        condition_label = condition_map[condition]
    else:
        condition_label = "unknown"

    # Map the stage to fault label
    if stage == '0':
        stage_label = 'healthy'
    elif stage == '1':
        stage_label = 'developing_fault'
    elif stage == '2':
        stage_label = 'faulty'
    else:
        stage_label = 'unknown'

    return f'{condition_label}_{stage_label}'

# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)

        # Load only the first column from the CSV
        data = pd.read_csv(filepath, usecols=[0])  # Use 'usecols' to load specific columns

        # Extract condition and fault stage from filename
        label = extract_condition_and_stage(filename)

        # Add new label to label_map if not already present
        if label not in label_map:
            label_map[label] = label_index
            label_index += 1

        # Add label as a new column in the DataFrame
        data['Label'] = label_map[label]

        # Concatenate the data from the current file to the complete DataFrame
        all_data = pd.concat([all_data, data], ignore_index=True)

print("Loaded and labeled data from all files.")
print(f"Label mapping: {label_map}")
