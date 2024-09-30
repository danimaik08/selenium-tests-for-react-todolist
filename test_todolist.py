import pytest
from pytest_bdd import scenario
from selenium.common import NoSuchElementException
from api import BrowserAPI

browser_api = BrowserAPI()

@pytest.fixture(autouse=True)
def after_each():
    yield
    browser_api.refresh()

@pytest.fixture(scope='session', autouse=True)
def before_all():
    browser_api.init()

@pytest.fixture(scope='session', autouse=True)
def after_all():
    yield
    browser_api.close()

@scenario('todolist.feature', 'Rendering this web application')
def test_is_correct_text_of_button_add():
    assert browser_api.get_button_add().text == '+ Добавить элемент'

@scenario('todolist.feature', 'Adding a new todo_item')
def test_is_added_one_element_todolist_by_click():
    browser_api.click_button_add()
    browser_api.get_todo_item()

@scenario('todolist.feature', 'Adding a new todo_item\'s input')
def test_todolist_element_has_input_after_adding_by_button_add():
    browser_api.click_button_add()
    browser_api.get_adding_input()

@scenario('todolist.feature', 'Cancelling of adding a todo_item')
def test_todolist_is_empty_after_creating_and_canceling_of_creating():
    browser_api.click_button_add()
    browser_api.click_button_cancel_adding()

    with pytest.raises(NoSuchElementException):
        browser_api.get_todo_item()

@scenario('todolist.feature', 'Filling by text a todo_item')
def test_todolist_elements_input_save_space_on_the_edge():
    browser_api.click_button_add()
    todo_item_input = browser_api.get_adding_input()

    string_with_spaces_on_the_edge = ' string '
    todo_item_input.send_keys(string_with_spaces_on_the_edge)

    assert string_with_spaces_on_the_edge == todo_item_input.get_dom_attribute('value')

@scenario('todolist.feature', 'Pressing Enter after filling by text a todo_item')
def test_todolist_element_doesnt_save_space_on_the_edge_after_pressing_enter():
    browser_api.click_button_add()

    element_input = browser_api.get_adding_input()

    string_with_spaces_on_the_edge = ' string '
    element_input.send_keys(string_with_spaces_on_the_edge)
    browser_api.press_enter()
    div_with_text = browser_api.get_todo_item_text()

    assert (string_with_spaces_on_the_edge != div_with_text.text
            and string_with_spaces_on_the_edge.strip() == div_with_text.text)

@scenario('todolist.feature', 'Finding a button for editing todo_item')
@pytest.mark.usefixtures('add_todo_item')
def test_is_found_button_edit_todo_item():
    browser_api.get_button_edit_todo_item()

@scenario('todolist.feature', 'Finding a button for removing todo_item')
@pytest.mark.usefixtures('add_todo_item')
def test_is_found_button_remove_todo_item():
    browser_api.get_button_remove_todo_item()

@scenario('todolist.feature', 'Switching on editing state')
@pytest.mark.usefixtures('add_todo_item')
def test_is_enable_editing_input_by_click_button_edit_todo_item():
    browser_api.click_button_edit_todo_item()
    browser_api.get_editing_input()

@scenario('todolist.feature', 'Switching on removing state')
@pytest.mark.usefixtures('add_todo_item')
def test_is_opened_modal_by_click_button_remove_todo_item():
    browser_api.click_button_remove_todo_item()
    browser_api.get_removing_modal()

@scenario('todolist.feature', 'Finding buttons Yes and No on a removing modal')
@pytest.mark.usefixtures('add_todo_item')
def test_removing_modal_has_button_yes_and_no():
    browser_api.click_button_remove_todo_item()
    browser_api.get_removing_modal_button_yes()
    browser_api.get_removing_modal_button_no()

@scenario('todolist.feature', 'Removing todo_item')
@pytest.mark.usefixtures('add_todo_item')
def test_removing_modal_click_yes_removed_todo_item():
    browser_api.click_button_remove_todo_item()
    browser_api.click_removing_modal_button_yes()

    with pytest.raises(NoSuchElementException):
        browser_api.get_todo_item()

@scenario('todolist.feature', 'Cancel removing todo_item')
@pytest.mark.usefixtures('add_todo_item')
def test_removing_modal_click_no_removed_removing_modal():
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