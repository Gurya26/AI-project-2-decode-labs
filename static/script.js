async function predictFlower() {

    const sepalLength = document.getElementById("sepal_length").value;
    const sepalWidth = document.getElementById("sepal_width").value;
    const petalLength = document.getElementById("petal_length").value;
    const petalWidth = document.getElementById("petal_width").value;

    const result = document.getElementById("result");

    // Validate Inputs
    if (
        sepalLength === "" ||
        sepalWidth === "" ||
        petalLength === "" ||
        petalWidth === ""
    ) {

        result.innerHTML = `
            <div class="error-card">
                ⚠️ Please enter all four flower measurements.
            </div>
        `;

        return;
    }

    // Loading Animation

    result.innerHTML = `

        <div class="loading-card">

            <div class="loader"></div>

            <h3>Analyzing Flower...</h3>

            <p>Please wait...</p>

        </div>

    `;

    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                sepal_length: sepalLength,
                sepal_width: sepalWidth,
                petal_length: petalLength,
                petal_width: petalWidth

            })

        });

        const data = await response.json();

        if (data.error) {

            result.innerHTML = `
                <div class="error-card">
                    ❌ ${data.error}
                </div>
            `;

            return;

        }

        result.innerHTML = `

        <div class="prediction-card">

            <div class="flower-emoji">

                ${data.image}

            </div>

            <div class="prediction-title">

                Prediction Result

            </div>

            <div class="prediction-name">

                ${data.prediction}

            </div>

            <div class="scientific-name">

                ${data.scientific}

            </div>

            <div class="confidence-title">

                🎯 Confidence

            </div>

            <div class="progress">

                <div
                    class="progress-bar"
                    style="width:${data.confidence}%"
                ></div>

            </div>

            <div class="confidence-value">

                ${data.confidence}%

            </div>

            <div class="description">

                ${data.description}

            </div>

        </div>

        `;

    }

    catch (error) {

        console.error(error);

        result.innerHTML = `

            <div class="error-card">

                ❌ Something went wrong.

            </div>

        `;

    }

}

function resetFields() {

    document.getElementById("sepal_length").value = "";
    document.getElementById("sepal_width").value = "";
    document.getElementById("petal_length").value = "";
    document.getElementById("petal_width").value = "";

    document.getElementById("result").innerHTML = `
        Prediction will appear here.
    `;

}