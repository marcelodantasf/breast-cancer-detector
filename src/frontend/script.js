const selectedFeatures = [
    "worst_concave_points",
    "worst_perimeter",
    "mean_compactness",
    "se_radius",
    "worst_texture",
    "worst_smoothness",
    "worst_symmetry",
    "se_concave_points",
];

const form = document.getElementById("prediction-form");
const errorMessage = document.getElementById("error-message");
const apiUrls = [
    "http://localhost:5000/analysis",
    "http://127.0.0.1:5000/analysis",
    "http://localhost:8000/analysis",
    "http://127.0.0.1:8000/analysis",
];

function showResult(message, probability) {
    let resultMessage = document.getElementById("result-message");

    if (!resultMessage) {
        resultMessage = document.createElement("p");
        resultMessage.id = "result-message";
        resultMessage.className = "result-message";
        form.appendChild(resultMessage);
    }

    resultMessage.innerHTML = probability
        ? `Resultado:<br><strong>${message}</strong><br>Probabilidade: ${probability}`
        : `Resultado:<br><strong>${message}</strong>`;
}

function clearResult() {
    const resultMessage = document.getElementById("result-message");

    if (resultMessage) {
        resultMessage.remove();
    }
}

async function handleSubmit(event) {
    event.preventDefault();
    clearResult();

    // Verifica se todos os campos foram preenchidos antes de preparar os dados.
    const hasEmptyField = selectedFeatures.some((feature) => {
        return document.getElementById(feature).value.trim() === "";
    });

    if (hasEmptyField) {
        errorMessage.textContent = "Todos os campos devem ser preenchidos.";
        return;
    }

    errorMessage.textContent = "";

    // Monta o objeto no mesmo formato esperado pelo futuro back-end.
    const data = {
        worst_concave_points: Number(document.getElementById("worst_concave_points").value),
        worst_perimeter: Number(document.getElementById("worst_perimeter").value),
        mean_compactness: Number(document.getElementById("mean_compactness").value),
        se_radius: Number(document.getElementById("se_radius").value),
        worst_texture: Number(document.getElementById("worst_texture").value),
        worst_smoothness: Number(document.getElementById("worst_smoothness").value),
        worst_symmetry: Number(document.getElementById("worst_symmetry").value),
        se_concave_points: Number(document.getElementById("se_concave_points").value),
    };

    try {
        let response;

        for (const apiUrl of apiUrls) {
            try {
                response = await fetch(apiUrl, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data),
                });

                if (response.ok) {
                    break;
                }
            } catch (error) {
                response = null;
            }
        }

        if (!response || !response.ok) {
            throw new Error("Erro na resposta da API.");
        }

        const apiResponse = await response.json();
        const isMalignant =
            apiResponse.prediction_label === "malignant" || apiResponse.prediction === "M";
        const diagnosis = isMalignant ? "Tumor Maligno" : "Tumor Benigno";
        const probabilityValue = isMalignant
            ? apiResponse.probabilities?.malignant
            : apiResponse.probabilities?.benign;
        const probability =
            typeof probabilityValue === "number"
                ? `${(probabilityValue * 100).toFixed(2)}%`
                : "";

        showResult(diagnosis, probability);
    } catch (error) {
        errorMessage.textContent = "Não foi possível realizar a previsão. Tente novamente.";
    }
}

form.addEventListener("submit", handleSubmit);
