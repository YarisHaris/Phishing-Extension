document.querySelectorAll("a").forEach(link => {
    const url = link.href;
  
    fetch("http://localhost:5000/check_url", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url: url })
    })
      .then(res => res.json())
      .then(data => {
        if (data.phishing) {
          link.style.border = "3px solid red";
          link.style.backgroundColor = "#ffe6e6";
          link.title = "⚠️ This may be a phishing link!";
          link.addEventListener("click", e => {
            e.preventDefault();
            alert("⚠️ Blocked: Phishing link detected!");
          });
        }
      })
      .catch(err => console.error("API error:", err));
  });
  