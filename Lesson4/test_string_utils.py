from typing import Literal
import pytest
from string_utils import StringUtils

stringutils = StringUtils()

# метод capitilize

@pytest.mark.test_capitalize_positive
@pytest.mark.parametrize( 'str, result', [("hihi", "Hihi"),
                                           ("123", "123"),
                                           ("Good", "Good")] )
def test_capitalize_positive(str, result):
    stringutils = StringUtils()
    res = stringutils.capitalize(str)
    assert res == result

@pytest.mark.xfail
@pytest.mark.test_capitalize_negative
@pytest.mark.parametrize( 'str, result', [("", ""),
                                          (" ", " "),
                                          (None, None)
                                          ] )
def test_capitalize_negative(str, result):
    stringutils = StringUtils()
    res = stringutils.capitalize(str)
    assert res == result

