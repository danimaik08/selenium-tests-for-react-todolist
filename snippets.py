def _test_is_():
    pass

with pytest.raises(Exception):
    pass

with pytest.raises(NoSuchElementException):
    pass

# comment
""" """

@pytest.fixture(autouse=True)
def before_each():
    # something
    yield

@pytest.fixture(autouse=True)
def after_each():
    yield
    browser_api.refresh()

ids = ['Data(value={})'.format(num) for num in [1, 2, 3]]

@pytest.mark.parametrize('data', [1, 2, 3], ids=ids)
def _test_parametrize(data):
    assert [1, 2, 3].count(data) == 1

@pytest.fixture()
def some_data():
    return 42

def _test_some_data(some_data):
    assert some_data == 42

# Gherkin

Scenario: Rendering this web application
    Given I'm a user

    When I go to the target page

    Then I must see button_add
    And Text of button_add must be equal '+ Добавить элемент'