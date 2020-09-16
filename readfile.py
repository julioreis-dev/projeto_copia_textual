import pandas as pd
import csv
from datetime import datetime, date, timedelta
from openpyxl import load_workbook

def ler_e_inserir_arquivo(caminho_arquivo):
    with open(caminho_arquivo, newline='', encoding="latin-1") as arquivo:
        delimitador = csv.Sniffer().sniff(arquivo.read(1024), delimiters=",")
        arquivo.seek(0)
        conteudo = csv.reader(arquivo, delimitador)
        dados = list(conteudo)
        x = len(dados)
        for coluna in range(1, len(dados)+1):
            info = dados[coluna]
            info[1] = datetime.strptime(info[1], '%I:%M %p')
            tratamento_dos_dados = pd.DataFrame({
                'timestamp': datetime.strptime(info[0], '%m/%d/%Y').strftime('%Y-%m-%d'),
                'ACTIVE POWER': info[1],
                'COMS STATUS': info[2],
                '': info[3]
        })
            print(tratamento_dos_dados)
        #tratamento_dos_dados.to_frame('count')
        #tratamento_dos_dados.to_csv(caminho_arquivo)
        tratamento_dos_dados.to_excel(caminho_arquivo)
        tratamento_dos_dados.save()



caminho = r'C:\Users\julio.firmino\Desktop\plantas\Sao Pedro-data-2020-01-01_2020-01-30-Inverter-SP2-1-IN1.csv'
ler_e_inserir_arquivo(caminho)