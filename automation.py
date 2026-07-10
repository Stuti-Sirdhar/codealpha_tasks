import os
import shutil

# Source and destination folders
source_folder = "source_images"
destination_folder = "moved_images"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files in source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("✅ All .jpg files moved successfully!")