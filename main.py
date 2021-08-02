import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto

# Config Tkinter
janela = Tk()
janela.title("Cotação Atual de Moedas")

texto_inicial = Label(janela, text="Clique abaixo para atualizar as cotações do Euro/Dólar/BTC")
texto_inicial.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Atualizar Cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, pady=10)

janela.mainloop()