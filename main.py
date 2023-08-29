import requests, time, csv, re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
palavras = 'estagio'
browser.get("https://portal.gupy.io")
time.sleep(1)

browser.find_element(By.XPATH,'//*[@id="react-aria-3"]').send_keys(palavras)
browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div[2]/button').click()
time.sleep(2)
html_content = browser.page_source
soup = BeautifulSoup(html_content, 'html.parser')


pattern = re.compile(r'(\d+)\s+vagas')

strong_elements = soup.find_all('strong')
for element in strong_elements:
    text = element.get_text()
    match = pattern.search(text)
    if match:
        integer_value = int(match.group(1))
        scrolls = integer_value // 9

        for _ in range(scrolls):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)  
            
elements_to_remove = ['img', 'svg']

for element in elements_to_remove:
    matches = soup.find_all(element)
    for match in matches:
        match.decompose()