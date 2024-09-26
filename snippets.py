def _test_is_():
    try:
        assert True
    except NoSuchElementException:
        assert False

    browser.refresh()