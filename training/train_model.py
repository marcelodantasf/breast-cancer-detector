from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


# Caminhos principais do projeto.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "breast+cancer+wisconsin+diagnostic" / "wdbc.data"
MODEL_PATH = PROJECT_ROOT / "models" / "naive_bayes_model.joblib"


# Nomes das colunas conforme a estrutura original da base WDBC.
BASE_FEATURES = [
    "radius",
    "texture",
    "perimeter",
    "area",
    "smoothness",
    "compactness",
    "concavity",
    "concave_points",
    "symmetry",
    "fractal_dimension",
]

STAT_PREFIXES = ["mean", "se", "worst"]

COLUMN_NAMES = ["id", "diagnosis"] + [
    f"{prefix}_{feature}"
    for prefix in STAT_PREFIXES
    for feature in BASE_FEATURES
]


# Features definidas na etapa de analise exploratoria.
selected_features = [
    "worst_concave_points",
    "worst_perimeter",
    "mean_compactness",
    "se_radius",
    "worst_texture",
    "worst_smoothness",
    "worst_symmetry",
    "se_concave_points",
]


# 1. Carrega a base de dados original.
df = pd.read_csv(DATA_PATH, header=None, names=COLUMN_NAMES)


# 2. Seleciona somente as variaveis preditoras escolhidas na EDA.
X = df[selected_features]


# 3. Codifica a variavel alvo: B = 0 e M = 1.
y = df["diagnosis"].map({"B": 0, "M": 1})


# 4. Divide os dados em treinamento e teste mantendo a proporcao das classes.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)


# 5. Cria e treina o modelo Gaussian Naive Bayes.
model = GaussianNB()
model.fit(X_train, y_train)


# 6. Faz previsoes no conjunto de teste.
y_pred = model.predict(X_test)


# 7. Calcula as metricas obrigatorias de avaliacao.
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_labels = np.array(["B", "M"])


# 8. Exibe os resultados de forma organizada.
print("Resultados do modelo Gaussian Naive Bayes")
print("=" * 45)
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")
print("\nMatriz de Confusao:")
print(
    pd.DataFrame(
        conf_matrix,
        index=[f"Real {label}" for label in class_labels],
        columns=[f"Previsto {label}" for label in class_labels],
    )
)


# 9. Salva o modelo treinado para uso posterior pela aplicacao web.
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, MODEL_PATH)

print(f"\nModelo salvo em: {MODEL_PATH}")
