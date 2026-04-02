<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atividade Machine Learning - Previsão de Vendas</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
            line-height: 1.6;
            color: #333333;
            background-color: #f6f8fa;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }
        .container {
            max-width: 850px;
            background-color: #ffffff;
            border: 1px solid #d0d7de;
            border-radius: 6px;
            padding: 40px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }
        h1 {
            color: #24292f;
            border-bottom: 1px solid #d0d7de;
            padding-bottom: 10px;
            margin-top: 0;
        }
        h2 {
            color: #24292f;
            margin-top: 30px;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 8px;
        }
        p {
            margin-top: 0;
            margin-bottom: 16px;
        }
        .authors {
            font-size: 1.1em;
            color: #57606a;
            margin-bottom: 30px;
        }
        ul {
            margin-top: 0;
            margin-bottom: 16px;
            padding-left: 2em;
        }
        li {
            margin-bottom: 8px;
        }
        .highlight-box {
            background-color: #f0f6fc;
            border-left: 4px solid #0969da;
            padding: 16px;
            margin-top: 24px;
            border-radius: 0 6px 6px 0;
        }
        code {
            font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;
            background-color: rgba(175, 184, 193, 0.2);
            padding: 0.2em 0.4em;
            border-radius: 6px;
            font-size: 85%;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Atividade de Machine Learning: Análise e Previsão</h1>
    
    <div class="authors">
        <p><strong>Desenvolvido por:</strong> Pedro Batista e Matheus Oliveira</p>
    </div>

    <h2>1. Evidência Matemática (Coeficiente Angular)</h2>
    <p>Na equação da reta (<code>y = ax + b</code>), o coeficiente angular (<code>a</code>) representa a taxa de variação da tendência.</p>
    <ul>
        <li>Um valor <strong>igual a zero</strong> indicaria estabilidade (vendas estagnadas).</li>
        <li>Um valor <strong>negativo</strong> indicaria queda (redução nas vendas).</li>
        <li>Um valor <strong>positivo</strong> indica crescimento.</li>
    </ul>
    <p>Ao calcular as métricas para a rede de lojas, o coeficiente (<code>a</code>) resultou em valores estritamente positivos para todos os itens do portfólio. Destaca-se a "Tinta Acrílica" com a maior taxa de inclinação (<code>a = 19.09</code>), indicando a aceleração mais expressiva no volume de vendas mensais, seguida por produtos de crescimento constante, como as tintas Látex e PVA (<code>a = 10.00</code>).</p>

    <h2>2. Evidência Gráfica (Projeção Visual)</h2>
    <p>A análise visual dos gráficos de dispersão, sobrepostos pelas retas de regressão, confirma a ascensão. Nenhuma das retas de previsão apresenta um comportamento horizontal ou descendente ao longo dos meses 1 a 12. Pelo contrário, todas as projeções para os trimestres futuros (meses 13, 14 e 15) seguem trajetórias ascendentes, confirmando a ampliação da demanda.</p>

    <div class="highlight-box">
        <p><strong>Conclusão da Tendência Geral:</strong></p>
        <p style="margin-bottom: 0;">A análise dos dados históricos indica uma clara tendência de <strong>crescimento nas vendas</strong> para todos os produtos analisados. Do ponto de vista matemático, esta conclusão baseia-se no cálculo do coeficiente angular (a inclinação <code>a</code> da equação da reta). Como os valores de <code>a</code> são positivos para todos os itens calculados (variando de +5.98 a +19.09), o modelo atesta que o volume de unidades vendidas aumenta a cada mês. Ao agrupar as previsões por trimestres, o volume projetado para os períodos futuros é consistentemente superior aos períodos anteriores, descartando cenários de estabilidade ou queda na demanda.</p>
    </div>
</div>

</body>
</html>
