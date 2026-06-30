# Treinamento do Modelo

Este arquivo resume as etapas usadas no treinamento do modelo Gaussian Naive Bayes.

## 1. Importacao das bibliotecas

As bibliotecas `pandas` e `numpy` sao usadas para trabalhar com dados tabulares e estruturas numericas. O `scikit-learn` fornece a divisao dos dados, o modelo `GaussianNB` e as metricas de avaliacao. O `joblib` salva o modelo treinado em arquivo.

Essa etapa e necessaria porque o treinamento depende dessas ferramentas.

## 2. Carregamento da base de dados

A base Breast Cancer Wisconsin Diagnostic e carregada a partir do arquivo original `wdbc.data`, dentro da pasta `data/`.

Essa etapa transforma o arquivo bruto em um `DataFrame`, que e uma tabela mais facil de manipular com Python.

## 3. Selecao das features

O treinamento usa somente as oito variaveis escolhidas na analise exploratoria:

- `worst_concave_points`
- `worst_perimeter`
- `mean_compactness`
- `se_radius`
- `worst_texture`
- `worst_smoothness`
- `worst_symmetry`
- `se_concave_points`

Essa etapa e necessaria para manter o treinamento de acordo com a EDA e evitar usar variaveis que nao foram selecionadas.

## 4. Codificacao da variavel alvo

A coluna `diagnosis` possui os valores `B` e `M`. Para o modelo, eles sao convertidos para numeros:

- `B` vira `0`
- `M` vira `1`

Essa conversao e necessaria porque os algoritmos do `scikit-learn` trabalham melhor com rotulos numericos.

## 5. Divisao em treino e teste

Os dados sao divididos com `train_test_split`, usando `test_size=0.2`, `random_state=42` e `stratify=y`.

O conjunto de treino e usado para ensinar o modelo. O conjunto de teste e usado para avaliar o desempenho em dados que o modelo ainda nao viu. O `stratify=y` mantem a proporcao de tumores benignos e malignos nos dois conjuntos.

## 6. Criacao e treinamento do modelo

O modelo usado e exclusivamente o `GaussianNB`, conforme pedido no trabalho.

Ele aprende, a partir dos dados de treino, o comportamento das variaveis selecionadas para cada classe: benigno ou maligno.

## 7. Previsoes no conjunto de teste

Depois do treinamento, o modelo faz previsoes para os registros do conjunto de teste.

Essa etapa e necessaria para comparar as respostas previstas pelo modelo com as respostas reais.

## 8. Avaliacao do modelo

As metricas calculadas sao:

- Accuracy
- Precision
- Recall
- F1-score
- Matriz de Confusao

Essas metricas mostram a qualidade geral do modelo e ajudam a entender os erros de classificacao.

## 9. Salvamento do modelo

O modelo treinado e salvo em `models/naive_bayes_model.joblib` usando `joblib.dump()`.

Essa etapa e necessaria porque a aplicacao web podera carregar esse arquivo depois, sem precisar treinar o modelo novamente.
