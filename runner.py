from behave.__main__ import main as behavemain

# Define the value of the tags you want to run
tags_value = "@login"

# Construct the command to execute Behave with the specified tags and formatting options
behave_command = f"--tags={tags_value} -f allure_behave.formatter:AllureFormatter -o reports/ features"

# Execute Behave using the imported main function
behavemain(behave_command.split())

