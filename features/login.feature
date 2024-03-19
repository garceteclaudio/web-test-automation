@login
Feature: Login
    As an user i want to login to the app

    @login1
    Scenario: Login to the page 1
        Given Launch chrome browser
        When I type my user "standard_user"
        And my password
        And click login button
        Then I enter to the app

    @login2
    Scenario: Login to the page 2
        Given Launch chrome browser
        When I type my user "standard_user"
        And my password
        And click login button
        Then I enter to the app
