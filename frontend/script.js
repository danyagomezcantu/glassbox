async function sendMessage() {
  const message = document.getElementById("inputText").value;
  const response = await fetch("http://localhost:5000/inference", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });
  const data = await response.json();
  document.getElementById("result").textContent = `Result: ${data.result}`;
}

