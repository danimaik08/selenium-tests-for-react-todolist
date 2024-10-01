Feature: Todolist
  There is a GUI (todolist and a button (named as button_add) that adding todo_item)
  User can add, edit and remove todo_items
  User can adding, cancel adding, editing, cancel editing, removing and cancel removing todo_items
  button that adds todo_item named as button_add
  button that edits todo_item named as button_edit
  button that opens todo_item's removing modal named as button_open_removing_modal
  button that removes todo_item named as button_remove
  todo_item's button that cancels adding named as button_cancel_adding
  todo_item's button that cancels editing named as button_cancel_editing
  todo_item's button that cancels removing named as button_cancel_removing

  Scenario: Rendering this web application
    Given I'm on page

    Then button_add should be
    And button_add's text should be equal '+ Добавить элемент'

  Scenario: Adding a new todo_item
    Given given There is 0 todo_item

    When I click button_add

    Then There is 1 todo_item

  Scenario: Adding a new todo_item's input
    Given given There is 1 todo_item

    Then There is 1 adding input

  Scenario: Cancelling of adding a todo_item
    Given given There is 1 todo_item

    When I click button_cancel_adding

    Then There is 0 todo_item

  Scenario: Filling by text a todo_item
    Given given There is 1 todo_item

    When I fill all adding inputs by text ' string '

    Then adding inputs texts are equal ' string '

  Scenario: Pressing Enter after filling by text a todo_item
    Given given There is 1 todo_item
    And given adding inputs texts are equal ' string '

    When I press Enter

    Then There is an element with a text equal 'string'

  Scenario: Finding button_edit
    Given given There is 1 todo_item
    And given adding inputs texts are equal 'string'
    And I pressed Enter

    Then There is button_edit

  Scenario: Finding button_open_removing_modal
    Given given There is 1 todo_item
    And given adding inputs texts are equal 'string'
    And I pressed Enter

    Then There is button_open_removing_modal

  Scenario: Switching on editing state
    Given given There is 1 todo_item
    And given adding inputs texts are equal 'string'
    And I pressed Enter

    When I click button_edit

    Then There is an editing input

  Scenario: Switching on removing state
    Given given There is 1 todo_item
    And given adding inputs texts are equal 'string'
    And I pressed Enter

    When I click button_open_removing_modal

    Then There is a removing modal

  Scenario: Finding button_remove and button_cancel_removing on a removing modal
    Given given There is 1 todo_item
    And given adding inputs texts are equal 'string'
    And I pressed Enter

    When I click button_open_removing_modal

    Then There is button_remove
    And There is button_cancel_removing

  Scenario: Removing todo_item
    Given given There is 1 todo_item
    And given adding inputs texts are equal 'string'
    And I pressed Enter

    When I click button_open_removing_modal
    And I click button_remove

    Then There is 0 todo_item

  Scenario: Cancel removing todo_item
    Given given There is 1 todo_item
    And given adding inputs texts are equal 'string'
    And I pressed Enter

    When I click button_open_removing_modal
    And I click button_cancel_removing

    Then There is 1 todo_item