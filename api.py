from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from settings import TARGET

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class BrowserAPI:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get(TARGET)

    def get_button_add(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, '[data-testid="button_add"]')

    def get_button_edit_todo_item(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, '[data-testid="button_edit_todo_item"]')

    def get_button_remove_todo_item(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, '[data-testid="button_remove_todo_item"]')

    def click_button_add(self):
        self.get_button_add().click()

    def click_button_edit_todo_item(self):
        self.get_button_edit_todo_item().click()

    def click_button_remove_todo_item(self):
        self.get_button_remove_todo_item().click()

    def get_todo_item(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR,'[data-testid="todo_item"]')

    def get_adding_input(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR,'[data-testid="creating_input"]')

    def get_editing_input(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR,'[data-testid="editing_input"]')

    def get_button_cancel_editing(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR,'[data-testid="button_cancel_editing"]')

    def get_button_cancel_adding(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR,'[data-testid="button_cancel_creating"]')

    def click_button_cancel_editing(self):
        return self.get_button_cancel_editing().click()

    def click_button_cancel_adding(self):
        return self.get_button_cancel_adding().click()

    def press_enter(self):
        ActionChains(self.browser).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

    def get_todo_item_text(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, '[data-testid="text"]')

    def add_todo_item(self):
        self.click_button_add()
        todo_item_input = self.get_adding_input()
        todo_item_input.send_keys('string')
        self.press_enter()

    def get_removing_modal(self):
        return self.browser.find_element(By.CSS_SELECTOR, '[data-testid="removing_modal"]')

    def get_removing_modal_button_yes(self):
        return self.browser.find_element(By.CSS_SELECTOR, '[data-testid="removing_modal"] [data-testid="modal_yes"]')

    def get_removing_modal_button_no(self):
        return self.browser.find_element(By.CSS_SELECTOR, '[data-testid="removing_modal"] [data-testid="modal_no"]')

    def click_removing_modal_button_yes(self):
        self.get_removing_modal_button_yes().click()

    def click_removing_modal_button_no(self):
        self.get_removing_modal_button_no().click()

    def refresh(self):
        self.browser.refresh()