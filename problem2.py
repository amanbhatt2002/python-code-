import os

def list_directory_contents(path="/"):
    try:
        files = os.listdir(path)
        print(f"Contents of '{path}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print("The specified directory does not exist.")
    except PermissionError:
        print("Permission denied to access this directory.")

# Example usage
list_directory_contents()  # Lists contents of the current directory
