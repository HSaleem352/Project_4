function fetchRisk() {
    var age = document.getElementById("age-inp").value;
    var obesity = document.querySelector('#obesity-check').checked;
    var smoking = document.querySelector('#smoking-check').checked;

    var race = document.getElementById("race-select").value;
    var area = document.getElementById("area-select").value;

    var treatment = document.querySelector('#treatment-check').checked;
    var status = document.getElementById("status-select").value;

    var diabetes = document.querySelector('#diabetes-check').checked;
    var cardiovascular = document.querySelector('#cardiovascular-check').checked;
    var pulmonary = document.querySelector('#pulmonary-check').checked;
    var renal = document.querySelector('#renal-check').checked;

    const apiUrl = `/api/v1/risk_query/${age}/${obesity}/${smoking}/${race}/${area}/${treatment}/${status}/${diabetes}/${cardiovascular}/${pulmonary}/${renal}`;

    d3.json(apiUrl).then(function(data) {

        document.getElementById("risk").textContent = `This individual has an estimated risk of ${data[0].predicted_risk} for moderate-to-severe COVID-19`;
    });
}