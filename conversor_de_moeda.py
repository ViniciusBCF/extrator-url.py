from extrator_url import ExtratorURL
import re
import math

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_conversao = int(quantidade) * VALOR_DOLAR
    print(quantidade + ' dólares equivalem a: ' + str(valor_conversao) + ' reais.')
elif moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_conversao = int(quantidade) / VALOR_DOLAR
    print(quantidade + ' reais equivalem a: ' + str(valor_conversao) + ' dólares.')
else:
    print('Esse câmbio não está disponível.')