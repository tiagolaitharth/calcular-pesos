import streamlit as st

# Funções para calcular os pesos brutos e líquidos
def calcular_peso_total_pavimento(numero_pavimento):
    peso_pavimento = 97  # Peso bruto de cada pavimento
    peso_caixa_pavimento = 39  # Peso líquido da caixa de pavimento
    peso_total_pavimento = numero_pavimento * peso_pavimento  # Peso bruto total
    peso_total_caixa_pavimento = numero_pavimento * peso_caixa_pavimento  # Peso líquido total
    return peso_total_pavimento, peso_total_caixa_pavimento

def calcular_peso_total_cabine(numero_cabine):
    peso_cabine = 110  # Peso bruto de cada cabine
    peso_caixa_cabine = 39  # Peso líquido da caixa de cabine
    peso_total_cabine = numero_cabine * peso_cabine  # Peso bruto total
    peso_total_caixa_cabine = numero_cabine * peso_caixa_cabine  # Peso líquido total
    return peso_total_cabine, peso_total_caixa_cabine

# Título
st.title("Calculadora de Pesos")

# Armazenamento dos resultados no estado da sessão
if 'peso_total_pavimento' not in st.session_state:
    st.session_state.peso_total_pavimento = 0
if 'peso_total_caixa_pavimento' not in st.session_state:
    st.session_state.peso_total_caixa_pavimento = 0
if 'peso_total_cabine' not in st.session_state:
    st.session_state.peso_total_cabine = 0
if 'peso_total_caixa_cabine' not in st.session_state:
    st.session_state.peso_total_caixa_cabine = 0
if 'peso_total_soma_bruto' not in st.session_state:
    st.session_state.peso_total_soma_bruto = 0
if 'peso_total_soma_liquido' not in st.session_state:
    st.session_state.peso_total_soma_liquido = 0

# Layout com 2 colunas
col1, col2 = st.columns(2)

with col1:
    st.header("Pavimento")
    numero_pavimento = st.number_input("Digite a quantidade de pavimentos:", min_value=1, step=1)

if st.button("Calcular peso (Pavimento)", key="button_pavimento"):
    st.session_state.peso_total_pavimento, st.session_state.peso_total_caixa_pavimento = calcular_peso_total_pavimento(numero_pavimento)

with col2:
    st.header("Cabine")
    numero_cabine = st.number_input("Digite a quantidade de cabines:", min_value=1, step=1)

if st.button("Calcular peso (Cabine)", key="button_cabine"):
    st.session_state.peso_total_cabine, st.session_state.peso_total_caixa_cabine = calcular_peso_total_cabine(numero_cabine)

# Exibir resultados de pavimento
if st.session_state.peso_total_pavimento > 0 and st.session_state.peso_total_caixa_pavimento > 0:
    st.subheader(f"Resultados para {numero_pavimento} pavimentos:")
    st.write(f"Peso bruto: {st.session_state.peso_total_pavimento} kg")
    st.write(f"Peso líquido (caixas): {st.session_state.peso_total_caixa_pavimento} kg")

# Exibir resultados de cabine
if st.session_state.peso_total_cabine > 0 and st.session_state.peso_total_caixa_cabine > 0:
    st.subheader(f"Resultados para {numero_cabine} cabines:")
    st.write(f"Peso bruto: {st.session_state.peso_total_cabine} kg")
    st.write(f"Peso líquido (caixas): {st.session_state.peso_total_caixa_cabine} kg")

# Somar os pesos totais
st.subheader("Soma dos Pesos Totais")
if st.button("Somar Pesos Totais", key="button_soma"):
    st.session_state.peso_total_soma_bruto = st.session_state.peso_total_pavimento + st.session_state.peso_total_cabine
    st.session_state.peso_total_soma_liquido = st.session_state.peso_total_caixa_pavimento + st.session_state.peso_total_caixa_cabine

# Exibir o peso total bruto e líquido
st.write(f"Peso total bruto: {st.session_state.peso_total_soma_bruto} kg")
st.write(f"Peso total líquido: {st.session_state.peso_total_soma_liquido} kg")


