# Test Case
# --------
# 1) Open web browser(Chrome/ff/IE).
# 2) Open URL https://admin-demo.nopcommerce.com/login
# 3) Provide Email(admin@yourstore.com)
# 4) Provide password(admin).
# 5) Click on login.
# 6) Capture title of the dashboard page. (Actual title).
# 7) Verify title of the page: Dashbraod/ nopcommerce adminstration" (Expected)
# 8) Close Browser

# from selenium import webdriver
#
# from selenium.webdriver.chrome.service import Service
#
# ser_obj = Service("C:/Users/akash.chandel.ACS/Desktop/Drivers/chromedriver.exe")
# driver = webdriver.Chrome(service=ser_obj)
#
# driver.get("https://www.google.co.in/")
#
# driver.maximize_window()
#
# driver.close()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/akash.chandel.ACS/Desktop/Drivers/chromedriver.exe")

driver.get("https://github.com/login")
driver.maximize_window()

driver.find_element(By.ID,"login_field").send_keys("akashchandel27@gmail.com")
time.sleep(5)
driver.find_element(By.ID,"password").send_keys("Akash@27031995")

driver.find_element(By.CSS_SELECTOR,"input[value='Sign in']").click()
time.sleep(15)




#driver.find_element(By.CLASS_NAME,"HeaderMenu-link HeaderMenu-link--sign-in flex-shrink-0 no-underline d-block d-lg-inline-block border border-lg-0 rounded rounded-lg-0 p-2 p-lg-0").click()
#driver.find_element((By.CSS_SELECTOR,"HeaderMenu-link.HeaderMenu-link--sign-in.flex-shrink-0.no-underline.d-block.d-lg-inline-block.border.border-lg-0.rounded.rounded-lg-0.p-2.p-lg-0")).click()
#driver.find_element(By.CSS_SELECTOR,".HeaderMenu-link.HeaderMenu-link--sign-in.flex-shrink-0.no-underline.d-block.d-lg-inline-block.border.border-lg-0.rounded.rounded-lg-0.p-2.p-lg-0").click()
# time.sleep(14)
# driver.find_element(By.NAME,"user[email]").send_keys("akashchandel27@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"button[data-optimizely-event='click.signup_continue.email']").click()


# driver.find_element_by_name("username").send_keys("Admin")
# driver.find_element_by_name("password").send_keys("admin123")
# driver.find_element(by=class("oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"))





