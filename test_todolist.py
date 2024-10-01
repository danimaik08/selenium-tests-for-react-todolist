import time
import pytest
from pytest_bdd import scenario, given, when, then, parsers
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

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

@given('I\'m on page')
def im_on_page():
    pass

@given(parsers.cfparse('given There is {todo_items_number_bdd:Number} todo_item', extra_types={'Number': int}))
def given_todo_items(todo_items_number_bdd):
    for i in range(todo_items_number_bdd):
        browser_api.click_button_add()

@given(parsers.cfparse('given adding inputs texts are equal \'{text_bdd:String}\'', extra_types={'String': str}))
def given_adding_inputs_texts_are_equal(text_bdd):
    for adding_input in browser_api.get_adding_inputs():
        adding_input.send_keys(str(text_bdd))

@given('I pressed Enter')
def given_pressed_enter():
    browser_api.press_enter()

@when('I click button_add')
def click_button_add():
    browser_api.click_button_add()

@when('I click button_cancel_adding')
def click_button_cancel_adding():
    browser_api.click_button_cancel_adding()

@when('I press Enter')
def press_enter():
    browser_api.press_enter()

@when(parsers.cfparse('I fill all adding inputs by text \'{text_with_spaces:String}\'', extra_types={'String': str}))
def fill_all_todo_items_inputs_by_text(text_with_spaces):
    for adding_input in browser_api.get_adding_inputs():
        adding_input.send_keys(str(text_with_spaces))

@when('I click button_open_removing_modal')
def click_button_removing_modal():
    browser_api.click_button_remove_todo_item()

@when('I click button_edit')
def click_button_edit():
    browser_api.click_button_edit_todo_item()

@when('I click button_remove')
def click_button_remove():
    browser_api.click_removing_modal_button_yes()

@when('I click button_cancel_removing')
def click_button_cancel_removing():
    browser_api.click_removing_modal_button_no()

@then('button_add should be', target_fixture='button_add')
def button_add() -> WebElement:
    return browser_api.get_button_add()

@then(parsers.cfparse('button_add\'s text should be equal \'{button_text:String}\'', extra_types={'String': str}))
def is_correct_text_of_button_add(button_add, button_text):
    assert button_add.text == button_text

@then(parsers.cfparse('There is {todo_items_number_bdd:Number} todo_item', extra_types={'Number': int}))
def is_correct_todo_items_amount(todo_items_number_bdd):
    assert len(browser_api.get_todo_items()) == todo_items_number_bdd

@then(parsers.cfparse('There is {inputs_number_bdd:Number} adding input', extra_types={'Number': int}))
def is_correct_inputs_amount(inputs_number_bdd):
    assert len(browser_api.get_adding_inputs()) == inputs_number_bdd

@then(parsers.cfparse('adding inputs texts are equal \'{text_with_spaces:String}\'', extra_types={'String': str}))
def is_correct_todo_items_text_after_filling(text_with_spaces):
    for adding_input in browser_api.get_adding_inputs():
        assert adding_input.get_dom_attribute('value') == text_with_spaces

@then(parsers.cfparse('There is an element with a text equal \'{text:String}\'', extra_types={'String': str}))
def is_correct_todo_items_text(text):
    assert browser_api.get_todo_item_text().text == text

@then('There is button_edit')
def there_is_button_edit():
    assert browser_api.get_button_edit_todo_item()

@then('There is button_open_removing_modal')
def there_is_button_open_removing_modal():
    assert browser_api.get_button_remove_todo_item()

@then('There is an editing input')
def there_is_editing_input():
    assert browser_api.get_editing_input()

@then('There is a removing modal')
def there_is_removing_modal():
    assert browser_api.get_removing_modal()

@then('There is button_remove')
def there_is_button_remove():
    assert browser_api.get_removing_modal_button_yes()

@then('There is button_cancel_removing')
def there_is_button_cancel_removing():
    assert browser_api.get_removing_modal_button_no()

@scenario('todolist.feature', 'Rendering this web application')
def test_is_correct_text_of_button_add():
    pass

@scenario('todolist.feature', 'Adding a new todo_item')
def test_is_added_one_element_todolist_by_click():
    pass

@scenario('todolist.feature', 'Adding a new todo_item\'s input')
def test_is_added_adding_input():
    pass

@scenario('todolist.feature', 'Cancelling of adding a todo_item')
def test_is_cancelled_todo_item_by_click_button_cancel_adding():
    pass

@scenario('todolist.feature', 'Filling by text a todo_item')
def test_adding_input_is_correctly_filled_by_text():
    pass

@scenario('todolist.feature', 'Pressing Enter after filling by text a todo_item')
def test_todo_item_is_correctly_filled_after_pressing_enter():
    pass

@scenario('todolist.feature', 'Finding button_open_removing_modal')
def test_finding_button_open_removing_modal():
    pass

@scenario('todolist.feature', 'Finding button_edit')
def test_finding_button_edit():
    pass

@scenario('todolist.feature', 'Finding button_open_removing_modal')
def test_finding_button_open_removing_modal():
    pass

@scenario('todolist.feature', 'Switching on editing state')
def test_switching_on_editing_state():
    pass

@scenario('todolist.feature', 'Switching on removing state')
def test_switching_on_removing_state():
    pass

@scenario('todolist.feature', 'Finding button_remove and button_cancel_removing on a removing modal')
def test_button_remove_and_button_cancel_remove():
    pass

@scenario('todolist.feature', 'Removing todo_item')
def test_removing_todo_item():
    pass

@scenario('todolist.feature', 'Cancel removing todo_item')
def test_cancel_removing_todo_item():
    pass