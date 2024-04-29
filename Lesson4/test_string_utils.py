from typing import Literal
import pytest
from string_utils import StringUtils

stringutils = StringUtils()

# метод capitilize

@pytest.mark.test_capitalize_positive
@pytest.mark.parametrize( 'str, result', [("hihi", "Hihi"),
                                           ("123", "123"),
                                           ("good", "Good")] )
def test_capitalize_positive(str, result):
    stringutils = StringUtils()
    res = stringutils.capitalize(str)
    assert res == result

@pytest.mark.xfail
@pytest.mark.test_capitalize_negative
@pytest.mark.parametrize( 'str, result', [("", ""),
                                          (" ", " "),
                                          (None, None),
                                          (123, 123)
                                          ] )
def test_capitalize_negative(str, result):
    stringutils = StringUtils()
    res = stringutils.capitalize(str)
    assert res == result

# метод trim

@pytest.mark.test_trim_positive
@pytest.mark.parametrize( 'str, result', [("   Clow", "Clow"),
                                           ("   123", "123"),
                                           ("   .", ".")] )
def test_trim_positive(str, result):
    stringutils = StringUtils()
    res = stringutils.trim(str)
    assert res == result

@pytest.mark.xfail
@pytest.mark.test_trim_negative
@pytest.mark.parametrize( 'str, result', [(   123, 123),
                                          (" S u n", "Sun"),
                                          (" G ood", "Good"),
                                          (" Работ а", "Работа")
                                          ] )
def test_trim_negative(str, result):
    stringutils = StringUtils()
    res = stringutils.trim(str)
    assert res == result

# метод to_list
    
@pytest.mark.test_to_list_positive
@pytest.mark.parametrize( 'str, delim, result', [("1,2,3", ",", ["1", "2", "3"])])
def test_to_list_positive(str, delim, result):
    stringutils = StringUtils()
    res = stringutils.to_list(str, delim)
    assert res == result

@pytest.mark.xfail
@pytest.mark.test_to_list_negative
@pytest.mark.parametrize( 'str, delim, result', [(" , , ", ",", [" ", " ", " "])] )
def test_to_list_negative(str, delim, result):
    stringutils = StringUtils()
    res = stringutils.to_list(str, delim)
    assert res == result

# метод contains
    
@pytest.mark.test_contains_positive
@pytest.mark.parametrize( 'str, symbol, result', [("1,2,3", "1", True),
                                                  ("qwerty", "a", False)])
def test_contains_positive(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.contains(str, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.test_contains_negative
@pytest.mark.parametrize( 'str, symbol, result', [("1,2,3", "5", True)])
def test_contains_negative(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.contains(str, symbol)
    assert res == result    

# метод delete_symbol
    
@pytest.mark.delete_symbol_positive
@pytest.mark.parametrize( 'str, symbol, result', [("1,2,3", "1", ",2,3"),
                                                  ("emty", "e", "mty")])
def test_delete_symbol_positive(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(str, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.test_delete_symbol_negative
@pytest.mark.parametrize( 'str, symbol, result', [("1,2,3", "5", "1,2,3")])
def test_delete_symbol_negative(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(str, symbol)
    assert res == result

# метод starts_with
    
@pytest.mark.starts_with_positive
@pytest.mark.parametrize( 'str, symbol, result', [("1,2,3", "1", True),
                                                  ("cool", "c", True),
                                                  ("огонь", "н", False)])
def test_starts_with_positive(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.starts_with(str, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.test_starts_with_negative
@pytest.mark.parametrize( 'str, symbol, result', [("1,2,3", None, True)])
def test_starts_with_negative(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.starts_with(str, symbol)
    assert res == result

# метод end_with

@pytest.mark.end_with_positive
@pytest.mark.parametrize( 'str, symbol, result', [("1,2,3", "3", True),
                                                  ("light", "t", True),
                                                  ("добро", "д", False)])
def test_end_with_positive(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.end_with(str, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.test_end_with_negative
@pytest.mark.parametrize( 'str, symbol, result', [("1,2,3", None, True),
                                                  ("", "", True)])
def test_end_with_negative(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.end_with(str, symbol)
    assert res == result

# метод is_empty
    
@pytest.mark.is_empty_positive
@pytest.mark.parametrize( 'str, result', [("", True),
                                          (" ", True),
                                          ("А что если?", False)])
def test_is_empty_positive(str, result):
    stringutils = StringUtils()
    res = stringutils.is_empty(str)
    assert res == result

@pytest.mark.xfail
@pytest.mark.test_is_empty_negative
@pytest.mark.parametrize( 'str, result', [("     ",  True),
                                          (None, True),
                                          ])
def test_is_empty_negative(str, result):
    stringutils = StringUtils()
    res = stringutils.is_empty(str)
    assert res == result

# метод list_to_string

@pytest.mark.list_to_string_positive
@pytest.mark.parametrize( 'lst, joi, result', [([1,2,3,4], ", ", "1, 2, 3, 4"),
                                                (["just", "do", "it"], " - ", "just - do - it"),
                                              ])
def test_list_to_string_positive(lst, joi, result):
    stringutils = StringUtils()
    res = stringutils.list_to_string(lst, joi)
    assert res == result

@pytest.mark.xfail
@pytest.mark.test_list_to_string_negative
@pytest.mark.parametrize( 'lst, joi, result', [([" , , ,"], "*", "* * *" ),
                                               ([None], "!", ""),
                                              ])
def test_list_to_string_negative(lst, joi, result):
    stringutils = StringUtils()
    res = stringutils.list_to_string(lst, joi)
    assert res == result
