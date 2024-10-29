import os
import shutil

# Define target directory to sort (customize as needed)
TARGET_DIR = os.path.expanduser("~/Downloads")  # Change this to your target directory

# File categories and their extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Compressed": [".zip", ".rar", ".tar", ".gz", ".7z"]
}

def create_folders():
    """Create target folders if they do not exist."""
    for category in file_categories.keys():
        folder_path = os.path.join(TARGET_DIR, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files():
    """Move files to their corresponding category folders."""
    for filename in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR, filename)
        
        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()  # Get the file extension
            
            # Match file to a category
            for category, extensions in file_categories.items():
                if file_ext in extensions:
                    target_folder = os.path.join(TARGET_DIR, category)
                    shutil.move(file_path, target_folder)
                    print(f"Moved {filename} to {category}")
                    break

if __name__ == "__main__":
    create_folders()
    move_files()