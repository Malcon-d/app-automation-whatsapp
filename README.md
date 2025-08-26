# Automação de Envio de Mensagens no WhatsApp 📲

Este projeto foi desenvolvido em Python com o objetivo de automatizar o envio de mensagens personalizadas via WhatsApp Web, a partir de uma planilha Excel.  
A automação foi criada para facilitar a comunicação com um grande número de alunos, evitando o envio manual de mensagens repetitivas.

---

  🚀 Funcionalidades
- Leitura de uma planilha Excel com dados dos alunos (nome, telefone, data de vencimento e valor).  
- Geração de mensagem personalizada para cada aluno.  
- Abertura automática do WhatsApp Web com a mensagem pronta para envio.  
- Uso de variável de ambiente para armazenar a chave PIX de forma segura.  

🛠️ Tecnologias e Bibliotecas Utilizadas
- Python  
- Openpyxl → leitura da planilha Excel  
- Webbrowser → abrir o WhatsApp Web  
- Urllib.parse (quote) → formatar a mensagem na URL  
- Time → controle de tempo entre envios  
- Pyautogui → interação com a interface (se necessário)  
- Os → acesso à variável de ambiente (chave PIX)

- ▶️ Como usar
1. Clone o repositório:  
   ```bash
   git clone https://github.com/Malcon-d/app-automation-whatsapp
