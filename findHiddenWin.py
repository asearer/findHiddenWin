import os

def find_hidden_files(directory):
    # Get the list of files and folders in the directory
    files = os.listdir(directory)
    
    # Iterate over each file or folder
    for item in files:
        # Create the full path of the item
        item_path = os.path.join(directory, item)
        
        # Check if the item is hidden
        if is_hidden(item_path):
            print(f"Hidden item found: {item_path}")
        
        # Recursively search hidden items in subdirectories
        if os.path.isdir(item_path):
            find_hidden_files(item_path)

def is_hidden(item_path):
    # Check if the item path has a hidden attribute
    if os.name == 'nt':
        try:
            attrs = os.stat(item_path).st_file_attributes
            return attrs == (attrs | FILE_ATTRIBUTE_HIDDEN)
        except OSError:
            pass
    
    return False

# Windows-specific constants for hidden file attributes
FILE_ATTRIBUTE_HIDDEN = 0x02

# Example usage:
directory_path = r"C:\path\to\your\directory"
find_hidden_files(directory_path)
