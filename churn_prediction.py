import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregar dados fictícios
data = pd.DataFrame({
    'ClienteID': range(1, 101),
    'GastoMensal': [abs(x) for x in range(-50, 50)],
    'InteracoesSuporte': [x % 5 for x in range(1, 101)],
    'Churn': [1 if x % 10 == 0 else 0 for x in range(1, 101)]
})

# Preparo dos dados
X = data[['GastoMensal', 'InteracoesSuporte']]
y = data['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinamento do modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Avaliação do modelo
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Acurácia do modelo: {accuracy * 100:.2f}%")
