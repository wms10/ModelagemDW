import mysql.connector
import pandas as pd
import streamlit as st
#Conectar ao banco de dados
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2024',
    database='dw_populado_recife'
)
# Função para executar consultas e obter resultados em um DataFrame
def execute_query(query):
    return pd.read_sql_query(query, connection)
st.title('Despesas Orçamentárias de Recife-PE')

st.subheader('Data Warehouse das Despesas Orçamentárias de Recife-PE')

st.markdown("<h3 style='font-size: 16px;'>Wanderson Moura da Silva</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 16px;'>Fellipe de Brito Lira Batista</h3>", unsafe_allow_html=True)



# Feche a conexão após o uso
connection.close()
