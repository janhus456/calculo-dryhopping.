import streamlit as st

def calcular_dryhopping(dryhopping_anterior, oleo_anterior, oleo_novo):
    if oleo_novo == 0:
        return "Erro: O óleo do novo lote não pode ser zero."
    return (dryhopping_anterior * oleo_anterior) / oleo_novo

st.title("Calculadora de DryHopping")

st.write("Insira os valores para calcular a quantidade necessária de DryHopping no novo lote.")

dryhopping_anterior = st.number_input("DryHopping Anterior (g)", min_value=0.0, value=12000.0)
oleo_anterior = st.number_input("Óleo/100g (Lote Anterior)", min_value=0.0, value=1.2)
oleo_novo = st.number_input("Óleo/100g (Novo Lote)", min_value=0.0, value=1.3)

if st.button("Calcular"):
    resultado = calcular_dryhopping(dryhopping_anterior, oleo_anterior, oleo_novo)
    st.success(f"A quantidade necessária de DryHopping para o novo lote é: {resultado:.2f} g")
