import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from settings import TARGET
from api import BrowserAPI

browser_api = BrowserAPI()

def test_is_correct_text_of_button_add():
    assert browser_api.get_button_add().text == '+ Добавить элемент'

def test_is_added_one_element_todolist_by_click():
    browser_api.click_button_add()
    browser_api.get_todo_item()

    browser_api.refresh()

def test_todolist_element_has_input_after_adding_by_button_add():
    browser_api.click_button_add()
    browser_api.get_creating_input()

    browser_api.refresh()

def test_todolist_is_empty_after_creating_and_canceling_of_creating():
    browser_api.click_button_add()
    browser_api.click_button_cancel_creating()

    with pytest.raises(NoSuchElementException):
        browser_api.get_todo_item()

    browser_api.refresh()

def test_todolist_elements_creating_input_enable():
    browser_api.click_button_add()
    element_input = browser_api.get_creating_input()
    element_input.send_keys('string')

    browser_api.refresh()

def test_todolist_elements_input_save_space_on_the_edge():
    browser_api.click_button_add()
    todo_item_input = browser_api.get_creating_input()

    string_with_spaces_on_the_edge = ' string '
    todo_item_input.send_keys(string_with_spaces_on_the_edge)

    assert string_with_spaces_on_the_edge == todo_item_input.get_dom_attribute('value')

    browser_api.refresh()

def test_todolist_element_doesnt_save_space_on_the_edge_after_pressing_enter():
    browser_api.click_button_add()

    element_input = browser_api.get_creating_input()

    string_with_spaces_on_the_edge = ' string '
    element_input.send_keys(string_with_spaces_on_the_edge)
    browser_api.press_enter()
    div_with_text = browser_api.get_todo_item_text()

    assert (string_with_spaces_on_the_edge != div_with_text.text
            and string_with_spaces_on_the_edge.strip() == div_with_text.text)

    browser_api.refresh()

def test_is_found_button_edit_todo_item():
    browser_api.create_todo_item()
    browser_api.get_button_edit_todo_item()

    browser_api.refresh()

def test_is_found_button_remove_todo_item():
    browser_api.create_todo_item()
    browser_api.get_button_remove_todo_item()

    browser_api.refresh()

def test_is_enable_editing_input_by_click_button_edit_todo_item():
    browser_api.create_todo_item()
    browser_api.click_button_edit_todo_item()
    browser_api.get_editing_input()

    browser_api.refresh()

def test_is_opened_modal_by_click_button_remove_todo_item():
    browser_api.create_todo_item()
    browser_api.click_button_remove_todo_item()
    browser_api.get_removing_modal()

    browser_api.refresh()

def test_removing_modal_has_button_yes_and_no():
    browser_api.create_todo_item()
    browser_api.click_button_remove_todo_item()
    browser_api.get_removing_modal_button_no()
    browser_api.get_removing_modal_button_yes()

    browser_api.refresh()

def test_removing_modal_click_yes_removed_todo_item():
    browser_api.create_todo_item()
    browser_api.click_button_remove_todo_item()
    browser_api.click_removing_modal_button_yes()

    with pytest.raises(NoSuchElementException):
        browser_api.get_todo_item()

    browser_api.refresh()

def test_removing_modal_click_no_removed_removing_modal():
    browser_api.create_todo_item()
    browser_api.click_button_remove_todo_item()
    browser_api.click_removing_modal_button_no()

    with pytest.raises(NoSuchElementException):
        browser_api.get_removing_modal()

    browser_api.refresh()