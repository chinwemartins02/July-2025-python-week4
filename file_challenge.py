# File Read & Write Challenge with Error Handling

filename = input("Enter the filename to read: ")

try:
    # Try opening the file
    with open(filename, "r") as infile:
        content = infile.read()
        print("\nOriginal File Content:\n")
        print(content)

    # Modify the content (convert to uppercase)
    modified_content = content.upper()

    # Write modified content to output.txt
    with open("output.txt", "w") as outfile:
        outfile.write("=== MODIFIED CONTENT ===\n")
        outfile.write(modified_content)

    print("\nSuccess ✅: 'output.txt' has been created with the modified content!")

except FileNotFoundError:
    print(f"Error ❌: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error ❌: You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
