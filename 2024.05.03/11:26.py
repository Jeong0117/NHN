import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# 크롬 드라이버 경로 설정
chrome_driver_path = "/Users/nhn/Desktop/Automation/chromedriver"

# 크롬 드라이버 서비스 설정
service = Service(chrome_driver_path)

# 크롬 브라우저 열기
driver = webdriver.Chrome(service=service)

# 웹 페이지 불러오기
url = "https://dev-www.fashiongo.net/login?returnUrl=%2F"
driver.get(url)

#로그인
id_field = driver.find_element("id","email-inp")
pw_field = driver.find_element("id","pwd_inp")

id = "detester999@gmail.com"
pw = "Ehlswkd*1596"
id_field.send_keys(id)
pw_field.send_keys(pw)

login = driver.find_element("id","btn-signin")
login.click()

time.sleep(10)

#검색필드에 입력
search = driver.find_element("id","lb_sch")

search.send_keys("TA1680")

search.send_keys(Keys.RETURN)

time.sleep(2)

#아이템 디테일 이동
Selectitem = driver.find_element(By.CSS_SELECTOR,"#item-found > div.product_wrap > ul > li:nth-child(1) > div.info > p:nth-child(2) > a")
Selectitem.click()

time.sleep(5)

#수량입력 후 쇼핑백으로 이동
inputqty = driver.find_element(By.ID,'lb_qty')
inputqty.clear()
qty = 3
inputqty.send_keys(qty)

time.sleep(2)

driver.execute_script("window.scrollTo(0, window.scrollY + 300);")
time.sleep(1)

addtoshopping = driver.find_element(By.XPATH,"//button[contains(@class, 'btn_black_v01') and contains(@class, 'addCart')]")
addtoshopping.click()

time.sleep(5)

shoppingbag = driver.find_element(By.ID,'miniCount')
shoppingbag.click()
shoppingbag.click()

time.sleep(5)

driver.find_element(By.XPATH,"//button[contains(@class, 'btn-dark_grey ') and contains(@class, 'checkoutAll')]").click()
time.sleep(5)

driver.find_element_by_xpath("//button[@class='btn-sure' and text()='Continue To Checkout']").click()
time.sleep(5)
# 드라이버 종료
driver.quit()

