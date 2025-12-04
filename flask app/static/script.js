
function predictScore() {
    const data = {
        gender: document.getElementById('gender').value,
        race: document.getElementById('race').value,
        parent: document.getElementById('parent').value,
        lunch: document.getElementById('lunch').value,
        prep: document.getElementById('prep').value,
        reading: Number(document.getElementById('reading').value),
        writing: Number(document.getElementById('writing').value)
    };

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        document.getElementById("result").textContent = "Predicted Math Score: " + result.prediction;
    });
}
