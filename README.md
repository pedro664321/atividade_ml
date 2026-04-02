# Atividade Machine Learning - Previsão de Vendas

**Desenvolvido por:** Pedro Batista e Matheus Oliveira

---

## 💡 Como a lógica funciona? (Explicação Simples)

Para realizar as previsões, utilizamos um conceito chamado **Regressão Linear Simples**. Imagine que pegamos todos os pontos de vendas dos meses passados e tentamos desenhar uma linha reta que passe o mais perto possível de todos eles.

1.  **Olhamos para o passado:** O código analisa os meses (1 a 12) e a quantidade vendida.
2.  **Traçamos uma tendência:** Ele descobre se essa "linha" está subindo ou descendo e qual a velocidade disso.
3.  **Olhamos para o futuro:** Com essa linha desenhada, basta "esticá-la" para os meses 13, 14 e 15 para descobrir quanto provavelmente vamos vender.
4.  **Medimos a confiança:** Usamos o cálculo do **R²** para saber o quanto podemos confiar nessa linha. Se o R² for próximo de 1, a linha segue muito bem os dados reais.

---

## 📊 Tabela de Resultados (Dados de Vendas e Previsões)

Abaixo estão os dados processados, incluindo as vendas reais, o que o modelo previu e a confiabilidade (R²) de cada produto.

| Produto | Mês | Vendas Reais | Vendas Previstas (ŷ) | R² |
| :--- | :--- | :--- | :--- | :--- |
| Tinta Acrílica | 1 | 120 | 108.33 | 0.7985 |
| Tinta Acrílica | 12 | 400 | 318.33 | 0.7985 |
| **Tinta Acrílica** | **13 (Prev)** | **--** | **337.42** | **0.7985** |
| Tinta Esmalte | 1 | 80 | 82.69 | 0.9817 |
| Tinta Esmalte | 12 | 200 | 202.31 | 0.9817 |
| **Tinta Esmalte** | **13 (Prev)** | **--** | **213.18** | **0.9817** |
| Tinta Látex | 1 | 200 | 200.00 | 1.0000 |
| Tinta Látex | 12 | 310 | 310.00 | 1.0000 |
| **Tinta Látex** | **13 (Prev)** | **--** | **320.00** | **1.0000** |
| Tinta Spray | 1 | 50 | 54.71 | 0.9427 |
| Tinta Spray | 12 | 120 | 120.52 | 0.9427 |
| **Tinta Spray** | **13 (Prev)** | **--** | **126.50** | **0.9427** |
| Tinta PVA | 1 | 150 | 150.00 | 1.0000 |
| Tinta PVA | 12 | 260 | 260.00 | 1.0000 |
| **Tinta PVA** | **13 (Prev)** | **--** | **270.00** | **1.0000** |

*(Nota: A tabela completa com todos os meses e produtos está disponível no arquivo Excel gerado pelo sistema.)*

---

## 📈 Análise de Tendência

### 1. Evidência Matemática (Coeficiente Angular)
Na equação da reta (`y = ax + b`), o coeficiente angular (`a`) representa a taxa de variação da tendência.
* Um valor **positivo** indica crescimento.

Ao calcular as métricas, o coeficiente (`a`) resultou em valores estritamente positivos para todos os itens do portfólio. Destaca-se a "Tinta Acrílica" com a maior taxa de inclinação (`a = 19.09`), seguida por produtos de crescimento constante, como as tintas Látex e PVA (`a = 10.00`).

### 2. Evidência Gráfica (Projeção Visual)
A análise visual confirma a ascensão. Todas as projeções para os trimestres futuros (meses 13, 14 e 15) seguem trajetórias ascendentes, confirmando a ampliação da demanda e descartando cenários de estabilidade ou queda.
