
@login
Feature: Login functionality

  @login1
  Scenario: Successful login
    Given the user is on the login page
    When the user enters a valid username
    And the user enters a valid password
    And the user clicks the login button
    Then shows home page