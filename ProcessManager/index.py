import subprocess
import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide')

col_geral1, col_geral2 = st.columns(2)

# Função para obter a lista de processos
def obter_processos():
    output = subprocess.check_output(["ps", "-auxc"])
    processos = output.decode().splitlines()
    return processos

# Organiza a tabela que mostra os processos em execução
def organiza_tabela_processos(processos):
    colunas = ['USUÁRIO', 'PID', '%CPU', '%MEM', 'VSZ', 'RSS', 'TTY', 'STAT', 'START', 'TIME', 'NOME DO PROCESSO']
    dados = []
    for processo in processos[1:]:
        valores_do_processo = [valor for valor in processo.split(' ') if valor]
        dados.append(valores_do_processo)
    data = pd.DataFrame(dados, columns=colunas)
    with col_geral1:
        st.dataframe(data)

# Exibe os processos na interface
def atualiza_processos():
    processos = obter_processos()
    organiza_tabela_processos(processos)

def funcao_filtro():
    with col_geral2:
        pid_filtro = st.text_input(label='Ação de filtragem - Insira o PID')
        st.button('Filtrar')

def funcoes_processo():  
    with col_geral2:
        pid_funcoes_processo = st.text_input(label='Ação de um processo - Insira o PID')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button('Kill')
        with col2:
            st.button('Stop')
        with col3:
            st.button('Cont')

def prioridade_processo():
    with col_geral2:
        pid_prioridade_processo = st.text_input(label='Prioridade de um processo - Insira o PID')
        botao_prioridade = st.button('Verificar prioridade')

def cpu_processo():
    with col_geral2:
        pid_cpu_processo = st.text_input(label='CPU de um processo - Insira o PID')
        botao_cpu = st.button('Verificar CPU')

def pagina_inicial():
    with col_geral1:
        st.title('Gerenciador de processos')
        st.markdown('#### Desenvolvido por Deborah Moreira e Mariana Azevedo')
        st.markdown('###### Sistemas de Tempo Real')
        st.markdown('###### Professor Luiz Affonso Guedes')
    with col_geral2:
        st.markdown('#### Selecione a ação desejada')
    funcao_filtro()
    atualiza_processos()
    funcoes_processo()
    prioridade_processo()
    cpu_processo()

pagina_inicial()

