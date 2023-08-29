import pandas as pd
import json

df = pd.read_csv('jobs_data.csv')

# Calcula o total de trabalhos
total_jobs = len(df)

# Realiza análises sobre as modalidades de trabalho, tipos de trabalho e localizações
work_modalities = df['Work Modality'].value_counts().to_dict()

# Calcula as porcentagens das modalidades de trabalho
work_modalities_percentages = {key: value / total_jobs * 100 for key, value in work_modalities.items()}

job_types = df['Job Type'].value_counts().to_dict()
locations = df['Location'].value_counts().to_dict()

# Extrai uma lista única de empresas
companies = df['Company'].unique().tolist()

# Realiza análises sobre as palavras-chave usadas na busca
words = df['Word'].value_counts().to_dict()

# Realiza análises sobre o status de PCD (Pessoa com Deficiência)
pcd_statuses = df['PCD Status'].value_counts().to_dict()

# Lista de palavras-chave para as quais queremos contar a ocorrência
word_types = ['estagio', 'jr', 'pleno', 'senior']
word_counts = {}

# Itera através das palavras-chave e conta suas ocorrências no DataFrame
for word_type in word_types:
    filtered_df = df[df['Word'] == word_type]
    word_counts[word_type] = len(filtered_df)

# Cria um dicionário com todas as análises realizadas, incluindo as porcentagens das modalidades de trabalho
analysis = {
    "total_jobs": total_jobs,
    "work_modalities": work_modalities,
    "work_modalities_percentages": work_modalities_percentages,
    "job_types": job_types,
    "locations": locations,
    "companies": companies,
    "words": words,
    "pcd_statuses": pcd_statuses,
    "word_counts": word_counts
}

# Cria um arquivo JSON e escreve as análises nele com formatação legível
with open('job_analysis_results.json', 'w') as json_file:
    json.dump(analysis, json_file, indent=4)
