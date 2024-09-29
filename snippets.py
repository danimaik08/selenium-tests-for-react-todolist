def _test_is_():
    pass

with pytest.raises(Exception):
    pass

with pytest.raises(NoSuchElementException):
    pass

# comment
""" """

@pytest.fixture(autouse=True)
def before_and_after_each_test():
    yield
    browser_api.refresh()