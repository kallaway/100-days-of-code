import pytest
from selenium import webdriver
rom selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new online time app. She goes
# to check out its homepage

# She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title
def test_flask_is_running():

    browser = webdriver.Firefox()
    browser.get('http://localhost:5000')

    assert 'flask' in browser.title


# She is invited to enter a time item straight away ina a form

# She

# When she hits enter, the page updates, and show the time down the form

# There is still a text box inviting her to add another item. She
# enters types 22 in hour field 11 in minute fiel and 30 in seconds fields

# The page updates again, and now shows both items on her list

# Satisfied, she goes back to sleep

    browser.quit()
