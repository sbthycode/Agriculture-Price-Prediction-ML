// main.js
document.getElementById("predictionForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const commodity = document.getElementById("commodity").value;
    const APMC = document.getElementById("APMC").value;
    const date = document.getElementById("date").value;
    const arrival = document.getElementById("arrival").value;

    // Build the URL with user input
    const apiUrl = `http://127.0.0.1:8000/make_prediction/?commodity=${commodity}&APMC=${APMC}&date=${date}&arrival=${arrival}`;

    // Make a request to your FastAPI endpoint
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const predictedPrice = data.predicted_price;
            document.getElementById("predictionResult").innerText = `Predicted Price: ${predictedPrice}`;
        })
        .catch(error => console.error('Error:', error));
});