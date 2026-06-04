import streamlit as st
import sys
import os
import math

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.youssef import YoussefAgent
from utils.voice import speak

st.set_page_config(
    page_title="Youssef — Agent Stocks",
    page_icon="📦",
    layout="centered"
)

st.markdown("""
<style>
    .agent-header {
        background: linear-gradient(135deg, #7F77DD, #534AB7);
        padding: 20px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    }
    .agent-name { font-size: 28px; font-weight: 700; margin: 0; }
    .agent-role { font-size: 14px; opacity: 0.85; margin: 4px 0 0; }
    .metric-card {
        background: #F8F9FF;
        border: 1px solid #E0DEFF;
        border-radius: 10px;
        padding: 12px 16px;
        text-align: center;
        margin-bottom: 8px;
    }
    .metric-val { font-size: 24px; font-weight: 700; color: #534AB7; }
    .metric-lbl { font-size: 12px; color: #666; margin-top: 4px; }
</style>
""", unsafe_allow_html=True)

# ── MICRO ──
st.components.v1.html("""
<script>
let recognition = null;
let isRecording = false;

function toggleMic() {
    if (isRecording) { stopMic(); } else { startMic(); }
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
        document.getElementById('micBtn').textContent = 'Ecoute... cliquez pour arreter';
        document.getElementById('micBtn').style.background = '#E24B4A';
        document.getElementById('micStatus').textContent = 'Parlez maintenant...';
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById('micStatus').textContent = 'Reconnu: ' + transcript;
        const chatInput = window.parent.document.querySelector('textarea');
        if (chatInput) {
            const setter = Object.getOwnPropertyDescriptor(
                window.HTMLTextAreaElement.prototype, 'value').set;
            setter.call(chatInput, transcript);
            chatInput.dispatchEvent(new Event('input', { bubbles: true }));
            setTimeout(() => {
                chatInput.dispatchEvent(new KeyboardEvent('keydown', {
                    key: 'Enter', keyCode: 13, bubbles: true
                }));
            }, 800);
        }
    };

    recognition.onerror = function(event) {
        document.getElementById('micStatus').textContent = 'Erreur: ' + event.error;
        resetMic();
    };

    recognition.onend = function() { resetMic(); };
    recognition.start();
}

function stopMic() {
    if (recognition) recognition.stop();
    resetMic();
}

function resetMic() {
    isRecording = false;
    document.getElementById('micBtn').textContent = 'Parler a Youssef';
    document.getElementById('micBtn').style.background = '#534AB7';
}
</script>

<div style="padding:10px 0">
    <div id="micStatus" style="font-size:12px;color:#534AB7;
    min-height:20px;margin-bottom:8px">
        Cliquez pour parler a Youssef
    </div>
    <button id="micBtn" onclick="toggleMic()"
        style="background:#534AB7;color:white;border:none;
        padding:10px 20px;border-radius:8px;cursor:pointer;
        width:100%;font-size:14px">
        Parler a Youssef
    </button>
</div>
""", height=100)

# ── EN-TETE ──
st.markdown("""
<div class="agent-header">
    <p class="agent-name">📦 Youssef</p>
    <p class="agent-role">Agent IA — Optimisation des stocks & EOQ dynamique</p>
</div>
""", unsafe_allow_html=True)

# ── INITIALISER ──
if "youssef" not in st.session_state:
    st.session_state.youssef = YoussefAgent()
if "youssef_messages" not in st.session_state:
    st.session_state.youssef_messages = []
    welcome = "Bonjour ! Je suis Youssef, votre agent IA specialise en optimisation des stocks. Je calcule votre EOQ, stock de securite et point de reapprovisionnement. Donnez-moi vos donnees et j'optimise vos stocks immediatement !"
    st.session_state.youssef_messages.append({
        "role": "assistant",
        "content": welcome
    })
if "youssef_auto_speak" not in st.session_state:
    st.session_state.youssef_auto_speak = False

# ── MESSAGES ──
for i, message in enumerate(st.session_state.youssef_messages):
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant", avatar="📦"):
            st.write(message["content"])
            if st.button("🔊 Ecouter", key=f"speak_y_{i}"):
                speak(message["content"], gender="male")

# ── SAISIE TEXTE ──
if prompt := st.chat_input("Posez votre question a Youssef..."):
    st.session_state.youssef_messages.append({
        "role": "user",
        "content": prompt
    })
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant", avatar="📦"):
        with st.spinner("Youssef calcule..."):
            response = st.session_state.youssef.chat(prompt)
        st.write(response)
        if st.session_state.youssef_auto_speak:
            speak(response, gender="male")
    st.session_state.youssef_messages.append({
        "role": "assistant",
        "content": response
    })
    st.rerun()

# ── SIDEBAR ──
with st.sidebar:
    st.markdown("### ChainIQ")
    st.markdown("**Agent actif :** Youssef")
    st.markdown("**Specialite :** Stocks & EOQ")
    st.divider()

    st.markdown("### Calculateur EOQ Rapide")
    demande = st.number_input(
        "Demande annuelle (unites)", min_value=1, value=1200
    )
    cout_cmd = st.number_input(
        "Cout de commande (MAD)", min_value=1, value=500
    )
    cout_stock = st.number_input(
        "Cout stockage/unite/an (MAD)", min_value=1, value=50
    )

    if st.button("Calculer EOQ", use_container_width=True, type="primary"):
        eoq = math.sqrt((2 * demande * cout_cmd) / cout_stock)
        nb_cmd = demande / eoq
        cout_total = (demande / eoq) * cout_cmd + (eoq / 2) * cout_stock

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-val">{round(eoq)} unites</div>
            <div class="metric-lbl">EOQ optimal</div>
        </div>
        <div class="metric-card">
            <div class="metric-val">{round(nb_cmd, 1)}</div>
            <div class="metric-lbl">Commandes/an</div>
        </div>
        <div class="metric-card">
            <div class="metric-val">{round(365/nb_cmd)} jours</div>
            <div class="metric-lbl">Intervalle commande</div>
        </div>
        <div class="metric-card">
            <div class="metric-val">{round(cout_total)} MAD</div>
            <div class="metric-lbl">Cout total annuel</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### 🔊 Voix")
    st.session_state.youssef_auto_speak = st.toggle(
        "Lecture automatique",
        value=st.session_state.youssef_auto_speak
    )
    st.divider()
    if st.button("🔄 Nouvelle conversation", use_container_width=True):
        st.session_state.youssef.reset()
        st.session_state.youssef_messages = []
        st.rerun()