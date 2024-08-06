# Previsão de Séries Temporais

## Problema

Usando dados históricos das vendas ao longo de 2023 seria possível prever o total de vendas em Janeiro/2024?

## Sobre o dataset

O dataset é composto pelas as seguintes informações:

<img src="images/df_head.png" alt="Logo" width="300" height="" align-center = "true">

## Suavização Exponencial

A suavização exponencial é uma técnica de análise e previsão de séries temporais que aplica médias ponderadas aos dados históricos, onde os pesos diminuem exponencialmente à medida que os dados ficam mais antigos. A suavização exponencial é útil para lidar com tendências e sazonalidades nos dados, e para reduzir o ruído.

Quaisquer dúvidas, segue a [documentação](https://www.statsmodels.org/dev/generated/statsmodels.tsa.holtwinters.SimpleExpSmoothing.html).

## Conclusão

<img src="images/resultado.png" alt="Logo" width="600" height="">
