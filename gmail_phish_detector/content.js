let emailScanned = false;

function scanEmail() {

    const emailBody = document.querySelector(".a3s");
    if (!emailBody) return;

    const text = emailBody.innerText.trim();
    if (!text) return;

    if (emailScanned) return;

    fetch("http://127.0.0.1:5000/api/check_email", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email_text: text })
    })
    .then(res => res.json())
    .then(data => {

        let popup = document.getElementById("phish-popup");

        if (!popup) {
            popup = document.createElement("div");
            popup.id = "phish-popup";

            popup.style.position = "fixed";
            popup.style.bottom = "25px";
            popup.style.right = "25px";
            popup.style.background = "#0a0a0a";
            popup.style.color = "white";
            popup.style.padding = "15px";
            popup.style.borderRadius = "12px";
            popup.style.zIndex = "999999";
            popup.style.boxShadow = "0 0 25px cyan";

            document.body.appendChild(popup);
        }

        popup.innerHTML =
            `<b>${data.prediction}</b><br>
             Confidence : ${data.spam_probability}%`;

        emailScanned = true;
    });
}

// Observe Gmail DOM changes
const observer = new MutationObserver(() => {

    const emailBody = document.querySelector(".a3s");

    if (emailBody) {
        scanEmail();
    } else {
        emailScanned = false;
    }

});

observer.observe(document.body, {
    childList: true,
    subtree: true
});