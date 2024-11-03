import os

def scan_directory(directory: str = None, output_file_name: str = None, ignored_items: tuple = None) -> str:
    """
    Scans the specified directory and writes its structure to a file.

    :param directory: Path to the directory to be scanned. If not specified, the current directory is used.
    :param output_file_name: Name of the file where the structure will be written. Default is 'directory_structure.txt'.
    :param ignored_items: List of files and directories to ignore during scanning.
                        Default is ('.git', '.idea', 'venv', '__pycache__').
    :return: Name of the file where the structure is written.
    """
    if output_file_name is None:
        output_file_name = 'directory_structure.txt'

    if ignored_items is None:
        ignored_items = ('.git', '.idea', 'venv', '__pycache__',)

    if directory is None:
        directory = "."

    with open(output_file_name, 'w') as f:
        for root, dirs, files in os.walk(directory):
            level = root.replace(directory, '').count(os.sep)
            indent = ' ' * 4 * level

            if any(ignore_item in root for ignore_item in ignored_items):
                continue

            basename = os.path.basename(root)
            f.write('{}{}/\n'.format(indent, basename))

            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                if any(ignore_item in file for ignore_item in ignored_items):
                    continue

                f.write('{}{}\n'.format(sub_indent, file))
    print("Directory structure was captured in file:", output_file_name)
    return output_file_name

def prettify_structure(output_file: str, spaces_to_trim: int, lines_to_trim: int):
    """
    Trims specified number of spaces and lines from the beginning of the file.

    :param output_file: The file to prettify.
    :param spaces_to_trim: Number of spaces to trim from the beginning of each line.
    :param lines_to_trim: Number of lines to trim from the beginning of the file.
    :return: None
    """
    with open(output_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines[lines_to_trim:]:
            f.write(line[spaces_to_trim:])
