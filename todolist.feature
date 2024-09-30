Feature: Todolist
  There is a GUI (todolist and a button (named as button_add) that adding todo_item)
  User can add, edit and remove todo_items
  User can cancel adding, editing and removing todo_items

  Scenario: Rendering this web application
    Given I'm a user

    When I go to the target page

    Then I must see button_add
    And button_add's text must be equal '+ Добавить элемент'

  Scenario: Adding a new todo_item
    Given I'm on the target page

    When I click button_add

    Then Click of button_add must add todo_item

  Scenario: Adding a new todo_item's input
    When todo_item was added

    Then There must be input

  Scenario: Cancelling of adding a todo_item
    Given There is one todo_item

    When I click of the button that cancelling adding todo_item

    Then There is no todo_item

  Scenario: Filling by text a todo_item
    Given There is one todo_item

    When I fill todo_item's input by text

    Then todo_item's input must save spaces on the edge of input's value

  Scenario: Pressing Enter after filling by text a todo_item
    Given There is one todo_item
    And I has filled todo_item's input by text

    When I press Enter

    Then todo_item's input must remove spaces on the edge of input's value
    And There must be an element with the same text

  Scenario: Finding a button for editing todo_item
    Given There is one todo_item_with_filled_input
    And I has pressed Enter

    When I'm on the page

    Then There is the button for editing todo_item

  Scenario: Finding a button for removing todo_item
    Given There is one todo_item_with_filled_input
    And I has pressed Enter

    When I'm on the page

    Then There is the button for removing todo_item

  Scenario: Switching on editing state
    Given There is one todo_item_with_filled_input
    And I has pressed Enter

    When I click a button for editing

    Then There is an input for editing

  Scenario: Switching on removing state
    Given There is one todo_item_with_filled_input
    And I has pressed Enter

    When I click a button for removing

    Then There is a modal for removing

  Scenario: Finding buttons Yes and No on a removing modal
    Given There is one todo_item_with_filled_input
    And I has pressed Enter

    When I click a button for removing

    Then There are buttons Yes and No on the modal

  Scenario: Removing todo_item
    Given There is a removing modal

    When I click 'Yes' button

    Then There is no todo_item

  Scenario: Cancel removing todo_item
    Given There is a removing modal

    When I click 'No' button

    Then There is one todo_item