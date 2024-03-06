print("FILE INI UNTUK LATIHAN CONTOH AKSES DATA DARI WEB versi 2")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("02. MEMBUAT KONEKSI Akses sebuah Class dari Web : ")
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

cdp = "C:/developer/chromedriver.exe"
service = Service(executable_path=cdp)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#driver.get("https://www.google.com")
driver.get("https://www.tokopedia.com/lighttechcomp/memory-4gb-laptop-lenovo-thinkpad-x240-x250-t410-t420-t430-memori-ram?extParam=ivf%3Dfalse&src=topads")
price = driver.find_element(By.CLASS_NAME,"price")
print(price.text)

driver.quit()