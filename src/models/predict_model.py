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
    
import os

# Set the locations of the weights and test images
weight_location = os.path.join(results_location, "weights/best.pt")
test_image_location = os.path.join("/home/sidd/Desktop/cricket_analysis/data/raw/cricket_dataset/test/images")

# Set the confidence threshold and image size
conf_threshold = 0.4
img_size = 416

# Build the command
command = [
    'python', 'detect.py', 
    '--weights', weight_location, 
    '--img', str(img_size),
    '--conf', str(conf_threshold), 
    '--source', test_image_location
]

try:
    # Execute the command and capture the output
    result = subprocess.run(command, capture_output=True, check=True, text=True)
    print(result.stdout)

except subprocess.CalledProcessError as e:
    print('Error:', e.stderr)
    
import os

# Set the directory path
dir_path = '/home/sidd/Desktop/cricket_analysis/yolov5/runs/detect'

# Get a list of all subdirectories
subdirs = [os.path.join(dir_path, d) for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]

# Sort the subdirectories by modification time
subdirs.sort(key=lambda x: os.path.getmtime(x))

# Print the latest subdirectory
latest_subdir = subdirs[-1]
print("Detections saved in the: ", latest_subdir)