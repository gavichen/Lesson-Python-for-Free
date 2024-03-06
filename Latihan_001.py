
print("FILE INI UNTUK LATIHAN CONTOH AKSES DATA DARI WEB")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("01. MEMBUAT KONEKSI DENGAN BROWSER untuk Akses Web : ")
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

cdp = "C:/developer/chromedriver.exe"
service = Service(executable_path=cdp)
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
driver.quit()