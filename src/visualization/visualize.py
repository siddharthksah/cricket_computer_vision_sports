import matplotlib.pyplot as plt
import os
from PIL import Image
import numpy as np

# Define the directory path
dir_path = '/home/sidd/Desktop/cricket_analysis/data/raw/cricket_dataset/train/images/'

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(dir_path) if f.endswith('.jpg')]

# Load the first image in the list using Matplotlib
img = plt.imread(os.path.join(dir_path, image_files[0]))

# Display the image using Matplotlib
plt.imshow(img)
plt.show()

# Print the total number of images in the directory
print(f"Total number of images: {len(image_files)}")

# Initialize an empty list to store image heights and widths
heights = []
widths = []

# Loop through all images in the directory
for file in image_files:
    # Open the image using PIL.Image
    img = Image.open(os.path.join(dir_path, file))
    
    # Append the height and width to their respective lists
    width, height = img.size
    heights.append(height)
    widths.append(width)
    
# Calculate and print the average image height and width
avg_height = np.mean(heights)
avg_width = np.mean(widths)
print(f"Average image height: {avg_height:.2f}")
print(f"Average image width: {avg_width:.2f}")

# Plot a histogram of image heights
plt.hist(heights, bins=50, alpha=0.5, color='blue')
plt.axvline(avg_height, color='red', linestyle='dashed', linewidth=1)
plt.title('Image Heights')
plt.xlabel('Height')
plt.ylabel('Count')
plt.show()

# Plot a histogram of image widths
plt.hist(widths, bins=50, alpha=0.5, color='green')
plt.axvline(avg_width, color='red', linestyle='dashed', linewidth=1)
plt.title('Image Widths')
plt.xlabel('Width')
plt.ylabel('Count')
plt.show()

# Display a random image from the directory
rand_file = np.random.choice(image_files)
img = Image.open(os.path.join(dir_path, rand_file))
plt.imshow(img)
plt.title(f"Random Image: {rand_file}")
plt.axis('off')
plt.show()