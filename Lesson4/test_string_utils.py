import pytest
from string_utils import StringUtils

stringutils = StringUtils()

@pytest.mark.parametrize( 'str1, result', [("hihi", "Hihi")] )
def test_capitalize_positive(str1, result):
    stringutils = StringUtils()
    res = stringutils.capitalize(str1)
    assert res == result

@pytest.mark.parametrize( 'str1, result', [("", "Hihi")] )
def test_capitalize_negative(str1, result):
    stringutils = StringUtils()
    res = stringutils.capitalize(str1)
    assert res == result