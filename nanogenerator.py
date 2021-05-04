#nanogenerator 
from selenium import webdriver
import time

x="www.freenanofaucet.com/"
refreshrate=900
driver = webdriver.Chrome("Downloads/chromedriver_win32/chromedriver.exe")
nanoAdress = "nano_1xzmfroso1hyrtg93xn9hp88ka3hetkssqt3j6cepzrhz3mddb6rbuocu16w"
driver.get("http://"+x)

i=0
while True:
    i+=1
    inputElement = driver.find_element_by_id("nanoAddr")
    senditem = driver.find_element_by_id("getNano")
    inputElement.send_keys(nanoAdress)
    senditem.click()
    print('Number of try:')
    print(i)
    time.sleep(refreshrate)
    driver.back()
   
