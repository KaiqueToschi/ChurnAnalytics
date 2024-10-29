# Visão Geral
O **ChurnAnalytics** é um projeto desenvolvido para prever a evasão de clientes (churn) para empresas B2B, utilizando técnicas de machine learning. A solução analisa dados de clientes e prevê o risco de churn, permitindo que a empresa adote ações proativas de retenção.

# Arquitetura

### Camada de Dados
Para o tratamento dos dados, usamos a biblioteca **Pandas** para carregar e preparar o conjunto de dados fictício. O modelo considera variáveis como **Gasto Mensal** e **Interações com Suporte** para identificar padrões de churn entre os clientes.

### Camada de Modelagem
A previsão de churn é feita usando o **RandomForestClassifier** do **Scikit-learn**. O modelo é treinado e testado com dados rotulados, onde clientes em risco de churn são identificados com base em variáveis comportamentais.

### Camada de Apresentação
A interface do projeto foi implementada com **Streamlit**, proporcionando uma visualização interativa dos dados e das previsões. Nessa interface, o usuário pode ajustar valores de entrada (ex.: gasto mensal, interações com suporte) para observar a probabilidade de churn de um cliente específico.

# Design Patterns Utilizados

- **Modelagem Preditiva**: Utilizamos machine learning para identificar padrões de churn e prever quais clientes têm maior probabilidade de evasão.
- **Segmentação de Clientes**: O modelo classifica clientes com base em características semelhantes, permitindo uma abordagem de retenção mais personalizada.
- **Controller**: A camada de apresentação atua como controlador, integrando a lógica do modelo com a interface para o usuário final.

# Arquitetura do Projeto

Abordagem Monolítica: Toda a lógica da aplicação está contida em um único projeto, o que facilita o desenvolvimento e manutenção neste estágio inicial.

### Justificativas para a Abordagem Monolítica

1. **Simplicidade de Desenvolvimento e Manutenção**
   - **Implementação Centralizada**: Todos os componentes estão agrupados em uma única base de código, tornando o desenvolvimento e o teste mais diretos.
   
2. **Redução de Custos e Dependências**
   - **Infraestrutura Simples**: A abordagem monolítica reduz a necessidade de recursos adicionais e facilita a implantação e manutenção inicial.

# Futuro Planejado
Para as próximas fases, planeja-se adicionar novas funcionalidades, incluindo:

- **Integração de Feedback**: Uma camada de feedback dos clientes para identificar as principais causas de churn e ajustar o modelo de acordo.
- **Segmentação Avançada**: Agrupamento dos clientes por características comportamentais adicionais para uma previsão mais precisa.

# Instruções para Executar o Projeto

### Pré-requisitos
- **Python 3.x**: Certifique-se de que o Python está instalado. Você pode baixá-lo [aqui](https://www.python.org/downloads/).
- **Bibliotecas**: Instale as dependências listadas em `requirements.txt`.

### Configuração

1. **Clone o Repositório**
    ```bash
    git clone https://github.com/KaiqueToschi/ChurnAnalytics.git
    cd ChurnAnalytics
    ```

2. **Instale as Dependências**
    ```bash
    pip install -r requirements.txt
    ```

3. **Execute a Interface Streamlit**
    ```bash
    streamlit run app.py
    ```

A interface permitirá que você visualize os dados dos clientes e preveja o churn com base nas variáveis fornecidas. Esta versão inicial oferece uma base para expandir a análise de churn e personalizar ações de retenção.
