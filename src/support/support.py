import os, inspect

class filesystem:
    '''
    class that helps doing several different file system operations
    '''

    def __init__(self) -> None:
        '''
        constructor of class
        Parameter:
            - None
        Initializes:
            - conversion_table: table of conversions from bit to byte [Dictionary(str: float)]
        Returns:
            - None
        '''
        self.conversion_table = {
            "kiloByte": 1e3,
            "MegaByte": 1e6,
            "GigaByte": 1e9,
            "TeraByte": 1e12
        }

    def get_files(self, path:str) -> ([str], [str]):
        '''
        get all files (with path name) and directories in given folder
        Parameter:
            - path: path to folder containing the files [String]
        Returns:    
            - Tuple containing [Tuple]
                - files: list containing all files [List(String)]
                - dirs: list containing all directories [List(String)]
        '''
        files, dirs = [], []
        for (dir_path, dir_names, filenames) in os.walk(path):
            for f in filenames:
                files.append(os.path.join(dir_path, f))
            dirs.extend(dir_names)
        dirs = sorted(dirs)
        files = sorted(files)
        return files, dirs

    def get_number_of_files(self, path:str, with_subdirs:bool = True) -> (int, int):
        '''
        get number of all files and folders in given path
        Parameter:
            - path: path to folder containing the files [String]
            - with_subdirs: whether (=True, default) or not (=False) include all files in subdirectories [Boolean]
        Returns:    
            - Tuple containing [Tuple]
                - file_count: count of files in given folder [Integer]
                - dir_count: count of directories in given folder [Integer]
        '''
        if not with_subdirs:
            files = os.listdir(path)
            dirs = [path]
        else:
            files, dirs = self.get_files(path)
        file_count, dir_count = len(files), len(dirs)
        return file_count, dir_count

    def get_size_of_object(self, path:str) -> str:
        '''
        get size (in bytes) of given object
        Parameter:
            - path: path to folder or file [String]
        Returns:
            - size: size of object (in bytes) [String]
        '''
        total_size = 0
        for dir_path, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dir_path, f)
                ## sometimes the os doesn't let us open a file
                try:
                    total_size += os.path.getsize(fp)
                except:
                    pass
        ## convert from bits to byte
        _size = total_size / 1.07374
        for name, factor in self.conversion_table.items():
            if _size / factor < 1:
                continue
            else:
                size = f'size of {path} is {round(_size / factor, 1)} {name}'
        return size
        
    def check_for_folder(self, path:str) -> None:
        '''
        checks if given folder exists. If not, it creates it
        Parameter:
            - path: path to folder to check for [String]
        Returns:
            - None
        ''' 
        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)

class helper:
    '''
    bunch of helper functions that don't belong to other classes
    '''

    def __init__(self) -> None:
        '''
        constructor of class
        Parameter:
            - None
        Initializes:
            - None
        Returns:
            - None
        '''
        pass
            
    def get_func_params(self, function:object) -> {str: object}: 
        '''
        helper-function to determine all parameters and their default values from given function
        Parameter: 
            - function: function to check [Python.object]
        Returns:
            - parameterlist: Dictionary of parameters and respective default value (if existing) [Dictionary(String: object)]
        '''
        try:
            args, _, _, defaults, *_ = inspect.getfullargspec(function)
        except:
            print(f'{function} is an unsupported callable')
            return {}
        if "self" in args: args.remove("self")
        if defaults is not None:
            if len(defaults) < len(args):
                parameterlist = dict(zip(args[ : -len(defaults)], [None for i in range( len(args) - len(defaults) )]))
                parameterlist.update(dict(zip(args[-len(defaults) : ], defaults)))
            else:
                parameterlist = dict(zip(args, defaults))
        else:
            parameterlist = dict(zip(args, [None for i in range(len(args))]))
        return parameterlist