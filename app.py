import openpyxl
import webbrowser
from urllib.parse import quote
from time import sleep
import pyautogui
import os

webbrowser.open('https://web.whatsapp.com/') # abre o navegador
sleep(20) # tempo apos abertura

caminho = r'C:\Users\mdonovan\OneDrive - Simpress\Documentos\Malcon\dados.xlsx' # caminho do arquivo excel
arquivo = openpyxl.open(caminho) # variavel para abrir o doc
page = arquivo['Planilha1'] # seleciona a aba onde esta o arquivo no excel

# For para iterar sobre todas as linhas no doc, começando pela linha 2 (min_row=2)
for linha in page.iter_rows(min_row=2):
     nome = linha[0].value # acessa o valor da coluna, a partir da segunda linha
     numero = linha[1].value # acessa o valor da coluna, a partir da segunda linha
     dt_vencimento = linha[2].value # acessa o valor da coluna, a partir da segunda linha
     valor = linha[3].value # acessa o valor da coluna, a partir da segunda linha
     pix =  os.environ.get('CHAVE_PIX') # variavel de ambiente que armazena a chave pix

     # mensagem que sera enviada para o numero
     mensagem = f"Olá, {nome}! Sua mensalidade vence no dia {dt_vencimento.strftime('%d/%m/%Y')}, com o valor de R${valor}. Por favor, pagar via PIX, para a chave {pix}"

     # try para captar possiveis erros de envio
     try:        
          # link que abrira a conversa com numero de acordo com a iteração da variavel 'numero'
          link_msg = f'https://web.whatsapp.com/send?phone={numero}&text={quote(mensagem)}' 
          # para abrir o navegador diretamente no link
          webbrowser.open(link_msg)
          sleep(15)
          pyautogui.press('enter') # press para enviar a mensagem
          sleep(5)
          pyautogui.hotkey('ctrl', 'w') # pyautogui para fechar a aba a cada iteração
          sleep(5)
   
     except:
          print(f'Não foi possivel enviar a mensagem para {nome}!')
          # whit open criara um arquivo csv com os erros de envio
          with open('erros.csv', 'a', newline=" ", encoding='UTF-8') as file:
               file.write(f'Nome: {nome}, Telefone: {numero}')
     



        
