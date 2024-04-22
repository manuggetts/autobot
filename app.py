from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

def login(driver, email, senha):
    email_input = driver.find_element(By.XPATH, "//input[@id='email']")
    email_input.send_keys(email)

    senha_input = driver.find_element(By.XPATH, "//input[@id='senha']")
    senha_input.send_keys(senha)

    botao_entrar = driver.find_element(By.XPATH, "//button[@id='Entrar']")
    botao_entrar.click()

def preencher_formulario(driver, dados_empresa):
    nome_empresa, email_empresa, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionarios, data_fundacao = dados_empresa

    driver.find_element(By.ID, 'nomeEmpresa').send_keys(nome_empresa)
    driver.find_element(By.ID, 'emailEmpresa').send_keys(email_empresa)
    driver.find_element(By.ID, 'telefoneEmpresa').send_keys(telefone)
    driver.find_element(By.ID, 'enderecoEmpresa').send_keys(endereco)
    driver.find_element(By.ID, 'cnpj').send_keys(cnpj)
    driver.find_element(By.ID, 'areaAtuacao').send_keys(area_atuacao)
    driver.find_element(By.ID, 'numeroFuncionarios').send_keys(quantidade_de_funcionarios)
    driver.find_element(By.ID, 'dataFundacao').send_keys(data_fundacao)

    driver.find_element(By.ID, 'Cadastrar').click()

def main():
    driver = webdriver.Chrome()
    driver.get('https://contabilidade-devaprender.netlify.app/')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))

    login(driver, 'admin@contabilidade.com', 'cont123')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nomeEmpresa')))

    empresas = openpyxl.load_workbook('./empresas.xlsx')
    pagina_empresas = empresas['dados empresas']

    for linha in pagina_empresas.iter_rows(min_row=2, values_only=True):
        preencher_formulario(driver, linha)

    driver.quit()

if __name__ == "__main__":
    main()