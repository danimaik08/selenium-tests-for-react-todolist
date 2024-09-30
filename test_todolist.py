import pytest
from selenium.common import NoSuchElementException
from api import BrowserAPI

""" Function: todolist app """
""" There is a GUI (todolist and a button (named as button_add) that adding todo_item) """
""" User can add, edit and remove todo_items """
""" User can cancel adding, editing and removing todo_items """
""" Background: User opened page with url = {settings.TARGET} """

browser_api = BrowserAPI()

@pytest.fixture(autouse=True)
def after_each():
    yield
    browser_api.refresh()

def test_is_correct_text_of_button_add():
    """ Text of button_add must be equal '+ Добавить элемент' """
    assert browser_api.get_button_add().text == '+ Добавить элемент'

def test_is_added_one_element_todolist_by_click():
    """ Click of button_add must add todo_item """
    browser_api.click_button_add()
    browser_api.get_todo_item()

def test_todolist_element_has_input_after_adding_by_button_add():
    """ Click of button_add must add input """
    browser_api.click_button_add()
    browser_api.get_adding_input()

def test_todolist_is_empty_after_creating_and_canceling_of_creating():
    """
    Background: User clicked button_add.
    Click of the button that cancelling adding todo_item must remove todo_item
    """
    browser_api.click_button_add()
    browser_api.click_button_cancel_adding()

    with pytest.raises(NoSuchElementException):
        browser_api.get_todo_item()

def test_todolist_elements_creating_input_enable():
    """
    Background: User clicked button_add.
    todo_item's input must be interactive after adding into todolist
    """
    browser_api.click_button_add()
    element_input = browser_api.get_adding_input()
    element_input.send_keys('string')

def test_todolist_elements_input_save_space_on_the_edge():
    """
    Background: User clicked button_add.
    todo_item's input must save spaces on the edge of input's value
    """
    browser_api.click_button_add()
    todo_item_input = browser_api.get_adding_input()

    string_with_spaces_on_the_edge = ' string '
    todo_item_input.send_keys(string_with_spaces_on_the_edge)

    assert string_with_spaces_on_the_edge == todo_item_input.get_dom_attribute('value')

def test_todolist_element_doesnt_save_space_on_the_edge_after_pressing_enter():
    """
    Background: User clicked button_add.
    todo_item's text must remove spaces on the edge of input's value after adding
    """
    browser_api.click_button_add()

    element_input = browser_api.get_adding_input()

    string_with_spaces_on_the_edge = ' string '
    element_input.send_keys(string_with_spaces_on_the_edge)
    browser_api.press_enter()
    div_with_text = browser_api.get_todo_item_text()

    assert (string_with_spaces_on_the_edge != div_with_text.text
            and string_with_spaces_on_the_edge.strip() == div_with_text.text)

def test_is_found_button_edit_todo_item(add_todo_item):
    """
    Background: User clicked button_add, added a text into input and pressed Enter.
    todo_item must have button that allows to edit todo_item
    """
    browser_api.get_button_edit_todo_item()

def test_is_found_button_remove_todo_item(add_todo_item):
    """
    Background: User clicked button_add, added a text into input and pressed Enter.
    todo_item must have button for removing todo_item
    """
    browser_api.get_button_remove_todo_item()

def test_is_enable_editing_input_by_click_button_edit_todo_item(add_todo_item):
    """
    Background: User clicked button_add, added a text into input and pressed Enter.
    Background Next Step: User clicked button that allows to edit todo_item
    todo_item must have input
    """
    browser_api.click_button_edit_todo_item()
    browser_api.get_editing_input()

def test_is_opened_modal_by_click_button_remove_todo_item(add_todo_item):
    """
    Background: User clicked button_add, added a text into input and pressed Enter.
    Background Next Step: User clicked button for removing todo_item
    There must be modal
    """
    browser_api.click_button_remove_todo_item()
    browser_api.get_removing_modal()

def test_removing_modal_has_button_yes_and_no(add_todo_item):
    """
    Background: User clicked button_add, added a text into input and pressed Enter.
    Background Next Step: User clicked button for removing todo_item
    There must be modal buttons Yes and No
    """
    browser_api.click_button_remove_todo_item()
    browser_api.get_removing_modal_button_yes()
    browser_api.get_removing_modal_button_no()

def test_removing_modal_click_yes_removed_todo_item(add_todo_item):
    """
    Background: User clicked button_add, added a text into input and pressed Enter.
    Background Next Step: User clicked button for removing todo_item
    User must remove todo_item by click button Yes
    """
    browser_api.click_button_remove_todo_item()
    browser_api.click_removing_modal_button_yes()

    with pytest.raises(NoSuchElementException):
        browser_api.get_todo_item()

def test_removing_modal_click_no_removed_removing_modal(add_todo_item):
    """
    Background: User clicked button_add, added a text into input and pressed Enter.
    Background Next Step: User clicked button for removing todo_item
    User must close modal by click button No
    """
    browser_api.click_button_remove_todo_item()
    browser_api.click_removing_modal_button_no()

    with pytest.raises(NoSuchElementException):
        browser_api.get_removing_modal()

@pytest.fixture()
def add_todo_item():
    browser_api.click_button_add()
    todo_item_input = browser_api.get_adding_input()
    todo_item_input.send_keys('string')
    browser_api.press_enter()
    yield