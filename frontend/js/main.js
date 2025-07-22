async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;
    if (!message) return;
    
    appendToChat("User", message);
    input.value = "";

    const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    const data = await res.json();
    appendToChat("Bot", data.response);
}

function appendToChat(sender, message) {
    const chatbox = document.getElementById("chat-box");
    const className = sender === "User" ? "user-message" : "bot-message";
    const timestamp = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
    chatbox.innerHTML += `
        <div class="${className}">
            <span>${message}</span>
            <div style="font-size: 0.6em; color: #888; margin-top: 4px; text-align: right;">${timestamp}</div>
        </div>
    `;
    chatbox.scrollTop = chatbox.scrollHeight;
}

/// add event listener to the button
document.querySelector("button").addEventListener("click", sendMessage);