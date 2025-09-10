import os
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

selected_folder = None

def get_exif_date(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if not exif_data:
            return None

        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name in ["DateTimeOriginal", "DateTimeDigitized", "DateTime"]:
                try:
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
                except Exception:
                    pass
        return None
    except Exception:
        return None

def rename_images_in_folder(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        messagebox.showerror("Error", f"The path {folder} does not exist")
        return

    count = 0
    for file_path in folder.rglob("*.*"):
        if file_path.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            exif_date = get_exif_date(file_path)
            if not exif_date:
                exif_date = datetime.fromtimestamp(file_path.stat().st_mtime)

            new_name = exif_date.strftime("%Y-%m-%d_%H-%M-%S")
            counter = 1
            new_file_path = file_path.with_name(f"{new_name}{file_path.suffix.lower()}")

            while new_file_path.exists():
                new_file_path = file_path.with_name(f"{new_name}-{counter}{file_path.suffix.lower()}")
                counter += 1

            try:
                file_path.rename(new_file_path)
                count += 1
            except Exception as e:
                print(f"Error renaming {file_path}: {e}")

    messagebox.showinfo("Finished", f"{count} files were renamed.")

def choose_folder():
    global selected_folder
    folder = filedialog.askdirectory()
    if folder:
        selected_folder = folder
        label_var.set(f"Selected folder: {folder}")

def apply_changes():
    if not selected_folder:
        messagebox.showwarning("Warning", "No folder selected.")
        return
    rename_images_in_folder(selected_folder)

# --- GUI ---
root = tk.Tk()
root.title("Image Organizer by Date")
root.geometry("400x150")

label_var = tk.StringVar(value="No folder selected")
label = tk.Label(root, textvariable=label_var, wraplength=350)
label.pack(pady=10)

btn_choose = tk.Button(root, text="Choose Folder", command=choose_folder)
btn_choose.pack(pady=5)

btn_apply = tk.Button(root, text="Apply Changes", command=apply_changes)
btn_apply.pack(pady=5)

root.mainloop()
