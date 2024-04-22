# 👾 Automatização de Preenchimento de Formulários com Python e Selenium 🤖

Este projeto consiste em uma automação desenvolvida em Python utilizando a biblioteca Selenium para preenchimento automatizado de formulários em um site de contabilidade. Ele visa aumentar a eficiência e reduzir erros manuais ao inserir dados de empresas em um sistema online.

![OIG2](https://github.com/manuggetts/autobot/assets/141872152/815ac3dd-4d96-4d0a-94fe-d2a24fa5e131 "Imagem gerada pelo Copilot.")

## Funcionalidades

- Realiza login no site de contabilidade.
- Extrai dados de uma planilha Excel contendo informações (nome, email etc) sobre empresas.
- Preenche os campos do formulário de cadastro de empresas de forma automatizada.
- Clica no botão de cadastro para submeter os dados.
- Repete a operação.

## Requisitos

- Python 3.x
- Selenium
- Chrome
- ChromeDriver (opcional, dependendo da configuração do ambiente)

## Como Usar

1. Clone este repositório:

```
git clone https://github.com/manuggetts/autobot.git
```

2. Instale as dependências:

```
pip install selenium openpyxl
```

3. Execute o script Python:

```
python app.py
```


### Observações

- Ao executar o script, aguarde enquanto o navegador Google Chrome é aberto automaticamente e os formulários são preenchidos de forma automatizada.
- Certifique-se de que o arquivo `empresas.xlsx` está localizado no mesmo diretório que o arquivo `app.py` e que contém os dados das empresas a serem cadastradas.

## Configuração

- Edite o arquivo `empresas.xlsx` para adicionar os dados das empresas que deseja cadastrar.
- Certifique-se de fornecer as credenciais de login no arquivo `app.py`.

## Referências 📌
- <a href="https://www.youtube.com/@DevAprender" target="_blank">Dev Aprender</a>

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão, melhoria ou correção, sinta-se à vontade para abrir uma [issue](https://github.com/manuggetts/autobot/issues) ou enviar um [pull request](https://github.com/manuggetts/autobot/pulls).

Obrigada por ajudar a melhorar este projeto!
