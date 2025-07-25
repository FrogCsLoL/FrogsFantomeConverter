import os
import sys
import zipfile
import shutil
from pathlib import Path

def create_fantome_from_folder(folder_path, output_dir=None):
    """
    Convert a folder to a .fantome file (which is just a renamed zip file)
    
    Args:
        folder_path: Path to the folder to convert
        output_dir: Directory to save the .fantome file (defaults to same directory as folder)
    """
    folder_path = Path(folder_path)
    
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Error: {folder_path} is not a valid directory")
        return False
    
    # Set output directory
    if output_dir is None:
        output_dir = folder_path.parent
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create fantome filename
    fantome_name = f"{folder_path.name}.fantome"
    fantome_path = output_dir / fantome_name
    
    try:
        # Create zip file with .fantome extension
        with zipfile.ZipFile(fantome_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through all files in the folder
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = Path(root) / file
                    # Calculate relative path from the folder being zipped
                    arcname = file_path.relative_to(folder_path)
                    zipf.write(file_path, arcname)
        
        print(f"✓ Created: {fantome_path}")
        return True
        
    except Exception as e:
        print(f"✗ Error creating {fantome_name}: {str(e)}")
        return False

def process_dropped_items(paths):
    """
    Process dropped folders/directories and convert their subfolders to .fantome files
    
    Args:
        paths: List of paths that were dropped onto the script
    """
    successful_conversions = []
    failed_conversions = []
    
    print(f"Processing {len(paths)} dropped item(s)...")
    
    for path_str in paths:
        path = Path(path_str)
        
        if not path.exists():
            print(f"✗ Path does not exist: {path}")
            failed_conversions.append(path)
            continue
        
        if path.is_file():
            print(f"⚠ Skipping file (only folders supported): {path.name}")
            continue
        
        if path.is_dir():
            print(f"\nProcessing main folder: {path.name}")
            print(f"Looking for subfolders to convert...")
            
            # Find all subdirectories in the dropped folder
            subfolders = [item for item in path.iterdir() if item.is_dir()]
            
            if not subfolders:
                print(f"  No subfolders found in {path.name}")
                continue
            
            print(f"  Found {len(subfolders)} subfolders:")
            for subfolder in subfolders:
                print(f"    - {subfolder.name}")
            
            # Convert each subfolder to .fantome
            for subfolder in subfolders:
                print(f"\n  Converting: {subfolder.name}")
                if create_fantome_from_folder(subfolder, path):  # Save .fantome in the main folder
                    successful_conversions.append(subfolder)
                else:
                    failed_conversions.append(subfolder)
    
    # Summary
    print(f"\n=== Conversion Summary ===")
    print(f"Successful: {len(successful_conversions)}")
    print(f"Failed: {len(failed_conversions)}")
    
    if failed_conversions:
        print("\nFailed conversions:")
        for folder in failed_conversions:
            print(f"  - {folder.name}")
    
    # Original folders are kept

def convert_all_folders_in_directory(directory, remove_original=False):
    """
    Convert all folders in a directory to .fantome files
    
    Args:
        directory: Path to the directory containing folders to convert
        remove_original: Whether to remove original folders after conversion
    """
    dir_path = Path(directory)
    
    if not dir_path.exists():
        print(f"Error: Directory {directory} does not exist")
        return
    
    print(f"Scanning directory: {dir_path}")
    
    # Find all subdirectories
    folders = [item for item in dir_path.iterdir() if item.is_dir()]
    
    if not folders:
        print("No folders found to convert")
        return
    
    print(f"Found {len(folders)} folders to convert:")
    for folder in folders:
        print(f"  - {folder.name}")
    
    print("\nStarting conversion...")
    
    successful_conversions = []
    failed_conversions = []
    
    for folder in folders:
        if create_fantome_from_folder(folder, dir_path):
            successful_conversions.append(folder)
        else:
            failed_conversions.append(folder)
    
    # Summary
    print(f"\n=== Conversion Summary ===")
    print(f"Successful: {len(successful_conversions)}")
    print(f"Failed: {len(failed_conversions)}")
    
    if failed_conversions:
        print("\nFailed conversions:")
        for folder in failed_conversions:
            print(f"  - {folder.name}")
    
    # Optionally remove original folders
    if remove_original and successful_conversions:
        print(f"\nRemoving original folders...")
        for folder in successful_conversions:
            try:
                shutil.rmtree(folder)
                print(f"✓ Removed: {folder.name}")
            except Exception as e:
                print(f"✗ Error removing {folder.name}: {str(e)}")

if __name__ == "__main__":
    print("=== Folder to Fantome Converter ===")
    print("Drag and drop folders onto this script or run it manually\n")
    
    # Check if items were dropped onto the script (command line arguments)
    if len(sys.argv) > 1:
        # Items were dropped onto the script
        dropped_paths = sys.argv[1:]
        print(f"Detected {len(dropped_paths)} dropped item(s)")
        print("Converting subfolders to .fantome files (original folders will be kept)...\n")
        
        process_dropped_items(dropped_paths)
    
    else:
        # Manual mode - ask for directory path
        print("Manual mode: Enter a directory path to convert all folders inside it")
        directory = input("Enter the directory path (or press Enter to exit): ").strip()
        
        if not directory:
            print("No path provided. Exiting.")
            exit(1)
        
        print("Converting folders to .fantome files (original folders will be kept)...\n")
        convert_all_folders_in_directory(directory, False)
    
