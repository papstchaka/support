import pytest
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
    assert files == ['PKG-INFO', 'SOURCES.txt', '__init__.py', 'dependency_links.txt', 'support.py', 'top_level.txt'], "files mismatch"
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
    assert 3.5 <= _size_val <= 6.0, "wrong size"