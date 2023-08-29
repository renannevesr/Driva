import time, csv, re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
job_data = []
#escolhi 4 palavras para realizar a busca no site.
words = ['estagio', 'jr', 'pleno', 'senior']
for word in words:
    browser.get("https://portal.gupy.io")
    time.sleep(1)

    browser.find_element(By.XPATH,'//*[@id="react-aria-3"]').send_keys(word)
    browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div[2]/button').click()
    time.sleep(2)
    html_content = browser.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    # Definindo um padrão de expressão regular para encontrar o número de vagas
    pattern = re.compile(r'(\d+)\s+vagas')
    # Analisei que a gupy retorna para o site a quantidade total de vagas e ela renderiza em blocos
    strong_elements = soup.find_all('strong')
    for element in strong_elements:
        text = element.get_text()
        match = pattern.search(text)
        if match:
            integer_value = int(match.group(1))
            # A gupy renderiza a parte de vagas por blocos de 9
            scrolls = integer_value // 9
            # Realizando o scroll da página para carregar mais blocos de 9
            for _ in range(scrolls):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)  
    # Removendo elementos indesejados do HTML para um carregamento mais rapido (imagens e SVGs)    
    elements_to_remove = ['img', 'svg']
    for element in elements_to_remove:
        matches = soup.find_all(element)
        for match in matches:
            match.decompose()
    html_content = browser.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    # Encontrando as informações dos trabalhos
    jobs = soup.find("ul", class_="zVzmE")
    # A gupo cria lista unica para cada vaga
    jobs_boxes = jobs.find_all('li')

    for job in jobs:
        #Apenas encontrei o padrão que o site foi construido para pegar todas as informações
        company = job.find("p", class_="cQyvth").text
        title = job.find("h2", class_="XNNQK").text
        date = job.find("p", class_="inqtnx").text
        #Todos esses campos abaixo estão com o mesmo nome da classe 
        span_elements = job.find_all("span", class_="cezNaf")
        # Criei uma logica para percorer os span na lista
        location = span_elements[0].text if len(span_elements) > 0 else ""
        work_modality = span_elements[1].text if len(span_elements) > 1 else ""
        job_type = span_elements[2].text if len(span_elements) > 2 else ""
        pcd_status = span_elements[3].text if len(span_elements) > 3 else ""
        
        # Adicionando informações do trabalho à lista de dados
        job_data.append([company, title, location, work_modality, job_type, pcd_status, date, word])
        
# Escrevendo os dados coletados em um arquivo CSV
with open('jobs_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company', 'Title', 'Location', 'Work Modality', 'Job Type', 'PCD Status', 'Date', 'Word'])
    writer.writerows(job_data)


