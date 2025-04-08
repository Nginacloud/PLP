import os

def read_and_modify_file(): 
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
        return

    # Modify the content
    modified_content = content.upper()

    # Extract filename only, not full path
    base_filename = os.path.basename(filename)
    new_filename = f"modified_{base_filename}"

    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{new_filename}'.")
    except IOError:
        print(f"Error: Could not write to '{new_filename}'.")

if __name__ == "__main__":
    read_and_modify_file()
