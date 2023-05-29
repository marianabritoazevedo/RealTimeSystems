import subprocess
import streamlit as st
import pandas as pd
import os
import signal

st.set_page_config(layout = 'wide')

col_geral1, col_geral2 = st.columns(2)

def exibe_mensagem(texto):
    with col_geral1:
        st.success(texto)

# Botão relacionado à ação de filtragem de um processo
def funcao_filtro():
    with col_geral2:
        pid_filtro = st.text_input(label='Ação de filtragem - Insira o PID')
        if st.button('Filtrar'):
            pid = int(pid_filtro)
            processos = obter_processos_apos_filtro(pid)
            atualiza_tabela_apos_filtro(processos)
            exibe_mensagem('Filtragem realizada com sucesso, atualize a página para visualizar')

# Botão relacionado a ações kill, stop e continue de um processo
def funcoes_processo():  
    with col_geral2:
        pid_funcoes_processo = st.text_input(label='Ação de um processo - Insira o PID')
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button('Kill'):
                atualiza_tabela_funcoes_processo(pid_funcoes_processo, signal.SIGKILL, 'finalizado')
        with col2:
            if st.button('Stop'):
                atualiza_tabela_funcoes_processo(pid_funcoes_processo, signal.SIGSTOP, 'parado')
        with col3:
            if st.button('Cont'):
                atualiza_tabela_funcoes_processo(pid_funcoes_processo, signal.SIGCONT, 'continuado')
                
# Botão relacionado a informações da prioridade do processo
def prioridade_processo():
    with col_geral2:
        pid_prioridade_processo = st.text_input(label='Prioridade de um processo - Insira o PID')
        botao_prioridade = st.button('Verificar prioridade')

# Botão relacionado a informações da CPU do processo
def cpu_processo():
    with col_geral2:
        pid_cpu_processo = st.text_input(label='CPU de um processo - Insira o PID')
        botao_cpu = st.button('Verificar CPU')

# Textos iniciais a serem mostrados na tela
def textos_iniciais():
    with col_geral1:
        st.title('Gerenciador de processos')
        st.markdown('#### Desenvolvido por Deborah Moreira e Mariana Azevedo')
        st.markdown('###### Sistemas de Tempo Real')
        st.markdown('###### Professor Luiz Affonso Guedes')
    with col_geral2:
        st.markdown('#### Selecione a ação desejada')


# Obtém processos a partir de uma filtragem
def obter_processos_apos_filtro(pid):
    output = subprocess.check_output(["ps", "-auxc"])
    output_pid = subprocess.check_output(["grep", str(pid)], input=output)
    processos = output_pid.decode().splitlines()
    return processos

# Obtém todos os processos (sem a aplicação de nenhum filtro)
def obter_processos():
    output = subprocess.check_output(["ps", "-auxc"])
    processos = output.decode().splitlines()
    return processos

# Escreve em um csv os processos atualizados
def atualiza_tabela(processos):
    colunas = ['USUÁRIO', 'PID', '%CPU', '%MEM', 'VSZ', 'RSS', 'TTY', 'STATUS', 'START', 'TIME', 'NOME DO PROCESSO']
    dados = []
    for processo in processos[1:]:
        valores_do_processo = [valor for valor in processo.split(' ') if valor]
        dados.append(valores_do_processo)
    data = pd.DataFrame(dados, columns=colunas)
    data.to_csv('dados.csv', index=False)

#Escreve em um csv processos atualizados após o filtro
def atualiza_tabela_apos_filtro(processos):
    colunas = ['USUÁRIO', 'PID', '%CPU', '%MEM', 'VSZ', 'RSS', 'TTY', 'STATUS', 'START', 'TIME', 'NOME DO PROCESSO']
    dados = []
    for processo in processos:
        valores_do_processo = [valor for valor in processo.split(' ') if valor]
        dados.append(valores_do_processo)
    data = pd.DataFrame(dados, columns=colunas)
    data.to_csv('dados.csv', index=False)

# Lê os dados do csv e mostra a tabela de processos de usuário
def mostra_tabela(dados):
    dados = pd.read_csv('dados.csv')
    with col_geral1:
        st.dataframe(dados)

#Função que irá rodar a primeira vez quando o csv estiver vazio
def primeira_escrita_csv():
    processos = obter_processos()
    atualiza_tabela(processos)
    data = pd.read_csv('dados.csv')
    mostra_tabela(data)

# Sobrescreve o csv de acordo com a ação escolhida referente a um processo
def atualiza_tabela_funcoes_processo(pid_funcoes_processo, sinal, status):
    pid = int(pid_funcoes_processo)
    os.kill(pid, sinal)
    processos = obter_processos()
    atualiza_tabela(processos)
    texto = f'Processo {pid} {status}, atualize a página para verificar'
    exibe_mensagem(texto)

# Equivalente a dar o comando ps -aucx novamente no terminal ao colocar um programa novo para rodar, por exemplo
def botao_atualizar_tabela():
    with col_geral1:
        if st.button('Atualizar tabela'):
            processos = obter_processos()
            atualiza_tabela(processos)

#-------------------main------------------------------------
data = pd.read_csv('dados.csv')
if (len(data) == 0):
    textos_iniciais()
    primeira_escrita_csv()
    funcao_filtro()
    funcoes_processo()
    prioridade_processo()
    cpu_processo()
    botao_atualizar_tabela()
else:
    textos_iniciais()
    mostra_tabela(data)
    funcao_filtro()
    funcoes_processo()
    prioridade_processo()
    cpu_processo()
    botao_atualizar_tabela()

