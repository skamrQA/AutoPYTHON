import pytest
from string_util import StringUtils

# метод capitilize


@pytest.mark.positive_test_capitilize
@pytest.mark.parametrize('line, result', [("привет", "Привет"),
                                          ('123', "123"),
                                          ("Добрый день", "Добрый день")])
def test_positive_capitilize(line, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(line)
    assert res == result


@pytest.mark.xfail
@pytest.mark.negative_test_capitilize
@pytest.mark.parametrize('line, result', [("", ""),  # должен падать но проходит тест
                                          # также должен падать но проходит
                                          (" ", " "),
                                          (None, None)
                                          ])
def test_negative_capitilize(line, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(line)
    assert res == result
