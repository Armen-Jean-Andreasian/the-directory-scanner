## The Directory Scanner

The Directory Scanner is a Python library designed to simplify the process of scanning directory structures and generating a comprehensive list of files and folders. It provides a convenient way to recursively traverse directories, ignoring specific files and folders specified by the user.

![](cover.jpg)
### Features:
- Recursively scan directories and subdirectories to generate a structured list of files and folders.
- Exclude specific files and folders from the scan using an ignore list.
- Supports customization of the output format to suit different needs.

### Usage:
1. Install the library using pip:
    ```
    pip install the-directory-scanner
    ```

2. Import the `scan_directory` function from the library and use it to scan a directory:
    ```python
   from the_directory_scanner import scan_directory
   
   scan_result = scan_directory(directory=".", output_file_name="directory_structure.txt",
                                ignored_items=('.git', '.idea', 'venv', '__pycache__',))
    ```
3. Access the generated directory structure in the output file (`directory_structure.txt` in this example) to view the results.

4. If you wish to modify the structure, import `prettify_structure` function and provide the path to generated file:
   ```python
   from the_directory_scanner import scan_directory, prettify_structure
   
   scan_result = scan_directory(directory=".", output_file_name="directory_structure.txt",
                                ignored_items=('.git', '.idea', 'venv', '__pycache__',))
   
   prettify_structure(output_file=scan_result, spaces_to_trim=4, lines_to_trim=1)
   ```
   
---
Output example `directory_structure.txt`:
```
directory_structure.txt
LICENSE.rst
README.md
setup.py
usage.py
directory_scanner/
    directory_structure.txt
    main.py
    __init__.py
```
---

### About:
The Directory Scanner library aims to simplify directory scanning tasks by providing a flexible and easy-to-use interface. Whether you need to generate a directory structure for documentation, analysis, or any other purpose, this library offers a convenient solution.

### Links:
- [GitHub Repository](https://github.com/Armen-Jean-Andreasian/the-directory-scanner)
- [PyPI Package](https://pypi.org/project/the-directory-scanner/)

---