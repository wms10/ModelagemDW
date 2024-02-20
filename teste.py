import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text

# Substitua 'sua_string_de_conexao' pela string de conexão do seu banco de dados
db_connection = 'mysql+pymysql://wanderson:12345678@35.247.239.74/dw_populado_recife'
engine = create_engine(db_connection)

# Estabeleça uma conexão
conn = engine.connect()
st.title('Despesas Orçamentárias de Recife-PE')

st.subheader('Data Warehouse das Despesas Orçamentárias de Recife-PE')

st.markdown("<h3 style='font-size: 16px;'>Wanderson Moura da Silva</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 16px;'>Fellipe de Brito Lira Batista</h3>", unsafe_allow_html=True)



# Feche a conexão após o uso
conn.close()
