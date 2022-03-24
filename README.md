# support

<p align="center">
    <p align="center">
        <a href="https://github.com/papstchaka/support/actions">
          <img alt="Build Python Package" src="https://github.com/papstchaka/support/actions/workflows/python-package.yml/badge.svg"/>
        </a>
        <a href="https://github.com/papstchaka/support/actions">
          <img alt="Code Coverage" src="https://github.com/papstchaka/support/actions/workflows/codecov.yml/badge.svg"/>
        </a>
        <a href="https://codecov.io/gh/papstchaka/support/">
          <img src="https://codecov.io/gh/papstchaka/support/branch/master/graph.badge.svg"/>
        </a>
        <a href="https://github.com/papstchaka/support/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/papstchaka/support?color=0088ff"/>
        </a>
        <a href="https://github.com/papstchaka/support/pulls">
          <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/papstchaka/support?color=0088ff"/>
        </a>
    </p>
</p>

---

<br></br>

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

    - `check_for_folder()`: checks if given folder exists. If not, it creates it

        - Parameter:
            - path: path to folder to check for [String]
        - Returns:
            - None

-----

- class `helper`: bunch of helper functions that don't belong to other classes

    - `__init__()`: constructor of class

        - Parameter: 
            - None
        - Initializes: 
            - None
        - Returns:
            - None

    - `get_func_params()`: helper-function to determine all parameters and their default values from given function

        - Parameter: 
            - function: function to check [Python.object]
        - Returns:
            - parameterlist: Dictionary of parameters and respective default value (if existing) [Dictionary(String: object)]