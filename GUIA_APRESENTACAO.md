# Guia de Apresentação

## 1. Objetivo do projeto

O objetivo do projeto é criar uma solução simples de Machine Learning para ajudar na predição de câncer de mama a partir de dados numéricos de exames.

A ideia não é substituir um médico. O projeto serve para mostrar o ciclo completo de um trabalho de Probabilidade, Estatística e Machine Learning: analisar uma base de dados, escolher variáveis importantes, treinar um modelo, salvar esse modelo e disponibilizar uma aplicação web simples para fazer previsões.

## 2. Explicação geral

Primeiro utilizamos a base Breast Cancer Wisconsin Diagnostic Dataset. Ela contém informações numéricas extraídas de exames de tumores de mama e também informa se cada caso era benigno ou maligno.

Depois fizemos a análise exploratória dos dados. Nessa etapa, olhamos a estrutura da base, verificamos se existiam valores faltantes, observamos as classes benigno e maligno, estudamos as distribuições e comparamos as variáveis.

Com base nessa análise, escolhemos oito variáveis para usar no modelo. Essas variáveis foram escolhidas porque ajudam a diferenciar os casos benignos dos malignos e reduzem um pouco a repetição de informações muito parecidas.

Depois treinamos o modelo Gaussian Naive Bayes. Ele foi escolhido porque era o algoritmo pedido no trabalho e porque combina com variáveis numéricas contínuas.

Em seguida, avaliamos o modelo usando métricas como accuracy, precision, recall, F1-score e matriz de confusão. Depois salvamos o modelo em um arquivo `.joblib`, para que a aplicação não precise treinar tudo de novo sempre que for usada.

Depois foi criada uma API. A API recebe os valores digitados pelo usuário, coloca esses valores na ordem correta, carrega o modelo salvo e pede para o modelo fazer a previsão.

Por fim, criamos o front-end. O usuário preenche um formulário com os oito valores, clica em "Prever", e o JavaScript envia esses dados para a API. A API devolve o resultado, e a página mostra se a previsão foi "Tumor Benigno" ou "Tumor Maligno".

## 3. Explicação de cada etapa

### Análise exploratória

A análise exploratória foi feita para entender a base antes de treinar qualquer modelo.

Ela é importante porque não faz sentido treinar um modelo sem antes saber como os dados estão organizados. Nessa etapa, verificamos o tamanho da base, os tipos das colunas, a distribuição das classes e o comportamento das variáveis.

### Limpeza dos dados

A limpeza serve para verificar se existem problemas nos dados, como valores faltantes, registros duplicados ou valores inválidos.

No nosso caso, a base já estava bem organizada. Mesmo assim, essa checagem foi importante para garantir que o modelo receberia dados confiáveis.

### Seleção das features

Features são as variáveis usadas pelo modelo para fazer a previsão.

No projeto, usamos estas oito:

- `worst_concave_points`
- `worst_perimeter`
- `mean_compactness`
- `se_radius`
- `worst_texture`
- `worst_smoothness`
- `worst_symmetry`
- `se_concave_points`

Essa escolha foi importante porque o modelo não precisa usar todas as colunas. Algumas variáveis carregam informações parecidas, então selecionar um conjunto menor ajuda a deixar o modelo mais simples e mais fácil de explicar.

### Treinamento

O treinamento é a etapa em que o modelo aprende a relação entre as variáveis do exame e o diagnóstico.

Para isso, os dados foram separados em treino e teste. O treino serve para ensinar o modelo. O teste serve para verificar como ele se comporta em dados que ainda não viu.

### Gaussian Naive Bayes

O Gaussian Naive Bayes é um algoritmo de classificação.

Ele tenta estimar, com base nas variáveis informadas, qual classe é mais provável: benigno ou maligno. Ele é chamado de "Gaussian" porque trabalha bem com variáveis numéricas contínuas, assumindo uma distribuição parecida com a normal para cada variável dentro de cada classe.

Ele foi usado porque era o algoritmo obrigatório do trabalho.

### Métricas utilizadas

Usamos algumas métricas para entender o desempenho do modelo.

Accuracy mostra a proporção geral de acertos.

Precision mostra, entre os casos previstos como malignos, quantos realmente eram malignos.

Recall mostra, entre os casos malignos reais, quantos o modelo conseguiu encontrar.

F1-score combina precision e recall em uma única medida.

A matriz de confusão mostra os acertos e erros separados por classe. Ela ajuda a entender melhor onde o modelo está errando.

### Salvamento do modelo

Depois de treinar, salvamos o modelo em `models/naive_bayes_model.joblib`.

Isso é importante porque a aplicação web não precisa treinar o modelo toda vez. Ela apenas carrega o arquivo salvo e usa o modelo pronto para prever.

### API

A API fica na pasta `src/app`.

Ela recebe uma requisição `POST` na rota `/analysis`. Essa requisição precisa enviar um JSON com as oito features. A API valida os dados, usa o modelo salvo e devolve uma resposta com a previsão.

A resposta traz a classe prevista, o rótulo em inglês, as probabilidades, o tipo do modelo e as features usadas.

### Front-end

O front-end fica na pasta `src/frontend`.

Ele possui uma página HTML com o formulário, um arquivo CSS para o visual e um arquivo JavaScript para coletar os valores, validar campos vazios, enviar a requisição para a API e exibir o resultado.

O front-end não faz Machine Learning. Ele apenas coleta os dados e mostra a resposta que vem da API.

## 4. Explicação do código

O `notebooks/exploratory-analysis.ipynb` contém a análise exploratória. É nele que a base foi estudada e onde as variáveis finais foram justificadas.

O `training/train_model.py` é responsável por carregar a base, selecionar as oito features, codificar o diagnóstico, separar treino e teste, treinar o Gaussian Naive Bayes, calcular as métricas e salvar o modelo.

O arquivo `models/naive_bayes_model.joblib` é o modelo treinado. Ele é carregado pela API para fazer previsões.

O `src/app/main.py` inicia a API e conecta as rotas.

O `src/app/api/routes.py` define as rotas da API. A rota principal para previsão é `POST /analysis`.

O `src/app/schemas/analysis.py` define o formato dos dados que a API espera receber e o formato da resposta que ela devolve.

O `src/app/ml/features.py` guarda a lista das oito features na ordem correta. Isso é importante porque o modelo precisa receber os dados na mesma ordem usada no treinamento.

O `src/app/ml/predictor.py` carrega o modelo salvo com `joblib`, organiza os valores em uma tabela e chama o `predict()` do modelo.

O `src/app/services/analysis_service.py` organiza o fluxo entre a requisição recebida e a resposta final enviada ao front-end.

O `src/frontend/index.html` é a página do formulário.

O `src/frontend/styles.css` define apenas o visual da página.

O `src/frontend/script.js` coleta os dados digitados, monta o JSON, envia para a API e mostra o resultado na tela.

## 5. Fluxo completo da aplicação

O usuário abre a página do front-end.

Depois ele preenche os oito campos do formulário com os valores do exame.

Quando clica em "Prever", o JavaScript verifica se todos os campos foram preenchidos.

Se algum campo estiver vazio, a página mostra uma mensagem simples e não envia nada.

Se todos os campos estiverem preenchidos, o JavaScript monta um JSON com os nomes das oito features.

Esse JSON é enviado para a API na rota `POST /analysis`.

A API recebe os dados e valida se os campos existem e se os valores são numéricos.

Depois a API passa os valores para o predictor.

O predictor carrega o modelo salvo em `models/naive_bayes_model.joblib`.

Em seguida, ele organiza os valores na mesma ordem usada no treinamento.

O modelo faz a previsão.

A API transforma essa previsão em uma resposta com a classe e as probabilidades.

O front-end recebe a resposta.

Por fim, a página mostra:

Resultado:

Tumor Benigno

ou

Resultado:

Tumor Maligno

Se a API devolver a probabilidade, o front-end também mostra essa probabilidade abaixo do diagnóstico.

## 6. Possíveis perguntas do professor

### Por que escolheram Gaussian Naive Bayes?

Porque era o algoritmo pedido no trabalho. Além disso, ele é adequado para variáveis numéricas contínuas, como as medidas presentes nessa base.

### O que é uma feature?

Feature é uma variável usada pelo modelo para fazer a previsão. Neste projeto, são medidas do exame, como perímetro, textura, suavidade e pontos côncavos.

### Por que não usamos todas as variáveis?

Porque algumas variáveis são muito parecidas entre si. Usar um conjunto menor deixa o modelo mais simples, reduz redundância e facilita a explicação.

### O que significa Accuracy?

Accuracy é a taxa geral de acertos do modelo. Ela mostra quantas previsões o modelo acertou em relação ao total.

### O que é Precision?

Precision responde: quando o modelo diz que um tumor é maligno, com que frequência ele está certo?

### O que é Recall?

Recall responde: de todos os tumores malignos reais, quantos o modelo conseguiu identificar?

### O que é F1-score?

F1-score combina precision e recall. Ele é útil quando queremos uma medida única que considere os dois lados.

### Por que dividir treino e teste?

Para avaliar o modelo de forma mais justa. O modelo aprende com o treino e depois é testado com dados separados, que ele ainda não viu.

### Por que salvar o modelo?

Para não precisar treinar novamente toda vez que a aplicação for usada. A API apenas carrega o modelo salvo e faz a previsão.

### Qual o papel da API?

A API recebe os dados do front-end, organiza os valores, chama o modelo treinado e devolve o resultado.

### Qual o papel do front-end?

O front-end é a parte visual. Ele permite que o usuário preencha os valores do exame, envia esses dados para a API e mostra o resultado na tela.

### A aplicação substitui um diagnóstico médico?

Não. Ela é um projeto acadêmico para demonstrar análise de dados, treinamento de modelo e integração com uma aplicação web.

## 7. Resumo para apresentação

Neste projeto, nós trabalhamos com a base Breast Cancer Wisconsin Diagnostic, que possui medidas numéricas extraídas de exames de tumores de mama. Cada registro da base informa se o tumor era benigno ou maligno.

Primeiro, fizemos uma análise exploratória para entender os dados. Antes de treinar qualquer modelo, era importante saber se a base estava organizada, se existiam valores faltantes, quais eram as classes e quais variáveis pareciam mais úteis para separar tumores benignos de malignos.

Depois dessa análise, selecionamos oito variáveis para usar no treinamento. A ideia foi escolher variáveis que tivessem relação com o diagnóstico, mas sem usar todas as colunas da base. Isso deixa o modelo mais simples e mais fácil de explicar.

Na etapa de treinamento, usamos o Gaussian Naive Bayes, que foi o algoritmo solicitado no trabalho. Antes de treinar, codificamos o diagnóstico: benigno virou 0 e maligno virou 1. Também dividimos os dados em treino e teste, porque o modelo precisa ser avaliado em dados que ele não usou para aprender.

Depois do treinamento, avaliamos o modelo com accuracy, precision, recall, F1-score e matriz de confusão. Essas métricas ajudam a entender não só quantas previsões o modelo acertou, mas também como ele se comportou em relação aos casos malignos e benignos.

Em seguida, salvamos o modelo usando joblib. Isso é importante porque a aplicação web não deve treinar o modelo toda vez. Ela só precisa carregar o arquivo do modelo já treinado e usar esse modelo para fazer previsões.

Depois foi criada a API. A API recebe os oito valores do exame em formato JSON, coloca esses valores na ordem correta, carrega o modelo salvo e chama o método de previsão. Depois ela devolve uma resposta dizendo se a previsão foi benigno ou maligno, junto com as probabilidades.

Por último, criamos o front-end. Ele é uma página simples com um formulário. O usuário preenche os oito campos, clica em "Prever", e o JavaScript envia esses dados para a API. Quando a API responde, o front-end mostra o resultado na própria página.

Então, o fluxo completo fica assim: o usuário preenche o formulário, o front-end envia os dados, a API recebe, o modelo faz a previsão e o resultado aparece para o usuário. O projeto mostra o caminho completo desde a análise da base até uma aplicação web simples usando Machine Learning.
