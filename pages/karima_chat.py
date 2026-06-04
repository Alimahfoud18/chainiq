import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.karima import KarimaAgent
from utils.voice import speak

st.set_page_config(
    page_title="Karima — Agent Supply Chain",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
    .agent-header {
        background: linear-gradient(135deg, #1D9E75, #0F6E56);
        padding: 20px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    }
    .agent-name { font-size: 28px; font-weight: 700; margin: 0; }
    .agent-role { font-size: 14px; opacity: 0.85; margin: 4px 0 0; }
    .mic-btn {
        background: #1D9E75;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        cursor: pointer;
        width: 100%;
        font-size: 15px;
        margin-top: 8px;
    }
    .mic-btn:hover { background: #0F6E56; }
    .mic-btn.recording { background: #E24B4A; animation: pulse 1s infinite; }
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.7} }
</style>
""", unsafe_allow_html=True)

# Injection JavaScript pour reconnaissance vocale
st.components.v1.html("""
<script>
let recognition = null;
let isRecording = false;

function toggleMic() {
    if (isRecording) {
        stopMic();
    } else {
        startMic();
    }
}

function startMic() {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        alert('Utilisez Google Chrome pour la reconnaissance vocale.');
        return;
    }
    
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.lang = 'fr-FR';
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = function() {
        isRecording = true;
        document.getElementById('micBtn').textContent = '🔴 Écoute... (cliquez pour arrêter)';
        document.getElementById('micBtn').className = 'mic-btn recording';
        document.getElementById('micStatus').textContent = '🎤 Parlez maintenant...';
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById('micStatus').textContent = '✅ Reconnu: ' + transcript;
        
        // Envoyer le texte reconnu à Streamlit via l'input caché
        const inputEl = window.parent.document.querySelector('input[data-testid="stTextInput"]');
        if (inputEl) {
            const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            setter.call(inputEl, transcript);
            inputEl.dispatchEvent(new Event('input', { bubbles: true }));
            inputEl.dispatchEvent(new Event('change', { bubbles: true }));
        }
        
        // Chercher le chat input
        const chatInput = window.parent.document.querySelector('textarea');
        if (chatInput) {
            const setter2 = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
            setter2.call(chatInput, transcript);
            chatInput.dispatchEvent(new Event('input', { bubbles: true }));
            chatInput.dispatchEvent(new Event('change', { bubbles: true }));
            
            // Simuler Enter
            setTimeout(() => {
                chatInput.dispatchEvent(new KeyboardEvent('keydown', {
                    key: 'Enter', keyCode: 13, bubbles: true
                }));
            }, 500);
        }
    };

    recognition.onerror = function(event) {
        document.getElementById('micStatus').textContent = '❌ Erreur: ' + event.error;
        resetMic();
    };

    recognition.onend = function() {
        resetMic();
    };

    recognition.start();
}

function stopMic() {
    if (recognition) recognition.stop();
    resetMic();
}

function resetMic() {
    isRecording = false;
    document.getElementById('micBtn').textContent = '🎤 Parler à Karima';
    document.getElementById('micBtn').className = 'mic-btn';
}
</script>

<div style="padding: 10px 0;">
    <p style="font-size:13px;color:#666;margin-bottom:6px">
        Parlez directement à Karima en français
    </p>
    <div id="micStatus" style="font-size:12px;color:#1D9E75;min-height:20px;margin-bottom:8px">
        🎤 Prêt — cliquez pour parler
    </div>
    <button id="micBtn" class="mic-btn" onclick="toggleMic()">
        🎤 Parler à Karima
    </button>
</div>
""", height=130)

# En-tête
st.markdown("""
<div class="agent-header">
    <p class="agent-name">🤖 Karima</p>
    <p class="agent-role">Agente IA — Prévision de la demande & Optimisation des stocks</p>
</div>
""", unsafe_allow_html=True)

# Initialiser
if "karima" not in st.session_state:
    st.session_state.karima = KarimaAgent()
if "messages" not in st.session_state:
    st.session_state.messages = []
    welcome = "Bonjour ! Je suis Karima, votre agente supply chain IA. Comment puis-je vous aider aujourd'hui ?"
    st.session_state.messages.append({"role": "assistant", "content": welcome})
if "auto_speak" not in st.session_state:
    st.session_state.auto_speak = False

# Afficher les messages
for i, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.write(message["content"])
            if st.button("🔊 Écouter", key=f"speak_{i}"):
                speak(message["content"])

# Zone de saisie texte
if prompt := st.chat_input("Posez votre question à Karima..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Karima analyse..."):
            response = st.session_state.karima.chat(prompt)
        st.write(response)
        if st.session_state.auto_speak:
            speak(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

# Sidebar
with st.sidebar:
    st.markdown("### ChainIQ")
    st.markdown("**Agent actif :** Karima")
    st.markdown("**Spécialité :** Supply Chain")
    st.divider()
    st.markdown("### 🔊 Voix")
    st.session_state.auto_speak = st.toggle(
        "Lecture automatique",
        value=st.session_state.auto_speak
    )
    st.divider()
    if st.button("🔄 Nouvelle conversation", use_container_width=True):
        st.session_state.karima.reset()
        st.session_state.messages = []
        st.rerun()