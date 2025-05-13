def process_file(input_filename, output_filename, transformation_function):
    """
    Reads content from input file, applies a transformation function, and writes to output file.
    
    Args:
        input_filename (str): Path to the input file
        output_filename (str): Path to the output file
        transformation_function (function): Function to apply to each line of the file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Try to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.readlines()
        
        # Apply the transformation function to each line
        transformed_content = [transformation_function(line) for line in content]
        
        # Write the transformed content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.writelines(transformed_content)
            
        return True
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return False
    
    except PermissionError:
        print(f"Error: You don't have permission to access '{input_filename}'.")
        return False
    
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
        return False
    
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False

def get_valid_filename():
    """
    Prompts the user for a filename until they provide one that exists and is readable.
    
    Returns:
        str: Valid filename provided by the user
    """
    while True:
        filename = input("Enter the name of the file to process: ")
        
        try:
            # Try to open the file to verify it exists and is readable
            with open(filename, 'r') as f:
                # We successfully opened it, so it exists
                return filename
        
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")
        
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'. Please try again.")
        
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file. Please try again.")
        
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}. Please try again.")

def main():
    """
    Main function that orchestrates the file processing workflow.
    """
    print("Welcome to the File Processor!")
    print("This program reads a file, modifies its content, and saves to a new file.\n")
    
    # Get a valid input filename from the user
    input_filename = get_valid_filename()
    
    # Get an output filename
    output_filename = input("Enter the name for the output file: ")
    
    # Define transformation options
    print("\nChoose a transformation to apply:")
    print("1. Convert to uppercase")
    print("2. Convert to lowercase")
    print("3. Add line numbers")
    print("4. Remove blank lines")
    
    # Get user's choice with error handling
    while True:
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Define transformation functions
    if choice == 1:
        transformation = lambda line: line.upper()
        description = "uppercase"
    elif choice == 2:
        transformation = lambda line: line.lower()
        description = "lowercase"
    elif choice == 3:
        transformation = lambda i, line: f"{i+1}: {line}"
        # Adjust for line numbering which needs the index
        numbered_transformation = lambda lines: [transformation(i, line) for i, line in enumerate(lines)]
    elif choice == 4:
        transformation = lambda line: line if line.strip() else ""
        # Special handling for removing blank lines
        def remove_blanks(lines):
            return [line for line in lines if line.strip()]
    
    try:
        print(f"\nProcessing {input_filename}...")
        
        # Special handling for options that need the whole file at once
        if choice == 3:
            with open(input_filename, 'r') as input_file:
                content = input_file.readlines()
            
            transformed_content = numbered_transformation(content)
            
            with open(output_filename, 'w') as output_file:
                output_file.writelines(transformed_content)
            
            success = True
        elif choice == 4:
            with open(input_filename, 'r') as input_file:
                content = input_file.readlines()
            
            transformed_content = remove_blanks(content)
            
            with open(output_filename, 'w') as output_file:
                output_file.writelines(transformed_content)
            
            success = True
        else:
            # Standard line-by-line processing
            success = process_file(input_filename, output_filename, transformation)
        
        if success:
            print(f"Success! Processed content saved to '{output_filename}'.")
            
            # Show a preview of the transformed file
            print("\nPreview of the transformed file:")
            try:
                with open(output_filename, 'r') as f:
                    preview = f.readlines()[:5]  # Show first 5 lines
                    if preview:
                        for line in preview:
                            print(line.rstrip())
                        if len(preview) < 5:
                            print("(End of file)")
                        else:
                            print("...")
                    else:
                        print("(File is empty)")
            except Exception as e:
                print(f"Couldn't show preview: {str(e)}")
    
    except Exception as e:
        print(f"An error occurred during processing: {str(e)}")

if __name__ == "__main__":
    main()