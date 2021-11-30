from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

button = browser.find_element_by_css_selector('#get-input > .btn')
message = browser.find_element_by_id('user-message')
message.clear()
message.send_keys('Test')
button.click()
output = browser.find_element_by_id('display')

print(output.text)
assert 'Test' in output.text

browser.quit()
