from selenium import webdriver
import time

PATH = "C:\Program Files (x86)/chromedriver.exe"
text_search = 'A friendly introduction to software testing'
driver = webdriver.Chrome(PATH)
driver.get("https://www.amazon.com")
search_input = driver.find_element_by_id("twotabsearchtextbox")
search_input.send_keys(text_search)
search_button = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
search_button.click()
time.sleep(2)
link = driver.find_element_by_link_text('A Friendly Introduction to Software Testing')
link.click()
time.sleep(2)
paperback = driver.find_element_by_xpath('//*[@id="a-autoid-5"]')
paperback.click()
time.sleep(2)
add_to_cart = driver.find_element_by_xpath('//*[@id="submit.add-to-cart-ubb"]/span')
add_to_cart.click()
time.sleep(2)
cart = driver.find_element_by_id("hlb-view-cart-announce")
cart.click()
time.sleep(2)
quantity= driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]')
quantity.click()
delete = driver.find_element_by_xpath('//*[@id="dropdown1_0"]')
time.sleep(2)
delete.click()
