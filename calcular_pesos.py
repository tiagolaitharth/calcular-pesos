import streamlit as st

def calcular_peso_total_pavimento(numero_pavimento):
    peso_pavimento = 97
    peso_desconto = 39
    calcular_peso_total_pavimento = numero_pavimento * peso_pavimento
    peso_total_desconto = numero_pavimento * peso_desconto
    total_com_desconto = calcular_peso_total_pavimento - peso_total_desconto
    return calcular_peso_total_pavimento, total_com_desconto

def calcular_peso_cabine(numero_cabine):
    peso_cabine = 110
    peso_desconto_cabine = 39
    peso_total_cabine = numero_cabine * peso_cabine
    peso_total_descont = numero_cabine * peso_desconto_cabine
    total_com_descont = peso_total_cabine - peso_total_descont
    return peso_total_cabine, total_com_descont

st.title("Calcular Pesos")

if 'peso_total_pavimento' not in st.session_state:
    st.session_state.peso_total_pavimento = 0
if 'total_com_desconto_pavimento' not in st.session_state:
    st.session_state.total_com_desconto_pavimento = 0
if 'peso_total_cabine' not in st.session_state:
    st.session_state.peso_total_cabine = 0
if 'total_com_desconto_cabine' not in st.session_state:
    st.session_state.total_com_desconto_cabine = 0
if 'peso_total_soma' not in st.session_state:
    st.session_state.peso_total_soma = 0
if 'peso_total_liquido' not in st.session_state:
    st.session_state.peso_total_liquido = 0


col1, col2, = st.columns(2)

with col1:
    st.header("Pavimento")
    numero_pavimento = st.number_input("Digite a quantidade de pavimentos:",min_value=1,step=1)

if st.button("Calcular peso(Pavimento)", key="button pavimento"):
    st.session_state.peso_total_pavimento, st.session_state.total_com_desconto_pavimento = calcular_peso_total_pavimento(numero_pavimento)
    
with col2:
    st.header("Cabine")
    numero_cabine = st.number_input("Digite a quantidade de cabine", min_value=1, step=1)

if st.button("Calcular peso(Cabine)", key="button cabine"):
    st.session_state.peso_total_cabine, st.session_state.total_com_desconto_cabine = calcular_peso_cabine(numero_cabine)
             
if st.session_state.peso_total_pavimento is not None and st.session_state.total_com_desconto_pavimento is not None:
    st.subheader(f"Resultados para {numero_pavimento} pavimentos:")
    st.write(f"Peso bruto: {st.session_state.peso_total_pavimento} kg")
    st.write(f"Peso líquido: {st.session_state.total_com_desconto_pavimento} kg")

if st.session_state.peso_total_cabine is not None and st.session_state.total_com_desconto_cabine is not None:
    st.subheader(f"Resultados para {numero_cabine} cabines:")
    st.write(f"Peso bruto: {st.session_state.peso_total_cabine} kg")
    st.write(f"peso liquido: {st.session_state.total_com_desconto_cabine} kg")

st.subheader("Soma dos Pesos")

if st.button("Somar Pesos Totais", key="button soma"):
    st.session_state.peso_total_soma = (st.session_state.peso_total_pavimento + st.session_state.peso_total_cabine)
    st.session_state.peso_total_liquido = (st.session_state.total_com_desconto_pavimento + st.session_state.total_com_desconto_cabine)
    
st.write(f"Peso Total bruto: {st.session_state.peso_total_soma} kg")
st.write(f"Peso total liquido: {st.session_state.peso_total_liquido} kg")


