import json

def le_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
        data = json.load(arquivo_json)
    return data
   