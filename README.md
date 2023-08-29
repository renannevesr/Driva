# Processo seletivo da Driva

Este script Python realiza análises sobre dados de vagas de emprego coletados de um site de busca de empregos. Ele extrai informações como modalidades de trabalho, tipos de trabalho, localizações e muito mais, gerando um arquivo JSON com os resultados.

## Requisitos

Certifique-se de ter o Python (versão 3.x) instalado no seu sistema. Além disso, você precisará das seguintes bibliotecas:

- `pandas`
- `json`
- `beautifulsoup4`
- `selenium`

## Uso

1. Primeiro, execute o script `scrape_jobs.py` para coletar os dados das vagas de emprego e salvar no arquivo `jobs_data.csv`.

2. Em seguida, execute o script `analyze_jobs.py` para realizar análises sobre os dados coletados e gerar um arquivo JSON com os resultados chamado `job_analysis_results.json`.

## Entendendo os Resultados

O arquivo `job_analysis_results.json` contém várias análises, incluindo:

- Total de vagas de emprego
- Distribuição de modalidades de trabalho
- Distribuição de tipos de trabalho
- Distribuição de localizações
- Lista única de empresas
- Distribuição das palavras-chave usadas na busca
- Distribuição dos status de PCD (Pessoa com Deficiência)
- Contagem de ocorrências para palavras-chave específicas

## Personalização

Você pode personalizar as palavras-chave que deseja analisar modificando a lista `word_types` no script `analyze_jobs.py`.

## Conclusão
O JSON analisado é uma amostra limitada para fins de visualização, onde os dados foram divididos em blocos de 500 para facilitar o deslocamento. No cenário real, ao coletar as vagas de emprego da página, o método correto seria dividir os dados em blocos de 9. Isso garantiria que todas as vagas da página fossem incluídas na análise, fornecendo uma visão mais completa
das estatísticas. Portanto, ao realizar a análise completa, certifique-se de aplicar a divisão correta para garantir resultados precisos e representativos.
### Total de Vagas de Emprego
Foram coletadas um total de 190 vagas de emprego.

### Modalidades de Trabalho
- A maioria das vagas (77.89%) é para trabalho presencial.
- Um percentual significativo de vagas (22.11%) é para trabalho remoto.

### Tipos de Trabalho
- A maioria das vagas (61.58%) é de trabalho efetivo.
- Uma quantidade considerável de vagas (29.47%) é de estágio.
- Um número menor de vagas (6.32%) é para trabalho como pessoa jurídica.
- Há vagas de banco de talentos, temporário e associado, mas em proporções menores.

### Localizações
- A cidade "São Paulo - SP" continua sendo a líder em número de vagas, com 25.79%.
- Outras cidades como "Curitiba - PR" e "Porto Alegre - RS" também têm presença significativa.

### Palavras-chave
- A palavra-chave "estagio" é a mais comum, presente em 60 vagas de emprego.
- As palavras-chave "pleno" e "senior" aparecem em 50 e 40 vagas, respectivamente.
- A palavra-chave "jr" aparece em 40 vagas de emprego.

### Status de PCD
- Cerca de 74.21% das vagas são para pessoas com deficiência (PcD).

