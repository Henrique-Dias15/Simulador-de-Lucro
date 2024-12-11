import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from io import BytesIO

# Constantes
HORAS_TOTAIS = 8

def calcular_pessoas_chegadas(total_pessoas, hora_interesse):
    """
    Calcula o número de pessoas que chegaram até a hora de interesse, com base em uma distribuição Beta.
    """
    hora_normalizada = hora_interesse / HORAS_TOTAIS
    alpha, beta = 2.5, 4.0  # Parâmetros da distribuição Beta
    probabilidade_cumulativa = stats.beta.cdf(hora_normalizada, alpha, beta)
    return (total_pessoas * probabilidade_cumulativa).astype(int)

def calcular_valor_arrecadado(ingressos_vendidos, lotes, aumento_por_lote, preco_inicial):
    """
    Calcula o valor arrecadado com base na distribuição Beta para os lotes de ingressos.
    """
    porcentagem_cortesia = 0.05
    ingressos_pagos = (ingressos_vendidos * (1 - porcentagem_cortesia)).astype(int)
    
    x = np.linspace(0, 1, lotes + 1)
    alpha, beta = 2, 5
    distribuicao = stats.beta.pdf(x, alpha, beta)
    proporcoes = distribuicao / distribuicao.sum()

    valor_total = np.zeros_like(ingressos_pagos, dtype=float)
    preco_atual = preco_inicial

    for i in range(lotes):
        ingressos_no_lote = (proporcoes[i] * ingressos_pagos).astype(int)
        valor_total += ingressos_no_lote * preco_atual
        preco_atual += aumento_por_lote

    return valor_total

def calcular_gastos(total_pessoas, local_300, local_700, lineup, staff, divulgacao, horas_openbar, valor_openbar):
    """
    Calcula os gastos totais do evento.
    """
    gastos_locais = np.where(total_pessoas <= 300, local_300, local_700)
    gastos_seg = np.where(total_pessoas <= 300, staff * 3, staff * 4)
    gastos_open_bar = valor_openbar * calcular_pessoas_chegadas(total_pessoas, horas_openbar)
    gastos_totais = gastos_locais + gastos_seg + gastos_open_bar + lineup + divulgacao
    return gastos_totais

def calcular_receitas(total_pessoas, valor_inicial, incremento, lotes, margem_bar, gasto_por_pessoa):
    """
    Calcula as receitas do evento com base nas vendas de ingressos e bar.
    """
    receitas = {
        "Ingressos": calcular_valor_arrecadado(total_pessoas, lotes, incremento, valor_inicial),
        "Bar": total_pessoas * gasto_por_pessoa * margem_bar
    }
    return sum(receitas.values())

def calcular_lucro(total_pessoas, valor_inicial, incremento, lotes, margem_bar, gasto_por_pessoa, local_300, local_700, lineup, staff, divulgacao, horas_openbar, valor_openbar):
    """
    Calcula o lucro do evento.
    """
    receitas = calcular_receitas(total_pessoas, valor_inicial, incremento, lotes, margem_bar, gasto_por_pessoa)
    gastos = calcular_gastos(total_pessoas, local_300, local_700, lineup, staff, divulgacao, horas_openbar, valor_openbar)
    return receitas - gastos

def calcular_pontos_equilibrio(lucro, total_pessoas):
    """
    Identifica os pontos de equilíbrio do evento.
    """
    lucro_0_300 = lucro[total_pessoas <= 300]
    pessoas_0_300 = total_pessoas[total_pessoas <= 300]
    ponto_equilibrio_0_300 = pessoas_0_300[np.argmax(lucro_0_300 >= 0)]

    lucro_301_700 = lucro[total_pessoas > 300]
    pessoas_301_700 = total_pessoas[total_pessoas > 300]

    if np.any(lucro_301_700 >= 0):
        ponto_equilibrio_301_700 = pessoas_301_700[np.argmax(lucro_301_700 >= 0)]
    else:
        ponto_equilibrio_301_700 = ponto_equilibrio_0_300

    return ponto_equilibrio_0_300, ponto_equilibrio_301_700

def criar_botao_download(fig):
    """
    Cria um botão para download do gráfico.
    """
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    st.download_button(
        label="Baixar Gráfico",
        data=buf,
        file_name="grafico_lucro.png",
        mime="image/png"
    )

# Configurações da página
st.title("Última do Semestre")
st.subheader("Simulador de Lucro")

# Entradas de gastos
st.write("## Configurações de Gastos")
col1, col2 = st.columns(2)
with col1:
    local_300 = st.number_input("Local para até 300 Pessoas", min_value=0, value=5000)
    horas_openbar = st.number_input("Horas de Open Bar", min_value=0, max_value=24, value=2)
with col2:
    local_700 = st.number_input("Local para até 700 Pessoas", min_value=0, value=10000)
    valor_openbar = st.number_input("Valor do Open Bar por Pessoa/Hora", min_value=0, value=25)
col1, col2, col3 = st.columns(3)
with col1:
    staff = st.number_input("Custo por Segurança/Brigadista", min_value=0, value=150)
with col2:
    lineup = st.number_input("Custo com Lineup", min_value=0, value=1000)
with col3:
    divulgacao = st.number_input("Custo com Divulgação", min_value=0, value=1000)

# Entradas de receitas
st.write("## Configurações de Receitas")
col1, col2, col3 = st.columns(3)
with col1:
    valor_inicial = st.number_input("Valor Inicial do Ingresso", min_value=10, value=25)
with col2:
    incremento = st.number_input("Incremento por Lote", min_value=1, value=10)
with col3:
    qtd_lotes = st.number_input("Quantidade de Lotes", min_value=1, value=5)
col1, col2 = st.columns(2)
with col1:
    gasto_por_pessoa = st.number_input("Gasto Médio por Pessoa no Bar", min_value=0, value=0)
with col2:
    margem_bar = st.number_input("Margem do Bar (%)", min_value=0, value=250) / 100

# Cálculos
st.write("## Resultados")
total_pessoas = np.arange(1, 701)
lucro = calcular_lucro(total_pessoas, valor_inicial, incremento, qtd_lotes, margem_bar, gasto_por_pessoa, local_300, local_700, lineup, staff, divulgacao, horas_openbar, valor_openbar)
ponto_equilibrio_0_300, ponto_equilibrio_301_700 = calcular_pontos_equilibrio(lucro, total_pessoas)

# Gráfico
fig, ax = plt.subplots()
ax.plot(total_pessoas, lucro, label="Lucro")
ax.axhline(0, color="gray", linestyle="--", alpha=0.7)
ax.axvline(ponto_equilibrio_0_300, color="green", linestyle="--", label="Equilíbrio (0-300)")
ax.axvline(ponto_equilibrio_301_700, color="blue", linestyle="--", label="Equilíbrio (301-700)")
ax.set_xlabel("Total de Pessoas")
ax.set_ylabel("Lucro (R$)")
ax.set_title("Lucro em Função do Total de Pessoas")
ax.legend()

st.pyplot(fig)

st.write("### Resultados")
col1, col2 = st.columns(2)
with col1:
    st.write("#### Pontos de Equilíbrio")
    st.write(f"Ponto de Equilíbrio (0-300 Pessoas): {ponto_equilibrio_0_300} pessoas")
    st.write(f"Ponto de Equilíbrio (301-700 Pessoas): {ponto_equilibrio_301_700} pessoas")
with col2:
    st.write("#### Lucros Máximos")
    if np.any(total_pessoas == 300):
        lucro_300 = lucro[np.where(total_pessoas == 300)][0]
        st.write(f"Lucro com 300 Pessoas: R$ {lucro_300:.2f}")
    else:
        st.write("Lucro com 300 Pessoas: Dados não disponíveis")
    if np.any(total_pessoas == 699):
        lucro_700 = lucro[-1]
        st.write(f"Lucro com 700 Pessoas: R$ {lucro_700:.2f}")
    else:
        st.write("Lucro com 700 Pessoas: Dados não disponíveis")

# Análises Estatísticas
receitas_totais = calcular_receitas(total_pessoas, valor_inicial, incremento, qtd_lotes, margem_bar / 100, gasto_por_pessoa)
gastos_totais = calcular_gastos(total_pessoas, local_300, local_700, lineup, staff, divulgacao, horas_openbar, valor_openbar)

st.write("#### Outras Análises")
col1, col2, col3 = st.columns(3)
with col1:
    if np.any(total_pessoas == 300):
        margem_lucro_300 = (lucro_300 / receitas_totais[np.where(total_pessoas == 300)][0]) * 100
        st.write(f"Margem de Lucro com 300 Pessoas: {margem_lucro_300:.2f}%")
with col2:
    if np.any(total_pessoas == 699):
        margem_lucro_700 = (lucro_700 / receitas_totais[np.where(total_pessoas == 699)][0]) * 100
        st.write(f"Margem de Lucro com 700 Pessoas: {margem_lucro_700:.2f}%")
with col3:
    lucro_medio = np.mean(lucro)
    st.write(f"Lucro Médio ao Longo do Evento: R$ {lucro_medio:.2f}")
