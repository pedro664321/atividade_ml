import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Carregar os dados (ajuste o nome do arquivo se necessário)
df = pd.read_csv("Pasta1.csv", skiprows=1)

# 2. Configurar o tamanho do gráfico
plt.figure(figsize=(14, 8))

# Pegar a lista de produtos únicos
produtos = df['Produto'].unique()

# Cores específicas para cada produto
cores = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#ff7f0e']

# 3. Iterar sobre cada produto para calcular a reta, o R² e plotar
for idx, prod in enumerate(produtos):
    # Filtrar apenas os dados do produto atual
    df_prod = df[df['Produto'] == prod].sort_values('Mês')
    
    # Extrair x e y como listas/arrays
    x = df_prod['Mês'].values
    y = df_prod['Vendas (unidades)'].values
    n = len(x)
    
    # Variáveis auxiliares para somatórios
    soma_x = 0
    soma_y = 0
    soma_xy = 0
    soma_x2 = 0
    
    # PASSO A: Fazer os somatórios com um laço simples
    for i in range(n):
        soma_x += x[i]
        soma_y += y[i]
        soma_xy += x[i] * y[i]
        soma_x2 += x[i] * x[i]
    
    # PASSO B: Cálculo dos coeficientes da reta (a e b)
    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x * soma_x)
    b = (soma_y - a * soma_x) / n
    
    # PASSO C: Cálculo do R² (exatamente como no exemplo de JS)
    # Primeiro a média de y
    media_y = soma_y / n
    
    sq_total = 0
    sq_res = 0
    
    for i in range(n):
        # Valor que a reta prevê para aquele 'x'
        y_estimado = a * x[i] + b
        
        # Soma dos quadrados total e residual
        sq_total += (y[i] - media_y) ** 2
        sq_res += (y[i] - y_estimado) ** 2
        
    # Fórmula final do R²
    r2 = 1 - (sq_res / sq_total)
    
    # PASSO D: Preparar os dados para desenhar a linha no gráfico
    # Criar um array para o eixo X indo do mês 1 até o mês 15
    x_tendencia = np.arange(1, 16)
    y_tendencia = a * x_tendencia + b
    
    # Plotar os pontos reais (bolinhas)
    plt.scatter(x, y, color='gray', alpha=0.5, s=20)
    
    # Plotar a linha de tendência colocando a Equação e o R² na legenda
    texto_legenda = f'{prod}: y = {a:.2f}x + {b:.2f} (R² = {r2:.4f})'
    plt.plot(x_tendencia, y_tendencia, color=cores[idx], linewidth=2.5, label=texto_legenda)

# 4. Adicionar a linha vertical divisória (Mês 12)
plt.axvline(x=12, color='gray', linestyle=':', linewidth=2)

# Pegar os limites do eixo Y para posicionar textos
ymin, ymax = plt.ylim()

# 5. Adicionar textos indicando os períodos
plt.text(8, ymin + 10, 'Dados Históricos\n(Meses 1-12)', ha='center', va='bottom', fontsize=12)
plt.text(14, ymin + 10, 'Previsão\n(Meses 13-15)', ha='center', va='bottom', fontsize=12)

# 6. Estilização do gráfico
plt.title("Previsão de Vendas por Produto e Mês com R²", fontsize=16)
plt.xlabel("Tempo (Meses)", fontsize=14)
plt.ylabel("Vendas Previstas (Unidades)", fontsize=14)

# Configurar eixos
plt.xticks(np.arange(1, 16, 1), fontsize=12)
plt.yticks(fontsize=12)

# Adicionar a legenda (ajustada para caber a equação e o R²)
plt.legend(title="Linha de Tendência", loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Grades e bordas
plt.grid(True, linestyle='-', alpha=0.4)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Ajustar layout para a legenda não cortar e mostrar o gráfico
plt.tight_layout()
plt.show()
