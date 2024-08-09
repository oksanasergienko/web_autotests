from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('https://www.qa-practice.com/elements/button/simple')

requirements = browser.find_element(By.CSS_SELECTOR, "a[href='#req_text']").click()
# requirements = browser.find_element(By.ID, 'req_header').click()

click_button = browser.find_element(By.ID, 'submit-id-submit').click()
# click_button = browser.find_element(By.CLASS_NAME, 'btn').click()
# click_button = browser.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]').click()
# click_button = browser.find_element(By.XPATH, '//input[@class="btn btn-primary"]').click()

result = browser.find_element(By.CLASS_NAME, 'result-text')
assert 'Submitted' in result.text

sleep(5)