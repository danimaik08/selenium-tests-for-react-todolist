import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from settings import TARGET

browser = webdriver.Chrome()

browser.get(TARGET)

def test_is_correct_text_of_button_add():
    assert get_button_add().text == '+ Добавить элемент'

def test_is_added_one_element_todolist_by_click():
    try:
        click_button_add()
        get_todo_item()
        assert True
    except NoSuchElementException:
        assert False

    browser.refresh()

def test_todolist_element_has_input_after_adding_by_button_add():
    try:
        click_button_add()
        get_creating_input()
        assert True
    except NoSuchElementException:
        assert False

    browser.refresh()

def test_todolist_is_empty_after_creating_and_canceling_of_creating():
    try:
        click_button_add()
        click_button_cancel_creating()
        get_todo_item()
        assert False
    except NoSuchElementException:
        assert True

    browser.refresh()

def test_todolist_elements_creating_input_enable():
    try:
        click_button_add()
        element_input = get_creating_input()
        element_input.send_keys('string')
        assert True
    except NoSuchElementException:
        assert False

    browser.refresh()

def test_todolist_elements_input_save_space_on_the_edge():
    try:
        click_button_add()
        todo_item_input = get_creating_input()

        string_with_spaces_on_the_edge = ' string '
        todo_item_input.send_keys(string_with_spaces_on_the_edge)

        assert string_with_spaces_on_the_edge == todo_item_input.get_dom_attribute('value')
    except NoSuchElementException:
        assert False

    browser.refresh()

def test_todolist_element_doesnt_save_space_on_the_edge_after_pressing_enter():
    try:
        click_button_add()

        element_input = get_creating_input()

        string_with_spaces_on_the_edge = ' string '
        element_input.send_keys(string_with_spaces_on_the_edge)
        click_enter()
        div_with_text = get_todo_item_text()

        assert (string_with_spaces_on_the_edge != div_with_text.text
                and string_with_spaces_on_the_edge.strip() == div_with_text.text)
    except NoSuchElementException:
        assert False

    browser.refresh()

def test_is_found_button_edit():
    try:
        create_todo_item()
        get_button_edit()
        assert True
    except NoSuchElementException:
        assert False

    browser.refresh()

def test_is_found_button_remove():
    try:
        create_todo_item()
        get_button_remove()
        assert True
    except NoSuchElementException:
        assert False

    browser.refresh()

def test_is_enable_editing_input_by_click_button_edit():
    try:
        create_todo_item()
        click_button_edit()
        get_editing_input()
        assert True
    except NoSuchElementException:
        assert False

    browser.refresh()

def test_is_opened_modal_by_click_button_remove():
    try:
        create_todo_item()
        click_button_remove()
        get_removing_modal()
        assert True
    except NoSuchElementException:
        assert False

    browser.refresh()

time.sleep(1)

def get_button_add() -> WebElement:
    return browser.find_element(By.CLASS_NAME, 'button_add')

def get_button_edit() -> WebElement:
    return browser.find_element(By.CLASS_NAME, 'button_edit')

def get_button_remove() -> WebElement:
    return browser.find_element(By.CLASS_NAME, 'button_remove')

def click_button_add():
    get_button_add().click()

def click_button_edit():
    get_button_edit().click()

def click_button_remove():
    get_button_remove().click()

def get_todo_item() -> WebElement:
    return browser.find_element(By.CLASS_NAME,'todo_item')

def get_creating_input() -> WebElement:
    return browser.find_element(By.CLASS_NAME,'creating_input')

def get_editing_input() -> WebElement:
    return browser.find_element(By.CLASS_NAME,'editing_input')

def get_button_cancel_editing() -> WebElement:
    return browser.find_element(By.CLASS_NAME,'button_cancel_editing')

def get_button_cancel_creating() -> WebElement:
    return browser.find_element(By.CLASS_NAME,'button_cancel_creating')

def click_button_cancel_editing():
    return get_button_cancel_editing().click()

def click_button_cancel_creating():
    return get_button_cancel_creating().click()

def click_enter():
    ActionChains(browser).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

def get_todo_item_text() -> WebElement:
    return browser.find_element(By.CLASS_NAME, 'text')

def create_todo_item():
    click_button_add()
    todo_item_input = get_creating_input()
    todo_item_input.send_keys('string')
    click_enter()

def get_removing_modal():
    return browser.find_element(By.CLASS_NAME, 'removing_modal')