#import mysql.connector
import pandas as pd
import streamlit as st

# Conectar ao banco de dados
from sqlalchemy import create_engine, text

# Substitua 'sua_string_de_conexao' pela string de conexão do seu banco de dados
db_connection = 'mysql+pymysql://wanderson:12345678@35.247.239.74/dw_populado_recife'
engine = create_engine(db_connection)

# Estabeleça uma conexão
conn = engine.connect()

# Título do aplicativo
st.title("Análise OLAP - Data Warehouse")

st.title('Pergunta 2')

st.subheader('Qual o valor total liquidado e empenhado filtrado por órgão?')


# Consulta 2: Valor total liquidado e empenhado filtrado por órgão
# Adicione um menu suspenso para selecionar o órgão
orgaos = execute_query("SELECT DISTINCT nome FROM dim_empenho ORDER BY nome;")
orgao_selecionado = st.selectbox("Selecione o órgão:", ["Todos os Órgãos"] + orgaos['nome'].tolist())

# Modifique a consulta para considerar a seleção do órgão
if orgao_selecionado == "Todos os Órgãos":
    query2 = """
        SELECT dim_empenho.nome, 
               SUM(fato_pagamento.valor_empenhado) as total_empenhado,
               SUM(fato_pagamento.valor_pago) as total_pago
        FROM fato_pagamento
        JOIN dim_empenho ON fato_pagamento.cod_empenho = dim_empenho.codigo
        GROUP BY dim_empenho.nome;
    """
else:
    query2 = f"""
        SELECT dim_empenho.nome, 
               SUM(fato_pagamento.valor_empenhado) as total_empenhado,
               SUM(fato_pagamento.valor_pago) as total_pago
        FROM fato_pagamento
        JOIN dim_empenho ON fato_pagamento.cod_empenho = dim_empenho.codigo
        WHERE dim_empenho.nome = '{orgao_selecionado}'
        GROUP BY dim_empenho.nome;
    """

result2 = execute_query(query2)

# Exibindo os resultados da Consulta 2
st.write("Valor total liquidado e empenhado filtrado por órgão:")
st.dataframe(result2)
