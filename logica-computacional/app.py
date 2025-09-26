from flask import Flask
import csv
import os

app = Flask(__name__)

# Nome do arquivo de dados
ARQUIVO_CSV = 'problemas.csv'

#Função para salvar problema com dados étnico-raciais
def salvar_problema(nome, problema, doenca, etnia):
    existe = os.path.isfile(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='uft-8') as file:
        escritor = csv.writer(file)
        if not existe:
            escritor.writerow(['nome', 'problema', 'doenca', 'etnia'])
        escritor.writerow([nome, problema, doenca, etnia])    

@app.route("/")
def home():
    return "este site foi desenvolvido para a disseminar de informações sobre o canhâmo meicinal"

@app.route("/sobre")
def sobre():
    return "A hempora foi criada para desmistificar o uso medicinal do cânhamo, combatendo o preconceito e desinformação sobre a Cannabis sativa. " \
    "A plataforma oferece informações científicas sobre "