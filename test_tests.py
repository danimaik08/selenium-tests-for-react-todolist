import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from settings import TARGET

browser = webdriver.Chrome()

browser.get(TARGET)

@pytest.mark.run_these_please
def test_is_correct_text_of_button_add():
    assert get_button_add().text == '+ Добавить элемент'

@pytest.mark.run_these_please
def test_is_added_one_element_todolist_by_click():
    click_button_add()
    get_todo_item()

    browser.refresh()

def test_todolist_element_has_input_after_adding_by_button_add():
    click_button_add()
    get_creating_input()

    browser.refresh()

def test_todolist_is_empty_after_creating_and_canceling_of_creating():
    click_button_add()
    click_button_cancel_creating()

    with pytest.raises(NoSuchElementException):
        get_todo_item()

    browser.refresh()

def test_todolist_elements_creating_input_enable():
    click_button_add()
    element_input = get_creating_input()
    element_input.send_keys('string')

    browser.refresh()

def test_todolist_elements_input_save_space_on_the_edge():
    click_button_add()
    todo_item_input = get_creating_input()

    string_with_spaces_on_the_edge = ' string '
    todo_item_input.send_keys(string_with_spaces_on_the_edge)

    assert string_with_spaces_on_the_edge == todo_item_input.get_dom_attribute('value')

    browser.refresh()

def test_todolist_element_doesnt_save_space_on_the_edge_after_pressing_enter():
    click_button_add()

    element_input = get_creating_input()

    string_with_spaces_on_the_edge = ' string '
    element_input.send_keys(string_with_spaces_on_the_edge)
    click_enter()
    div_with_text = get_todo_item_text()

    assert (string_with_spaces_on_the_edge != div_with_text.text
            and string_with_spaces_on_the_edge.strip() == div_with_text.text)

    browser.refresh()

def test_is_found_button_edit_todo_item():
    create_todo_item()
    get_button_edit_todo_item()

    browser.refresh()

def test_is_found_button_remove_todo_item():
    create_todo_item()
    get_button_remove_todo_item()

    browser.refresh()

def test_is_enable_editing_input_by_click_button_edit_todo_item():
    create_todo_item()
    click_button_edit_todo_item()
    get_editing_input()

    browser.refresh()

def test_is_opened_modal_by_click_button_remove_todo_item():
    create_todo_item()
    click_button_remove_todo_item()
    get_removing_modal()

    browser.refresh()

def test_removing_modal_has_button_yes_and_no():
    create_todo_item()
    click_button_remove_todo_item()
    get_removing_modal_button_no()
    get_removing_modal_button_yes()

    browser.refresh()

def test_removing_modal_click_yes_removed_todo_item():
    create_todo_item()
    click_button_remove_todo_item()
    click_removing_modal_button_yes()

    with pytest.raises(NoSuchElementException):
        get_todo_item()

    browser.refresh()

def test_removing_modal_click_no_removed_removing_modal():
    create_todo_item()
    click_button_remove_todo_item()
    click_removing_modal_button_no()

    with pytest.raises(NoSuchElementException):
        get_removing_modal()

    browser.refresh()

time.sleep(1)

def get_button_add() -> WebElement:
    return browser.find_element(By.CSS_SELECTOR, '[data-testid="button_add"]')

def get_button_edit_todo_item() -> WebElement:
    return browser.find_element(By.CSS_SELECTOR, '[data-testid="button_edit_todo_item"]')

def get_button_remove_todo_item() -> WebElement:
    return browser.find_element(By.CSS_SELECTOR, '[data-testid="button_remove_todo_item"]')

def click_button_add():
    get_button_add().click()

def click_button_edit_todo_item():
    get_button_edit_todo_item().click()

def click_button_remove_todo_item():
    get_button_remove_todo_item().click()

def get_todo_item() -> WebElement:
    return browser.find_element(By.CSS_SELECTOR,'[data-testid="todo_item"]')

def get_creating_input() -> WebElement:
    return browser.find_element(By.CSS_SELECTOR,'[data-testid="creating_input"]')

def get_editing_input() -> WebElement:
    return browser.find_element(By.CSS_SELECTOR,'[data-testid="editing_input"]')

def get_button_cancel_editing() -> WebElement:
    return browser.find_element(By.CSS_SELECTOR,'[data-testid="button_cancel_editing"]')

def get_button_cancel_creating() -> WebElement:
    return browser.find_element(By.CSS_SELECTOR,'[data-testid="button_cancel_creating"]')

def click_button_cancel_editing():
    return get_button_cancel_editing().click()

def click_button_cancel_creating():
    return get_button_cancel_creating().click()

def click_enter():
    ActionChains(browser).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

def get_todo_item_text() -> WebElement:
    return browser.find_element(By.CSS_SELECTOR, '[data-testid="text"]')

def create_todo_item():
    click_button_add()
    todo_item_input = get_creating_input()
    todo_item_input.send_keys('string')
    click_enter()

def get_removing_modal():
    return browser.find_element(By.CSS_SELECTOR, '[data-testid="removing_modal"]')

def get_removing_modal_button_yes():
    return browser.find_element(By.CSS_SELECTOR, '[data-testid="removing_modal"] [data-testid="modal_yes"]')

def get_removing_modal_button_no():
    return browser.find_element(By.CSS_SELECTOR, '[data-testid="removing_modal"] [data-testid="modal_no"]')

def click_removing_modal_button_yes():
    get_removing_modal_button_yes().click()

def click_removing_modal_button_no():
    get_removing_modal_button_no().click()