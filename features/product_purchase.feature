
@purchase @all
Feature: Product purchase functionality

  @purchase1
  Scenario: Successful login
    Given the user is on the login page
    When the user enters a valid username
    And the user enters a valid password
    And the user clicks the login button
    Then shows home page
    When the user select an item
    And the user click shopping cart
    And the user click checkout
    And the user complete personal information
    Then shows checkout overview
    When the user click finish
    Then shows than your for your order
