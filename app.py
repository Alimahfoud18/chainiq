import streamlit as st

st.set_page_config(
    page_title="ChainIQ — Agents IA Supply Chain",
    page_icon="⛓️",
    layout="wide"
)

st.markdown("""
<style>
    /* Global */
    .main { padding: 0 !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    
    /* Hero */
    .hero {
        background: linear-gradient(135deg, #0F6E56 0%, #1D9E75 50%, #2DD4A0 100%);
        padding: 80px 60px;
        text-align: center;
        color: white;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 13px;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.3);
    }
    .hero h1 {
        font-size: 52px;
        font-weight: 800;
        margin: 0 0 16px;
        line-height: 1.2;
    }
    .hero p {
        font-size: 20px;
        opacity: 0.9;
        max-width: 600px;
        margin: 0 auto 32px;
        line-height: 1.6;
    }
    .hero-btns { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }
    .btn-primary {
        background: white;
        color: #0F6E56;
        padding: 14px 32px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px;
        text-decoration: none;
        border: none;
        cursor: pointer;
    }
    .btn-secondary {
        background: transparent;
        color: white;
        padding: 14px 32px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 16px;
        text-decoration: none;
        border: 2px solid rgba(255,255,255,0.5);
        cursor: pointer;
    }

    /* Stats */
    .stats {
        background: #0F6E56;
        padding: 24px 60px;
        display: flex;
        justify-content: center;
        gap: 60px;
        flex-wrap: wrap;
    }
    .stat { text-align: center; color: white; }
    .stat-val { font-size: 28px; font-weight: 700; }
    .stat-lbl { font-size: 13px; opacity: 0.8; }

    /* Sections */
    .section { padding: 60px; }
    .section-alt { background: #F8FAF9; }
    .section-title {
        font-size: 32px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 8px;
        color: #1a1a1a;
    }
    .section-sub {
        text-align: center;
        color: #666;
        font-size: 16px;
        margin-bottom: 40px;
    }

    /* Agent cards */
    .agents-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        max-width: 1000px;
        margin: 0 auto;
    }
    .agent-card {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
        cursor: pointer;
    }
    .agent-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(0,0,0,0.1);
    }
    .agent-avatar {
        width: 64px;
        height: 64px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: 700;
        margin: 0 auto 12px;
        color: white;
    }
    .agent-name { font-size: 18px; font-weight: 700; margin-bottom: 4px; }
    .agent-role { font-size: 12px; color: #1D9E75; font-weight: 600; margin-bottom: 8px; }
    .agent-desc { font-size: 13px; color: #666; line-height: 1.5; }
    .agent-badge {
        display: inline-block;
        font-size: 11px;
        padding: 3px 10px;
        border-radius: 20px;
        margin-top: 12px;
        font-weight: 500;
    }

    /* Pricing */
    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        max-width: 900px;
        margin: 0 auto;
    }
    .pricing-card {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 32px 24px;
        text-align: center;
    }
    .pricing-card.featured {
        border: 2px solid #1D9E75;
        position: relative;
    }
    .pricing-badge {
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        background: #1D9E75;
        color: white;
        padding: 4px 16px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    .pricing-name { font-size: 18px; font-weight: 700; margin-bottom: 8px; }
    .pricing-price { font-size: 36px; font-weight: 800; color: #1D9E75; }
    .pricing-period { font-size: 13px; color: #666; margin-bottom: 20px; }
    .pricing-feature {
        font-size: 13px;
        color: #444;
        padding: 6px 0;
        border-bottom: 1px solid #F3F4F6;
        text-align: left;
    }
    .pricing-btn {
        display: block;
        margin-top: 20px;
        padding: 12px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 14px;
        cursor: pointer;
        border: none;
        width: 100%;
    }
    .pricing-btn-primary { background: #1D9E75; color: white; }
    .pricing-btn-secondary { background: #F3F4F6; color: #333; }

    /* Footer */
    .footer {
        background: #0F2420;
        color: white;
        padding: 40px 60px;
        text-align: center;
    }
    .footer-logo { font-size: 24px; font-weight: 800; margin-bottom: 8px; }
    .footer-sub { font-size: 13px; opacity: 0.6; margin-bottom: 20px; }
    .footer-links { display: flex; gap: 24px; justify-content: center; flex-wrap: wrap; }
    .footer-link { color: rgba(255,255,255,0.6); font-size: 13px; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">🇲🇦 Maroc & 🇨🇦 Canada — Plateforme IA Supply Chain</div>
    <h1>Votre équipe supply chain<br>augmentée par l'IA</h1>
    <p>Des agents IA spécialisés qui optimisent votre chaîne logistique — sans recrutement, sans formation, disponibles 24h/24.</p>
    <div class="hero-btns">
        <a href="#agents" class="btn-primary">🚀 Découvrir les agents</a>
        <a href="#pricing" class="btn-secondary">Voir les tarifs</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── STATS ──────────────────────────────────────────
st.markdown("""
<div class="stats">
    <div class="stat"><div class="stat-val">6</div><div class="stat-lbl">Agents spécialisés</div></div>
    <div class="stat"><div class="stat-val">24/7</div><div class="stat-lbl">Disponibilité</div></div>
    <div class="stat"><div class="stat-val">-30%</div><div class="stat-lbl">Coûts logistiques</div></div>
    <div class="stat"><div class="stat-val">MAD & CAD</div><div class="stat-lbl">Facturation locale</div></div>
</div>
""", unsafe_allow_html=True)

# ── AGENTS ──────────────────────────────────────────
st.markdown("""
<div class="section" id="agents">
    <p class="section-title">Votre équipe IA supply chain</p>
    <p class="section-sub">Chaque agent est un expert métier — pas un chatbot générique</p>
    <div class="agents-grid">
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#1D9E75,#0F6E56)">KA</div>
            <div class="agent-name">Karima</div>
            <div class="agent-role">Prévision de la demande</div>
            <div class="agent-desc">Anticipe vos ventes avec Prophet, ARIMA et XGBoost. Détecte la saisonnalité, le Ramadan, les tendances.</div>
            <span class="agent-badge" style="background:#E1F5EE;color:#0F6E56">✅ Disponible</span>
        </div>
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#7F77DD,#534AB7)">YO</div>
            <div class="agent-name">Youssef</div>
            <div class="agent-role">Optimisation des stocks</div>
            <div class="agent-desc">Calcule votre EOQ dynamique, stock de sécurité et point de réapprovisionnement optimal.</div>
            <span class="agent-badge" style="background:#EEEDFE;color:#534AB7">🔨 En construction</span>
        </div>
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#EF9F27,#BA7517)">NA</div>
            <div class="agent-name">Nadia</div>
            <div class="agent-role">Gestion fournisseurs</div>
            <div class="agent-desc">Score vos fournisseurs, suit les délais de livraison et vous alerte sur les retards critiques.</div>
            <span class="agent-badge" style="background:#FAEEDA;color:#854F0B">🔜 Bientôt</span>
        </div>
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#E24B4A,#993C1D)">OM</div>
            <div class="agent-name">Omar</div>
            <div class="agent-role">Transport & livraisons</div>
            <div class="agent-desc">Optimise vos routes, suit vos expéditions et gère vos coûts logistiques Tanger Med.</div>
            <span class="agent-badge" style="background:#FAECE7;color:#993C1D">🔜 Bientôt</span>
        </div>
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#378ADD,#185FA5)">SI</div>
            <div class="agent-name">Siham</div>
            <div class="agent-role">Reporting & KPIs</div>
            <div class="agent-desc">Génère vos tableaux de bord supply chain automatiquement et envoie des rapports PDF à la direction.</div>
            <span class="agent-badge" style="background:#E6F1FB;color:#185FA5">🔜 Bientôt</span>
        </div>
        <div class="agent-card">
            <div class="agent-avatar" style="background:linear-gradient(135deg,#888,#444)">AM</div>
            <div class="agent-name">Amine</div>
            <div class="agent-role">Chef d'orchestre</div>
            <div class="agent-desc">Coordonne tous les agents, répond à vos questions générales et pilote votre supply chain globale.</div>
            <span class="agent-badge" style="background:#F1EFE8;color:#5F5E5A">🔜 Bientôt</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── PRICING ──────────────────────────────────────────
st.markdown("""
<div class="section section-alt" id="pricing">
    <p class="section-title">Tarifs simples et transparents</p>
    <p class="section-sub">Facturation en MAD pour le Maroc, CAD pour le Canada</p>
    <div class="pricing-grid">
        <div class="pricing-card">
            <div class="pricing-name">Starter</div>
            <div class="pricing-price">1 500</div>
            <div class="pricing-period">MAD / mois</div>
            <div class="pricing-feature">✅ Agent Karima</div>
            <div class="pricing-feature">✅ Agent Youssef</div>
            <div class="pricing-feature">✅ Dashboard web</div>
            <div class="pricing-feature">✅ Support email</div>
            <div class="pricing-feature">❌ WhatsApp</div>
            <div class="pricing-feature">❌ Intégration ERP</div>
            <button class="pricing-btn pricing-btn-secondary">Commencer</button>
        </div>
        <div class="pricing-card featured">
            <div class="pricing-badge">⭐ Recommandé</div>
            <div class="pricing-name">Pro</div>
            <div class="pricing-price">5 000</div>
            <div class="pricing-period">MAD / mois</div>
            <div class="pricing-feature">✅ 6 agents complets</div>
            <div class="pricing-feature">✅ Dashboard avancé</div>
            <div class="pricing-feature">✅ WhatsApp Business</div>
            <div class="pricing-feature">✅ Intégration Odoo</div>
            <div class="pricing-feature">✅ Onboarding 1:1</div>
            <div class="pricing-feature">✅ Support prioritaire</div>
            <button class="pricing-btn pricing-btn-primary">Démarrer l'essai gratuit</button>
        </div>
        <div class="pricing-card">
            <div class="pricing-name">Enterprise</div>
            <div class="pricing-price">Sur mesure</div>
            <div class="pricing-period">Contrat annuel</div>
            <div class="pricing-feature">✅ Agents personnalisés</div>
            <div class="pricing-feature">✅ Déploiement on-premise</div>
            <div class="pricing-feature">✅ Intégration ERP custom</div>
            <div class="pricing-feature">✅ Formation équipe</div>
            <div class="pricing-feature">✅ SLA garanti</div>
            <div class="pricing-feature">✅ Account manager dédié</div>
            <button class="pricing-btn pricing-btn-secondary">Nous contacter</button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ──────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-logo">⛓️ ChainIQ</div>
    <div class="footer-sub">Plateforme d'agents IA supply chain — Maroc & Canada</div>
    <div class="footer-links">
        <a href="#" class="footer-link">À propos</a>
        <a href="#" class="footer-link">Agents</a>
        <a href="#" class="footer-link">Tarifs</a>
        <a href="#" class="footer-link">Contact</a>
        <a href="#" class="footer-link">Politique de confidentialité</a>
    </div>
    <p style="margin-top:20px;font-size:12px;opacity:0.4">© 2026 ChainIQ. Tous droits réservés.</p>
</div>
""", unsafe_allow_html=True)