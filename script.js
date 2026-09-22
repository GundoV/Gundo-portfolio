// Chat Widget Logic
const chatToggleBtn = document.getElementById('chat-toggle-btn');
const chatWindow = document.getElementById('chat-window');
const chatCloseBtn = document.getElementById('chat-close-btn');
const chatMessages = document.getElementById('chat-messages');
const chatInput = document.getElementById('chat-input');

chatToggleBtn.addEventListener('click', () => {
    chatWindow.style.display = chatWindow.style.display === 'none' ? 'flex' : 'none';
});

chatCloseBtn.addEventListener('click', () => {
    chatWindow.style.display = 'none';
});

function appendMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('chat-message', sender === 'bot' ? 'bot-message' : 'user-message');
    msgDiv.textContent = text;
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function getBotResponse(query) {
    const q = query.toLowerCase();
    if (q.includes('skill') || q.includes('it') || q.includes('experience')) {
        return "Gundo has 10 years of experience in IT infrastructure, network engineering, systems administration, and Windows/Linux environments, alongside CompTIA & ITIL certifications.";
    } else if (q.includes('project') || q.includes('invoicely') || q.includes('airbnb') || q.includes('wobsa')) {
        return "Key projects include Invoicely (Full-stack invoicing platform with React/Node/PostgreSQL), the Airbnb Full-Stack Clone, WOBSA sports academy site, and the Python Snake game!";
    } else if (q.includes('contact') || q.includes('email') || q.includes('phone') || q.includes('whatsapp')) {
        return "You can reach Gundo via email at nemandivhegv@gmail.com, phone at 0732022496, or directly via the WhatsApp chat link in the footer!";
    } else {
        return "That's a great question! Feel free to explore the portfolio sections above or reach out directly through the contact details at the bottom of the page.";
    }
}

function handleUserMessage() {
    const text = chatInput.value.trim();
    if (!text) return;
    
    appendMessage(text, 'user');
    chatInput.value = '';

    setTimeout(() => {
        const response = getBotResponse(text);
        appendMessage(response, 'bot');
    }, 500);
}

function sendQuickQuery(queryText) {
    appendMessage(queryText, 'user');
    setTimeout(() => {
        const response = getBotResponse(queryText);
        appendMessage(response, 'bot');
    }, 500);
}

chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleUserMessage();
    }
});