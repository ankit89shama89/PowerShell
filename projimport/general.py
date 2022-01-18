### importing python file\functions as module

#1st Method
import file_operations
file_operations.save_to_file('Rolf', 'data.txt')

# 2nd Method
from file_operations import read_from_file
print(read_from_file("data.txt"))

#### If module file is in a directory inside project
## create a __init__.py file inside the directory

## import file inside a folder - Absolute import

from import1.file_operations import save_to_file, read_from_file


