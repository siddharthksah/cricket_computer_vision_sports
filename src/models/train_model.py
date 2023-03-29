import subprocess
import os

# Define the directory path
dir_path = '/home/sidd/Desktop/cricket_analysis/yolov5'

# Check if the directory exists
if not os.path.exists(dir_path):
    print(f"Error: Directory '{dir_path}' does not exist.")
    exit()

# Change the current working directory
os.chdir(dir_path)

# Confirm the current working directory has been changed
print(f"Current working directory: {os.getcwd()}")

# Define the command to train the model
train_cmd = [
    'python', 'train.py', 
    '--img', '416', 
    '--batch', '128', 
    '--epochs', '100', 
    '--data', '/home/sidd/Desktop/cricket_analysis/data/raw/cricket_dataset/data.yaml', 
    '--weights', 'yolov5x.pt'
]

# Open log file for writing
with open('/home/sidd/Desktop/cricket_analysis/train.log', 'w') as f:
    # Execute the command and capture the output
    with subprocess.Popen(train_cmd, stdout=f, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True) as p:
        # Wait for the process to finish and get the return code
        return_code = p.wait()

# Raise an exception if the return code is non-zero
if return_code != 0:
    raise RuntimeError(f'Training command failed with return code {return_code}')

# Print a message indicating success
print('Training completed successfully')


import re
# Open the train.log file for reading
with open('/home/sidd/Desktop/cricket_analysis/train.log', 'r') as f:
    # Read the contents of the file
    contents = f.read()

    # Find the first occurrence of "runs/train/exp" in the contents
    start_idx = contents.find('runs/train/exp')

    # Find the end of the sentence containing the occurrence
    end_idx = contents.find('.', start_idx) + 1

    # Extract the sentence containing the occurrence
    sentence = contents[start_idx:end_idx]

    # Use regular expression to find the experiment number
    exp_num = re.findall(r'exp(\d+)', sentence)[0]

    # Print the experiment number
    results_location = "/home/sidd/Desktop/cricket_analysis/yolov5/runs/train/exp" + exp_num
    print("Results saved in: " + results_location)
    
    # # Print the sentence
    # print(sentence)