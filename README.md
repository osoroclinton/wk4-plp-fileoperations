# wk4-plp-fileoperations
# File Processor with Error Handling

This Python program reads a file, applies a transformation to its content, and writes the modified version to a new file. It includes comprehensive error handling to manage issues that might occur during file operations.

## Features

- **File Read & Write**: Reads from an input file and writes modified content to a new file
- **Error Handling**: Gracefully handles multiple error cases:
  - File not found
  - Permission issues
  - Directory instead of file
  - Other unexpected errors
- **Multiple Transformation Options**:
  - Convert text to uppercase
  - Convert text to lowercase
  - Add line numbers
  - Remove blank lines
- **Interactive Interface**: User-friendly prompts and feedback
- **Preview Function**: Shows the first few lines of the transformed file

## Requirements

- Python 3.x

## Usage

1. Run the program:
   ```
   python fileop.py
   ```

2. Follow the interactive prompts:
   - Enter the input filename (must be a valid, readable file)
   - Enter the output filename
   - Choose a transformation to apply
   
3. The program will process the file and show a preview of the results

### Example Execution

```
Welcome to the File Processor!
This program reads a file, modifies its content, and saves to a new file.

Enter the name of the file to process: sample.txt
Enter the name for the output file: sample_transformed.txt

Choose a transformation to apply:
1. Convert to uppercase
2. Convert to lowercase
3. Add line numbers
4. Remove blank lines

Enter your choice (1-4): 3

Processing sample.txt...
Success! Processed content saved to 'sample_transformed.txt'.

Preview of the transformed file:
1: This is a sample text file.
2: 
3: It has some text on different lines.
4: 
5: Some lines are blank.
...
```


## How It Works

The program consists of three main functions:

1. `process_file()`: Handles the core file reading, transformation, and writing operations
2. `get_valid_filename()`: Ensures the user provides a valid, readable file
3. `main()`: Orchestrates the workflow and provides user interaction

The error handling is implemented using try-except blocks that catch specific exceptions and provide clear error messages to guide the user.
