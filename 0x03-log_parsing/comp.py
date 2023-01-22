import difflib

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_text = f1.read()
        file2_text = f2.read()

    # Use the unified_diff function to get the differences
    # between the two files
    diff = difflib.unified_diff(file1_text.splitlines(), file2_text.splitlines())

    # Print out the differences
    for line in diff:
        print(line)

if __name__ == "__main__":
    compare_files('file1', 'file2')

