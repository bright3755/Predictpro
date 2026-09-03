import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="PredictPro Ghana", page_icon="⚽", layout="centered")

# --- HEADER WITH CASHOUT GRAPHIC ---
st.markdown("""
<style>
.cashout-box {
    background: linear-gradient(135deg, #00C853, #00B248);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
.ticket {
    background: white;
    color: #222;
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cashout-box">
    <h2>💸 SPORTYBET CASHOUT ALERT!</h2>
    <h3>GH₵ 3,450.00 WON!</h3>
    <div class="ticket">
        ✅ Hearts of Oak vs Kotoko - HOME WIN - ODDS 2.15 <br>
        ✅ Arsenal vs Chelsea - OVER 2.5 - ODDS 1.80 <br>
        <b>TOTAL ODDS: 3.87 | STAKE: GH₵ 200 | WIN: GH₵ 3,450</b><br>
        <span style="color:green; font-weight:bold;">STATUS: CASHOUT AVAILABLE ✅</span>
    </div>
    <p>Last winners from PredictPro VIP!</p>
</div>
""", unsafe_allow_html=True)

st.title("⚽ PredictPro Ghana - VIP Predictions")

# --- PREDICTION ---
match = st.selectbox("Select Match", ["Hearts of Oak vs Asante Kotoko", "Arsenal vs Chelsea", "Real Madrid vs Barcelona", "Man City vs Liverpool"])
if st.button("🎯 GET FREE PREDICTION"):
    pred = random.choice(["HOME WIN - 78% Confidence", "OVER 2.5 GOALS - 85% Confidence", "BTTS YES - 72% Confidence"])
    st.success(f"Free Tip for {match}: **{pred}**")
    st.warning("🔒 For 5 ODDS VIP ACCA + Correct Score, Unlock VIP for GH₵ 20")

st.divider()

# --- VIP SECTION ---
st.subheader("🔐 VIP SECTION - GH₵ 20")

# Simulate payment unlock with checkbox for now (replace with Paystack later)
paid = st.checkbox("I have paid GH₵ 20 via MTN MoMo (Check to unlock VIP)")

if not paid:
    st.markdown("### Pay GH₵ 20 to Unlock:")
    st.markdown("- 5 ODDS Banker Acca\n- Correct Score VIP\n- Upload Your Slip for Review\n- Daily Cashout Tickets")
    st.link_button("💳 PAY WITH MTN MoMo - GH₵ 20", "https://paystack.com/pay/predictpro-ghana")
    st.caption("After payment, CHECK the box above to unlock")
else:
    st.balloons()
    st.success("✅ VIP UNLOCKED! Welcome Boss!")
    
    st.markdown("""
    <div style="background:#E8F5E9; padding:15px; border-radius:10px; border:2px dashed #00C853;">
    <h4>🎯 TODAY'S VIP ACCA - 5.67 ODDS</h4>
    1. Bayern vs Dortmund - OVER 2.5 (1.55)<br>
    2. Hearts vs Kotoko - HOME WIN (2.15)<br>
    3. Man City to WIN (1.40)<br>
    <b>BOOK THIS ON SPORTYBET NOW!</b>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    # --- SCREENSHOT UPLOAD ---
    st.subheader("📸 Upload Your SportyBet Slip Screenshot")
    st.write("Upload your bet slip after booking on SportyBet, I will review it for cashout chance!")
    
    uploaded = st.file_uploader("Choose your SportyBet screenshot", type=["jpg", "png", "jpeg"])
    
    if uploaded:
        st.image(uploaded, caption="Your SportyBet Slip", use_column_width=True)
        st.success("✅ Screenshot Received! Good luck! This ticket will CASHOUT! 💰")
        st.markdown("**My Analysis:** Strong ticket! Hold for cashout at 70% profit.")
    
    st.divider()
    st.markdown("### 💰 Recent Cashouts from Members")
    st.image("https://i.ibb.co/3fL0X7n/sportybet-cashout.jpg", caption="GH₵ 1,200 Cashout - Member: Kwame from Kumasi", use_column_width=True)

st.caption("PredictPro Ghana - Not affiliated with SportyBet. 18+ Gamble Responsibly")
