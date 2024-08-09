from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('https://www.qa-practice.com/elements/input/simple')

submitform = browser.find_element(By.CLASS_NAME, 'textinput')
# submitform = browser.find_element(By.ID, 'id_text_string')

submit = submitform.send_keys('Check')
enter = submitform.send_keys(Keys.ENTER)

result = browser.find_element(By.CLASS_NAME, 'result-text')
assert 'Check' in result.text

tab = browser.find_element(By.XPATH, '//a[@href="/elements/input/simple"]')
background_value = tab.value_of_css_property("background-color")
expected_background = "rgba(0, 0, 0, 0)"

if background_value == expected_background:
    print("Expected color")
else:
    print(f"Color does not match. Expected: {expected_background}, actual: {background_value}")

sleep(5)