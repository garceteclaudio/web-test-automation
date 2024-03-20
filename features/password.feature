@password @all
Feature: Password
    As an user i want to test my password

    @password1
    Scenario: test user
        Given Launch chrome browser
        When I type my user "standard_user"
        And my password

    @password2
    Scenario: test password
        Given Launch chrome browser
        When I type my user "standard_user"
        And my password