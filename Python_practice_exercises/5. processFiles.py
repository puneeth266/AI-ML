import sys

def process_files(input_file_path, output_file_path):
    try:
        # Check if both input and output file paths are provided
        if not input_file_path or not output_file_path:
            raise ValueError("Both input and output file paths must be provided.")

        # Check if the input file exists
        try:
            with open(input_file_path, 'r') as input_file:
                # Read and process the input file content here
                content = input_file.read()
                # Perform your processing here (e.g., modify content)
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file '{input_file_path}' not found.")
        
        # Write the processed content to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(content)
        
        print(f"File processing completed. Result saved to '{output_file_path}'.")

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except FileNotFoundError as fe:
        print(f"Error: {fe}")
        sys.exit(1)
    except PermissionError:
        print("Error: Permission denied while writing to the output file.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if both input and output file paths are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python program.py <input_file_path> <output_file_path>")
        #sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    process_files(input_file_path, output_file_path)
