# support
Python module providing some useful functionality that may be needed from time to time

<br></br>

-----

## implemented classes and functions

- class `filesystem`: class that helps doing several different file system operations

    - `__init__()`: constructor of class

        - Parameter: 
            - None
        - Initializes: 
            - conversion_table: table of conversions from bit to byte [Dictionary(str: float)]
        - Returns:
            - None

    - `get_files()`: get all files (with path name) and directories in given folder

        - Parameter:
            - path: path to folder containing the files [String]
        - Returns:    
            - Tuple containing [Tuple]
                - files: list containing all files [List(String)]
                - dirs: list containing all directories [List(String)]

    - `get_number_of_files()`: get number of all files and folders in given path

        - Parameter:
            - path: path to folder containing the files [String]
            - with_subdirs: whether (=True, default) or not (=False) include all files in subdirectories [Boolean]
        - Returns:    
            - Tuple containing [Tuple]
                - file_count: count of files in given folder [Integer]
                - dir_count: count of directories in given folder [Integer]

    - `get_size_of_object()`: get size (in bytes) of given object

        - Parameter:
            - path: path to folder or file [String]
        - Returns:
            - size: size of object (in bytes) [String]