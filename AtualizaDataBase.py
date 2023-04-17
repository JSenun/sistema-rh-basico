import json

def le_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
        data = json.load(arquivo_json)
    return data

def atualiza_arquivo_json(nome_arquivo, dados_processados_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        new_data = json.dumps(dados_processados_arquivo)
        new_data = json.loads(new_data)
        json.dump(new_data, arquivo_json)