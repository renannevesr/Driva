import requests, time, csv, re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
palavras = 'estagio'
browser.get("https://portal.gupy.io")
time.sleep(2)

browser.find_element(By.XPATH,'//*[@id="react-aria-3"]').send_keys(palavras)
browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div[2]/button').click()
time.sleep(2)
html_content = browser.page_source
soup = BeautifulSoup(html_content, 'html.parser')
