import os

def rename_images(image_directory):
    # List all files in the directory
    for filename in os.listdir(image_directory):
        if filename.endswith(".png"):  # Ensure we are only looking at PNG files
            # Remove the part starting from '_cannabis_bud' and convert to lower case
            new_name = filename.split('_cannabis_bud')[0].lower()
            # Replace dashes and spaces with underscores
            new_name = new_name.replace("-", "_").replace(" ", "_")
            # Add the file extension back
            new_name += '.png'
            # Construct the full old and new file paths
            old_file = os.path.join(image_directory, filename)
            new_file = os.path.join(image_directory, new_name)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_name}'")

# Specify the directory containing your images
image_directory = '.'  # Current directory; change to the path of your image directory
rename_images(image_directory)
