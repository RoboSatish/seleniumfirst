import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.flipkart.com/')
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[3]/div/span').click()
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/div/input').send_keys("One plus mobile ")

d1 = driver.find_element(By.XPATH,'//*[@id="dropdown-class-example"]/option[4]').click()
d1 = driver.find_element(By.CLASS_NAME,'blinkingText')
# print(d1.get_attribute('href'))

# d2 = Select(d1)
# d2.select_by_index(1)
# time.sleep(2)
# d2.select_by_visible_text("Option3")

#driver1 = driver.find_element(By.XPATH,'//*[@id="name"]').send_keys('satish')
#driver1 = driver.find_element(By.XPATH,'//*[@id="name"]').clear()
#driver1 = driver.find_element(By.XPATH,'//*[@id="name"]').send_keys('pawale')

#s1 = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/fieldset/legend')
#s2 = s1.text
#print(s2)
#driver.get('https://softgridinfo.in/login/main/login.php')

#driver.forward()
#driver.get('https://www.youtube.com/watch?v=iffK7bIFkG8&list=PLjVLYmrlmjGfGLShoW0vVX_tcyT8u1Y3E&index=20')
#driver.back()
#driver.get('https://softgridinfo.in/login/main/login.php')
#c1 = driver.find_element(By.ID,"checkBoxOption1")
#c1 = driver.find_element(By.XPATH,'/html/body/form/input[1]').send_keys('satsh11')
# c2 = driver.find_element(By.XPATH,'/html/body/form/input[2]').send_keys('123')
#c3 = driver.find_element(By.XPATH,'/html/body/form/input[3]').click()

#c4 = driver.find_element(By.XPATH,'/html/body/div/p[3]/a').click()

#c2 = driver.find_element(By.ID,"checkBoxOption2")
#c3 = driver.find_element(By.ID,"checkBoxOption3")
