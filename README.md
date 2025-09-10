# rename-by-exif
# Photo Organizer by Date

This is a simple Python tool with a GUI (Tkinter) that renames images in a selected folder based on their EXIF creation date (or last modified time if EXIF data is missing).

Full Instructions for macOS:

# 1. Clone this repository:
git clone https://github.com/your-username/photo-organizer.git
cd photo-organizer

# 2. Check that Python 3 is installed:
python3 --version
# If Python is not installed, download it from https://www.python.org/downloads/

# 3. Install dependencies:
pip3 install pillow
# Tkinter is included by default on macOS.

# 4. Run the program:
python3 photo_organizer.py

# 5. Using the GUI:
# - Click "Choose Folder" (Select Folder) to choose the folder with your images.
# - The selected path will appear in the GUI below the button.
# - Click "Apply Changes" (Apply Changes) to rename all images in the folder based on their EXIF date.

Full Instructions for Windows:

# 1. Check that Python 3 is installed:
py --version
# If Python is not installed, download it from https://www.python.org/downloads/
# Make sure to check "Add Python to PATH" during installation.

# 2. Install dependencies:
py -m pip install pillow
# Tkinter is included by default with Python on Windows.

# 3. Run the program from source:
py rename_photos.py
# This will open the GUI where you can select a folder and apply changes.

# 4. Optional: Create a standalone executable (.exe) for easy distribution:
py -m pip install pyinstaller
py -m pyinstaller --onefile --noconsole rename_photos.py
# The .exe file will be generated in the "dist" folder.
# You can copy this .exe to any Windows computer and run it without installing Python.

# 5. Using the GUI:
# - Click "Choose Folder" (Select Folder) to choose the folder with your images.
# - The selected path will appear in the GUI below the button.
# - Click "Apply Changes" (Apply Changes) to rename all images in the folder based on their EXIF date.

# Notes:
# - Supported image formats: .jpg, .jpeg, .png
# - Files are renamed in the format: YYYY-MM-DD_HH-MM-SS
# - If a file with the same name already exists, a counter (-1, -2, …) is added automatically.
