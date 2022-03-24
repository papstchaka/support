import pytest, os
from support import filesystem

def test_getfiles() -> None:
    '''
    tests if function get_files() returns the correct files and directories from given path
    Parameter:
        - None
    Returns:    
        - None
    '''
    path = "./src"
    fs = filesystem()
    files, dirs = fs.get_files(path)
    assert dirs == ["support", "support.egg-info"], "directories mismatch"
    assert files == [
            os.path.join(path, 'support.egg-info', 'PKG-INFO'), 
            os.path.join(path, 'support.egg-info', 'SOURCES.txt'),
            os.path.join(path, 'support.egg-info', "dependency_links.txt"),
            os.path.join(path, 'support.egg-info', "top_level.txt"),
            os.path.join(path, 'support', "__init__.py"),
            os.path.join(path, 'support', "support.py")
        ], "files mismatch"
    return

def test_getnumberoffiles() -> None:
    '''
    tests if get_number_of_files() returns the correct number of files and directories from given path
    Parameter:
        - None
    Returns:
        - None
    '''
    path = "./src"
    fs = filesystem()
    file_count, dir_count = fs.get_number_of_files(path)
    assert dir_count == 2, "directory count mismatch"
    assert file_count == 6, "file count mismatch"
    file_count, dir_count = fs.get_number_of_files(path, False)
    assert dir_count == 1, "directory count mismatch"
    assert file_count == 2, "file count mismatch"

def test_getsizeofobject() -> None:
    '''
    tests if get_size_of_object() returns roughly the correct amount of size of given path
    Parameter:
        - None
    Returns:
        - None
    '''
    path = "./src"
    fs = filesystem()
    _size = fs.get_size_of_object(path)
    assert _size.endswith("kiloByte"), "wrong unit"
    _size_val = float(_size.split(" ")[-2])
    assert 2.0 <= _size_val <= 20.0, "wrong size"

def test_checkforfolder() -> None:
    '''
    tests if check_for_folder() correctly creates new folder that wasn't there before
    Parameter:
        - None
    Returns:
        - None
    '''
    path = "./test"
    folder_name = "test"
    fs = filesystem()
    assert folder_name not in os.listdir(path), "folder test already exists"
    fs.check_for_folder(os.path.join(path, folder_name))
    assert folder_name in os.listdir(path), "creating folder test failed"
    os.rmdir(os.path.join(path, folder_name))
    assert folder_name not in os.listdir(path), "folder test still exists"