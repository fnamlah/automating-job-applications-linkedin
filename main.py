from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = Service("/Users/faisalalnamlah/Desktop/Python Practice/chromedriver")
web_page = webdriver.Chrome(service=chrome_driver_path)
url = "https://www.linkedin.com/jobs/search/?currentJobId=3205241209&f_AL=true&geoId=92000000&keywords=marketing%20specialist&location=Worldwide&refresh=true"

web_page.get(url)
time.sleep(5)
# sign in:
sign_in = web_page.find_element(By.XPATH, '/html/body/div[3]/a[1]')
sign_in.click()
time.sleep(3)
email = web_page.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys("-")
password = web_page.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("-")
sign_in_button = web_page.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.send_keys(Keys.ENTER)
# clicking: Easy apply
time.sleep(10)
job_link = web_page.find_element(By.CSS_SELECTOR, '.jobs-apply-button')
job_link.click()
time.sleep(3)
phone = web_page.find_element(By.CSS_SELECTOR, '.fb-single-line-text__input')
if phone.text == "":
    phone.send_keys("234234545")
time.sleep(3)
next_button = web_page.find_element(By.CSS_SELECTOR, 'button[aria-label="Continue to next step"]')
next_button.click()
time.sleep(3)
next_button.click()
# review button
review_button = web_page.find_element(By.CSS_SELECTOR, 'button[aria-label="Review your application"]')
review_button.click()


time.sleep(1000)

