## Trabalho Final da Disciplina de Probabilidade e Estatística
### Curso de Engenharia da Computação
### Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE)
#### Professor: Valberto Feitosa
#### Alunos: Marcelo Antônio Dantas Filho, Marcos Martenier Santos Oliveira, Guilherme Leitão

## 1. Objetivo

Ao final da atividade, os alunos deverão ser capazes de desenvolver uma solução completa de Machine Learning, abrangendo desde a análise da base de dados até a disponibilização de um modelo treinado em uma aplicação web.
Para isso, deverão:
1. Utilizar a base de dados Breast Cancer Wisconsin Diagnostic Dataset, disponibilizada pelo
professor.
2. Analisar e compreender as características da base de dados.
3. Selecionar e justificar as variáveis (features) utilizadas no treinamento.
4. Treinar um modelo de Machine Learning utilizando o algoritmo Naive Bayes.
5. Salvar o modelo treinado para utilização posterior.
6. Desenvolver uma aplicação web simples (front-end e back-end) que permita ao usuário inserir
dados e obter previsões utilizando o modelo treinado.

## 2. Desenvolvimento da Atividade

### 2.1 Análise da Base de Dados
Todos os grupos deverão utilizar a base de dados Breast Cancer Wisconsin Diagnostic Dataset.
A base possui:
• 569 observações;
• 30 variáveis preditoras;
• 1 variável-alvo (diagnóstico);
• duas classes:
o Benigno;
o Maligno.

Cada equipe deverá:
1. Realizar uma análise exploratória dos dados;
2. Apresentar estatísticas descritivas das variáveis;
3. Investigar a distribuição das classes;
4. Justificar a escolha das variáveis utilizadas no modelo;
5. Explicar eventuais etapas de pré-processamento adotadas.

### 2.2 Treinamento do Modelo com Naive Bayes
Os alunos deverão utilizar Python e bibliotecas apropriadas, como o Scikit-Learn, para realizar as seguintes etapas:
1. Carregar a base de dados;
2. Selecionar as variáveis preditoras;
3. Dividir os dados em conjuntos de treinamento e teste;
4. Treinar um modelo Naive Bayes utilizando o conjunto de treinamento;
5. Avaliar o desempenho do modelo.
A avaliação deverá apresentar, no mínimo:
• Acurácia;
• Precisão (Precision);
• Revocação (Recall);
• F1-Score;
• Matriz de Confusão.
Salvamento do Modelo Treinado
Após o treinamento, o modelo deverá ser salvo utilizando:
• joblib; ou
• pickle.
O arquivo salvo deverá ser utilizado posteriormente pela aplicação web.

### 2.3 Desenvolvimento da Aplicação Web
Os alunos deverão desenvolver uma aplicação web simples que permita a interação do usuário com o
modelo treinado.

#### 2.3.1 Front-End
O front-end deverá:
• possuir uma página HTML;
• conter um formulário para entrada dos dados;
• apresentar campos correspondentes às variáveis utilizadas no treinamento;
• possuir um botão "Prever".
A criatividade na construção da interface será considerada na avaliação.

#### 2.3.2 Back-End
O back-end deverá ser desenvolvido utilizando Flask, Django ou framework equivalente.
O sistema deverá:
• carregar o modelo salvo;
• receber os dados enviados pelo formulário;
• aplicar o modelo Naive Bayes;
• retornar o resultado ao usuário.

#### 2.3.3 Exibição do Resultado
A aplicação deverá exibir claramente a classe prevista:
• Tumor Benigno; ou
• Tumor Maligno.
Opcionalmente, a equipe poderá apresentar também a probabilidade associada à previsão.

## 3. Ferramentas e Tecnologias
• Python
• Scikit-Learn
• Pandas
• NumPy
• Joblib ou Pickle
• Flask ou Django
• HTML
• CSS
• JavaScript

## 4. Fluxo da Aplicação
1. O usuário acessa a aplicação.
2. Preenche os campos do formulário.
3. Clica no botão "Prever".
4. O back-end processa os dados.
5. O modelo realiza a previsão.
6. O resultado é exibido ao usuário.

## 5. Critérios de Avaliação
A nota do trabalho terá valor máximo de 5,0 pontos e será composta por duas partes:

### 5.1 Nota da Equipe (4,0 pontos)
Esta nota será atribuída igualmente a todos os integrantes da equipe, considerando a qualidade técnica
do projeto desenvolvido.

#### Critérios de Pontuação:
- Análise exploratória da base de dados - 0,5
- Seleção e justificativa das features - 0,5
- Treinamento e avaliação do modelo - 1,0
- Desenvolvimento do Back-End - 0,75
- Desenvolvimento do Front-End - 0,75
- Documentação do projeto - 0,5

Total - 4,0

### 5.2 Nota Individual (1,0 ponto)
A nota individual será atribuída pelo professor durante a apresentação do trabalho, considerando:

#### Critérios de Pontuação:
- Domínio do conteúdo apresentado 0,4
- Participação efetiva no desenvolvimento do projeto 0,3
- Clareza e segurança na apresentação 0,3

Total 1,0

### Nota Final
Nota Final = Nota da Equipe + Nota Individual

Valor máximo: 5,0 pontos

### Observações
- Todos os integrantes deverão participar da apresentação.
- O professor poderá realizar perguntas individuais sobre qualquer parte do projeto.
- Alunos que demonstrarem desconhecimento do trabalho poderão ter redução na nota individual.
- A ausência na apresentação implicará atribuição de nota zero na parte individual, salvo justificativa aceita pelo professor.
- Todas as equipes deverão utilizar a base de dados Breast Cancer Wisconsin Diagnostic Dataset disponibilizada pelo professor.

## 6. Considerações Finais
Este trabalho permitirá aos alunos:

- aplicar o algoritmo Naive Bayes em um problema real de classificação;
- compreender o ciclo completo de um projeto de Machine Learning;
- desenvolver habilidades práticas em desenvolvimento web;
- integrar modelos de Machine Learning a aplicações interativas.

### Observação: 
Todas as equipes utilizarão a mesma base de dados, permitindo a comparação dos resultados obtidos e das estratégias adotadas para seleção de atributos, treinamento do modelo e desenvolvimento da aplicação.

#### Base de Dados Utilizada:
Breast Cancer Wisconsin Diagnostic Dataset (WDBC)

[Documentação oficial da base de dados](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)

A base contém 569 observações, 30 variáveis preditoras e uma variável-alvo referente ao diagnóstico do tumor (Benigno ou Maligno). Não possui valores faltantes e é amplamente utilizada em estudos e aplicações de Machine Learning.