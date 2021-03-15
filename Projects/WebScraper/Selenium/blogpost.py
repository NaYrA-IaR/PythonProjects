from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://cache9.in/")

driver.maximize_window()

# Go To Account Section For Login

account = driver.find_element_by_class_name("fa-user")
actions = ActionChains(driver)
actions.click(account)
actions.perform()

# Login

username = driver.find_element_by_name("username-103")
username.send_keys("cache9 Username Here")

password = driver.find_element_by_id("user_password-103")
password.send_keys("cache9 Password here")

driver.implicitly_wait(10)

login = driver.find_element_by_class_name("um-half")
actions1 = ActionChains(driver)
actions1.click(login)
actions1.perform()

# Tried login twice as it was showing error.
 '''
username = driver.find_element_by_name("username-103")
username.send_keys("cache9 Username Here")

password = driver.find_element_by_id("user_password-103")
password.send_keys("cache9 Password here")

login = driver.find_element_by_class_name("um-half")
actions1 = ActionChains(driver)
actions1.click(login)
actions1.perform()
'''

# Write Post Page

write = driver.find_element_by_class_name("fa-pencil-alt")
actions = ActionChains(driver)
actions.click(write)
actions.perform()

# Post Title

post_title = driver.find_element_by_id("user-submitted-title")
post_title.send_keys("Hello World From Bot")

# Post Tag

post_tag = driver.find_element_by_id("user-submitted-tags")
post_tag.send_keys("Aryan Kumar Rai")

# Post Category

post_category = driver.find_element_by_class_name("chosen-search-input")
for i in range(9):
	post_category.send_keys(Keys.DOWN)
post_category.send_keys(Keys.RETURN)

# Post Body

driver.switch_to.frame(driver.find_element_by_id("uspcontent_ifr"))
post_body = driver.find_element_by_id("tinymce")
post_body.send_keys("Hello World!! This is Selenium Bot posting here for the first time.")
driver.switch_to.default_content()

# Submit Post

submit = driver.find_element_by_id("user-submitted-post")
action = ActionChains(driver)
action.click(submit)
action.perform()