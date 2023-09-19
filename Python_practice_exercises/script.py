import sys

def count_file_stats(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            word_count = len(content.split())
            line_count = len(content.splitlines())
            char_count = len(content)

            print(f"Word count: {word_count}")
            print(f"Line count: {line_count}")
            print(f"Character count: {char_count}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
else:
    file_path = sys.argv[1]
    count_file_stats(file_path)
