import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Dados fictícios
data = pd.DataFrame({
    'ClienteID': range(1, 101),
    'GastoMensal': [abs(x) for x in range(-50, 50)],
    'InteracoesSuporte': [x % 5 for x in range(1, 101)],
    'Churn': [1 if x % 10 == 0 else 0 for x in range(1, 101)]
})

# Treinamento do modelo
X = data[['GastoMensal', 'InteracoesSuporte']]
y = data['Churn']
model = RandomForestClassifier()
model.fit(X, y)

# Interface Streamlit
st.title("Previsão de Churn")
st.write("Visualize a previsão de churn para clientes.")

# Exibir dados
st.subheader("Dados de Clientes")
st.write(data)

# Entrada do usuário para previsão
gasto_mensal = st.slider("Gasto Mensal", min_value=0, max_value=100, value=50)
interacoes_suporte = st.slider("Interações com Suporte", min_value=0, max_value=5, value=1)

# Prever churn
resultado = model.predict([[gasto_mensal, interacoes_suporte]])
st.write("Probabilidade de Churn:", "Sim" if resultado[0] == 1 else "Não")
