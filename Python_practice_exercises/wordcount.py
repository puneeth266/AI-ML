# wordcount.py

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = {}
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            return word_count

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python wordcount.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    word_count = count_words(filename)

    if word_count:
        for word, count in word_count.items():
            print(f"{word}: {count}")
