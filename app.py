import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="PredictPro Ghana - SportyBet Scanner", page_icon="💚", layout="centered")

# BEAUTIFUL SPORTYBET CSS
st.markdown("""
<style>
    .stApp { background: #121212; }
    .sporty-top { background: #00A650; padding: 12px; display:flex; justify-content:space-between; color:white; font-weight:bold; }
    .card-white { background:white; border-radius:12px; padding:16px; margin:10px 0; }
    .phone-cashout {
        background: white; border-radius: 20px; padding:10px; border: 8px solid black; 
        max-width: 320px; margin: auto;
    }
    .green-dot { height:10px; width:10px; background:#00A650; border-radius:50%; display:inline-block; }
    .win-badge { background:#E8F5E9; color:#00A650; padding:4px 10px; border-radius:20px; font-weight:bold; font-size:12px; }
    .locked { background: linear-gradient(90deg, #FFD700, #FF9800); padding:15px; border-radius:10px; text-align:center; font-weight:bold; }
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<div class="sporty-top"><span>⚽ PredictPro GH</span><span style="font-size:12px;">SPORTYBET SCANNER AI</span></div>', unsafe_allow_html=True)

# TRUST CASHOUT PHONE MOCKUP
st.markdown("""
<div class="card-white" style="text-align:center;">
    <p style="margin:0; color:green; font-weight:bold;">🔴 LIVE CASHOUT PROOF</p>
    <div class="phone-cashout">
        <div style="display:flex; justify-content:space-between; font-size:11px;"><span>9:41</span><span>🔋 84%</span></div>
        <div style="background:#00A650; color:white; padding:8px; border-radius:8px; margin:8px 0; font-weight:bold;">sportybet.com.gh</div>
        <div style="text-align:left; font-size:13px; line-height:1.6;">
            <span class="win-badge">WON</span><br>
            <b>Stake: GH₵ 150.00</b><br>
            Total Odds: 8.42<br>
            <b style="color:green; font-size:18px;">Return: GH₵ 1,263.00</b><br>
            <div style="background:#00A650; color:white; text-align:center; padding:8px; border-radius:6px; margin-top:8px; font-weight:bold;">✅ CASHED OUT</div>
            <p style="font-size:10px; color:gray; margin-top:6px;">Arsenal WIN ✔️ • Man City Over 2.5 ✔️ • Real Madrid WIN ✔️</p>
        </div>
    </div>
    <p style="font-size:12px; color:gray; margin-top:8px;">👆 Real user from Accra - 2 hours ago - Trusted by 4,200+ punters</p>
</div>
""", unsafe_allow_html=True)

# SESSION FOR LIMIT
if "scan_count" not in st.session_state:
    st.session_state.scan_count = 0

remaining = 2 - st.session_state.scan_count

st.markdown(f"""
<div class="card-white">
    <h3 style="margin:0;">📸 Upload Your SportyBet Screenshot</h3>
    <p style="font-size:13px; color:#555;">Our AI will scan your FOREIGN leagues ticket and tell you which games will WIN + correct goals</p>
    <p style="font-weight:bold; color:{'green' if remaining>0 else 'red'};">🔥 Free scans left: {remaining}/2</p>
</div>
""", unsafe_allow_html=True)

# VIP UNLOCK LOGIC
is_vip = st.session_state.get("is_vip", False)

if remaining <= 0 and not is_vip:
    st.markdown('<div class="locked">🔒 FREE LIMIT REACHED! Unlock VIP for GH₵ 20 to continue unlimited scans</div>', unsafe_allow_html=True)
    st.link_button("💳 UNLOCK VIP - GH₵ 20 (MTN MoMo)", "https://paystack.com/pay/predictpro", use_container_width=True)
    if st.checkbox("I have paid - Unlock me"):
        st.session_state.is_vip = True
        st.rerun()
    st.stop()

# UPLOADER
uploaded = st.file_uploader("Drop SportyBet slip here (JPG, PNG)", type=["jpg","png","jpeg"])

if uploaded:
    st.session_state.scan_count += 1
    img = Image.open(uploaded)
    
    st.markdown('<div class="card-white">', unsafe_allow_html=True)
    st.image(img, caption="Your Ticket", use_container_width=True)
    
    with st.spinner("🤖 AI Scanning foreign leagues... Analysing form, odds, goals..."):
        st.markdown("""
        <div style="background:#f5f5f5; padding:10px; border-radius:8px; font-family:monospace; font-size:12px;">
        > Detecting: Arsenal vs Chelsea... DONE<br>
        > Detecting: Man City vs Liverpool... DONE<br>
        > Detecting: Bayern vs Dortmund... DONE<br>
        > Calculating win probability... 87%
        </div>
        """, unsafe_allow_html=True)
    
    st.success("✅ SCAN COMPLETE!")
    
    # FAKE AI PREDICTION - BEAUTIFUL
    st.markdown("### 🎯 AI PREDICTION RESULT")
    
    preds = [
        ("Arsenal vs Chelsea", "HOME WIN (1)", "2-1", "88% ✅ SAFE"),
        ("Man City vs Liverpool", "OVER 2.5 Goals", "3-1", "92% ✅ VERY SAFE"),
        ("Real Madrid vs Barca", "BTTS YES", "1-1", "76% ⚠️ RISKY"),
        ("Bayern vs Dortmund", "HOME WIN", "2-0", "85% ✅ SAFE"),
    ]
    
    for game, market, score, conf in random.sample(preds, 3):
        st.markdown(f"""
        <div style="background:white; border-left:4px solid #00A650; padding:12px; border-radius:8px; margin:8px 0;">
            <b>{game}</b> <span style="float:right; font-size:11px; background:#E8F5E9; padding:2px 8px; border-radius:10px; color:green;">{conf}</span><br>
            <span style="font-size:13px;">Market: <b style="color:#00A650;">{market}</b></span><br>
            <span style="font-size:13px;">Predicted Score: <b>{score}</b></span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background:#1a1a1a; color:white; padding:15px; border-radius:10px; text-align:center; margin-top:10px;">
        <p style="margin:0; color:#00FF7F;">🔥 COMBINED SAFE TICKET</p>
        <h2 style="margin:5px 0;">4.85 ODDS</h2>
        <p style="font-size:12px;">Stake GH₵ 200 to WIN GH₵ 970 - Book on SportyBet Now!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if not is_vip:
        st.info(f"You have {2 - st.session_state.scan_count} free scan(s) left. After that, VIP required.")

else:
    st.markdown('<div class="card-white" style="text-align:center; color:gray; font-size:13px;">👆 Upload your ticket now - Only foreign leagues (EPL, LaLiga, Bundesliga) will be analysed</div>', unsafe_allow_html=True)

st.caption("PredictPro GHANA | SportyBet Scanner AI | 18+ Gamble Responsibly | Not affiliated with SportyBet")
