import pytest, os
from support import helper

def test_getfuncparams() -> None:
    '''
    tests if get_func_params() returns the correct arguments and their default values
    Parameter:
        - None
    Returns:
        - None 
    '''
    h = helper()
    parameterlist = h.get_func_params(os.listdir)
    assert parameterlist == {"path": None}, "wrong parameters for os.listdir"
    parameterlist = h.get_func_params(os.path)
    assert parameterlist == {}, "wrong parameters for os.path. Should be empty"