import streamlit as st

st.set_page_config(
    page_title="ChainIQ — Agents IA Supply Chain",
    page_icon="⛓️",
    layout="wide"
)

st.markdown("""
<style>
    .main, .block-container { padding: 0 !important; max-width: 100% !important; }
    .hero {
        background: linear-gradient(135deg, #0F6E56 0%, #1D9E75 50%, #2DD4A0 100%);
        padding: 80px 60px;
        text-align: center;
        color: white;
    }
    .hero h1 { font-size: 52px; font-weight: 800; margin: 0 0 16px; line-height: 1.2; }
    .hero p { font-size: 20px; opacity: 0.9; max-width: 600px; margin: 0 auto 32px; line-height: 1.6; }
    .stats { background: #0F6E56; padding: 24px 60px; display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; }
    .stat { text-align: center; color: white; }
    .stat-val { font-size: 28px; font-weight: 700; display: block; }
    .stat-lbl { font-size: 13px; opacity: 0.8; }
    .section { padding: 60px; background: white; }
    .section-alt { background: #F8FAF9; }
    .section-title { font-size: 32px; font-weight: 700; text-align: center; margin-bottom: 8px; color: #1a1a1a; }
    .section-sub { text-align: center; color: #666; font-size: 16px; margin-bottom: 40px; }
    .agents-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 1000px; margin: 0 auto; }
    .agent-card {
        background: white; border: 1px solid #E5E7EB; border-radius: 16px;
        padding: 24px; text-align: center; transition: all 0.2s; cursor: pointer;
    }
    .agent-card:hover { transform: translateY(-4px); box-shadow: 0 12px 32px rgba(0,0,0,0.1); }
    .agent-avatar {
        width: 70px; height: 70px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 22px; font-weight: 800; color: white; margin: 0 auto 12px;
    }
    .agent-name { font-size: 18px; font-weight: 700; margin-bottom: 4px; color: #1a1a1a; }
    .agent-role { font-size: 12px; color: #1D9E75; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; }
    .agent-desc { font-size: 13px; color: #666; line-height: 1.5; }
    .agent-badge { display: inline-block; font-size: 11px; padding: 3px 10px; border-radius: 20px; margin-top: 12px; font-weight: 500; }
    .pricing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 900px; margin: 0 auto; }
    .pricing-card { background: white; border: 1px solid #E5E7EB; border-radius: 16px; padding: 32px 24px; text-align: center; position: relative; }
    .pricing-card.featured { border: 2px solid #1D9E75; }
    .pricing-badge { position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: #1D9E75; color: white; padding: 4px 16px; border-radius: 20px; font-size: 12px; font-weight: 600; white-space: nowrap; }
    .pricing-name { font-size: 18px; font-weight: 700; margin-bottom: 8px; color: #1a1a1a; }
    .pricing-price { font-size: 36px; font-weight: 800; color: #1D9E75; }
    .pricing-period { font-size: 13px; color: #666; margin-bottom: 20px; }
    .pricing-feature { font-size: 13px; color: #444; padding: 6px 0; border-bottom: 1px solid #F3F4F6; text-align: left; }
    .footer { background: #0F2420; color: white; padding: 40px 60px; text-align: center; }
    .footer-logo { font-size: 24px; font-weight: 800; margin-bottom: 8px; }
    .footer-links { display: flex; gap: 24px; justify-content: center; flex-wrap: wrap; margin-top: 16px; }
    .footer-link { color: rgba(255,255,255,0.6); font-size: 13px; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <div style="display:inline-block;background:rgba(255,255,255,0.2);padding:6px 16px;border-radius:20px;font-size:13px;margin-bottom:20px;border:1px solid rgba(255,255,255,0.3)">
        🇲🇦 Maroc & 🇨🇦 Canada — Plateforme IA Supply Chain
    </div>
    <h1>Votre équipe supply chain<br>augmentée par l'IA</h1>
    <p>Des agents IA spécialisés qui optimisent votre chaîne logistique — sans recrutement, sans formation, disponibles 24h/24.</p>
</div>
""", unsafe_allow_html=True)

# Boutons hero
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.markdown("<div style='background:#0F6E56;padding:20px 60px;display:flex;gap:16px;justify-content:center'>", unsafe_allow_html=True)
    st.button("🚀 Découvrir les agents", type="primary", use_container_width=True)
    st.button("📅 Réserver une démo", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# STATS
st.markdown("""
<div class="stats">
    <div class="stat"><span class="stat-val">6</span><div class="stat-lbl">Agents spécialisés</div></div>
    <div class="stat"><span class="stat-val">24/7</span><div class="stat-lbl">Disponibilité</div></div>
    <div class="stat"><span class="stat-val">-30%</span><div class="stat-lbl">Coûts logistiques</div></div>
    <div class="stat"><span class="stat-val">MAD & CAD</span><div class="stat-lbl">Facturation locale</div></div>
</div>
""", unsafe_allow_html=True)

# AGENTS
st.markdown("""
<div class="section section-alt">
    <p class="section-title">Votre équipe IA supply chain</p>
    <p class="section-sub">Chaque agent est un expert métier — pas un chatbot générique</p>
    <div class="agents-grid">
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#1D9E75,#0F6E56)">KA</div>
            <div class="agent-name">Karima</div>
            <div class="agent-role">Prévision de la demande</div>
            <div class="agent-desc">Anticipe vos ventes avec Prophet, ARIMA et XGBoost. Detecte la saisonnalite, le Ramadan, les tendances.</div>
            <span class="agent-badge" style="background:#E1F5EE;color:#0F6E56">Disponible maintenant</span>
        </div>
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#7F77DD,#534AB7)">YO</div>
            <div class="agent-name">Youssef</div>
            <div class="agent-role">Optimisation des stocks</div>
            <div class="agent-desc">Calcule votre EOQ dynamique, stock de securite et point de reapprovisionnement optimal.</div>
            <span class="agent-badge" style="background:#EEEDFE;color:#534AB7">En construction</span>
        </div>
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#EF9F27,#BA7517)">NA</div>
            <div class="agent-name">Nadia</div>
            <div class="agent-role">Gestion fournisseurs</div>
            <div class="agent-desc">Score vos fournisseurs, suit les delais de livraison et vous alerte sur les retards critiques.</div>
            <span class="agent-badge" style="background:#FAEEDA;color:#854F0B">Bientot</span>
        </div>
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#E24B4A,#993C1D)">OM</div>
            <div class="agent-name">Omar</div>
            <div class="agent-role">Transport et livraisons</div>
            <div class="agent-desc">Optimise vos routes, suit vos expeditions et gere vos couts logistiques Tanger Med.</div>
            <span class="agent-badge" style="background:#FAECE7;color:#993C1D">Bientot</span>
        </div>
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#378ADD,#185FA5)">SI</div>
            <div class="agent-name">Siham</div>
            <div class="agent-role">Reporting et KPIs</div>
            <div class="agent-desc">Genere vos tableaux de bord supply chain automatiquement et envoie des rapports PDF a la direction.</div>
            <span class="agent-badge" style="background:#E6F1FB;color:#185FA5">Bientot</span>
        </div>
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#888,#444)">AM</div>
            <div class="agent-name">Amine</div>
            <div class="agent-role">Chef orchestre</div>
            <div class="agent-desc">Coordonne tous les agents, repond a vos questions generales et pilote votre supply chain globale.</div>
            <span class="agent-badge" style="background:#F1EFE8;color:#5F5E5A">Bientot</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# PRICING
st.markdown("""
<div class="section">
    <p class="section-title">Tarifs simples et transparents</p>
    <p class="section-sub">Facturation en MAD pour le Maroc, CAD pour le Canada</p>
    <div class="pricing-grid">
        <div class="pricing-card">
            <div class="pricing-name">Starter</div>
            <div class="pricing-price">1 500</div>
            <div class="pricing-period">MAD / mois</div>
            <div class="pricing-feature">Agent Karima</div>
            <div class="pricing-feature">Agent Youssef</div>
            <div class="pricing-feature">Dashboard web</div>
            <div class="pricing-feature">Support email</div>
        </div>
        <div class="pricing-card featured">
            <div class="pricing-badge">Recommande</div>
            <div class="pricing-name">Pro</div>
            <div class="pricing-price">5 000</div>
            <div class="pricing-period">MAD / mois</div>
            <div class="pricing-feature">6 agents complets</div>
            <div class="pricing-feature">WhatsApp Business</div>
            <div class="pricing-feature">Integration Odoo</div>
            <div class="pricing-feature">Onboarding 1 sur 1</div>
        </div>
        <div class="pricing-card">
            <div class="pricing-name">Enterprise</div>
            <div class="pricing-price">Sur mesure</div>
            <div class="pricing-period">Contrat annuel</div>
            <div class="pricing-feature">Agents personnalises</div>
            <div class="pricing-feature">Deploiement on-premise</div>
            <div class="pricing-feature">Integration ERP custom</div>
            <div class="pricing-feature">Account manager dedie</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    <div class="footer-logo">ChainIQ</div>
    <div style="font-size:13px;opacity:0.6;margin-bottom:16px">Plateforme agents IA supply chain — Maroc et Canada</div>
    <div class="footer-links">
        <a href="#" class="footer-link">A propos</a>
        <a href="#" class="footer-link">Agents</a>
        <a href="#" class="footer-link">Tarifs</a>
        <a href="#" class="footer-link">Contact</a>
    </div>
    <p style="margin-top:20px;font-size:12px;opacity:0.4">2026 ChainIQ. Tous droits reserves.</p>
</div>
""", unsafe_allow_html=True)