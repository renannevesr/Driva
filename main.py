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
        
jobs = soup.find("ul", class_="zVzmE")
jobs_boxes = jobs.find_all('li')

for job in jobs:
    company = job.find("p", class_="cQyvth").text
    title = job.find("h2", class_="XNNQK").text
    span_elements = job.find_all("span", class_="cezNaf")
    print(span_elements)
    location = span_elements[0].text if len(span_elements) > 0 else ""
    work_modality = span_elements[1].text if len(span_elements) > 1 else ""
    job_type = span_elements[2].text if len(span_elements) > 2 else ""
    pcd_status = span_elements[2].text if len(span_elements) > 2 else ""
    date = job.find("p", class_="inqtnx").text
    
    
