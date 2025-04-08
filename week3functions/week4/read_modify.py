def read_and_modify_file():
    filename = r"C:\Users\USER\OneDrive\Documents\presentation.txt"

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
            print("\n✅ File read successfully! Here’s the content:\n")
            print(content)
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"❌ Error: The file '{filename}' could not be read.")
        return

    # Modify the content (e.g., make everything uppercase)
    modified_content = content.proper()

    # Create a modified filename
    new_filename = r"C:\Users\USER\OneDrive\Documents\modified_presentation.txt"
    
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"\n✅ Modified content written to '{new_filename}'.")
    except IOError:
        print(f"❌ Error: Could not write to '{new_filename}'.")

if __name__ == "__main__":
    read_and_modify_file()
