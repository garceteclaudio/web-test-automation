Feature: Login
    
    Scenario: Login to the page
        Given Launch chrome browser
        #Step Parameters
        When I type my user "standard_user"
        And my password
        And click login button
        Then I enter to the app


    Scenario: Login to the page 2
        Given Launch chrome browser
        #Step Parameters
        When I type my user "standard_user"
        And my password
        And click login button
        Then I enter to the app