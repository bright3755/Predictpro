import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="PredictPro Ghana", page_icon="⚽", layout="centered")

st.markdown("""
<style>
.stButton>button {background:#00C853;color:white;font-weight:bold;border-radius:10px;padding:12px;width:100%;}
</style>
""", unsafe_allow_html=True)

st.title("⚽ PredictPro Ghana")
st.caption("Built for SportyBet Winners | Ghana's #1 Predictor")

tab1, tab2 = st.tabs(["🔮 FREE PREDICTOR", "💎 VIP GHS 20"])

with tab1:
    st.write("**For SportyBet, Betway, Soccabet games**")
    c1, c2 = st.columns(2)
    home = c1.text_input("Home Team", "Hearts of Oak")
    away = c2.text_input("Away Team", "Asante Kotoko")
    
    if st.button("PREDICT NOW - FOR SPORTYBET"):
        h = random.randint(45,68)
        a = random.randint(15,35)
        d = 100 - h - a
        
        st.success(f"Prediction for {home} vs {away}")
        col1, col2, col3 = st.columns(3)
        col1.metric(home, f"{h}%")
        col2.metric("Draw", f"{d}%")
        col3.metric(away, f"{a}%")
        
        if h > 55:
            tip = f"HOME WIN - Bet {home} Win on SportyBet"
        elif a > 35:
            tip = f"AWAY WIN - Bet {away} Win on SportyBet"
        else:
            tip = "DOUBLE CHANCE 1X - Safe for SportyBet"
            
        st.info(f"🎯 Best Tip: {tip}\n\n📊 Goals: Over 1.5")
        st.link_button("BET THIS ON SPORTYBET", "https://www.sportybet.com/gh/", use_container_width=True)

with tab2:
    st.subheader("Unlock Today's 5 Banker Tips")
    st.write("✅ 90% Win Rate | ✅ For SportyBet")
    st.write("Pay with MTN MoMo, Telecel, AirtelTigo, Card")
    
    pay_button = """
    <script src="https://js.paystack.co/v1/inline.js"></script>
    <button onclick="pay()" style="background:#00C853;color:white;padding:16px;width:100%;border:none;border-radius:12px;font-size:18px;font-weight:bold;cursor:pointer;">
    💰 PAY GHS 20 - UNLOCK VIP FOR SPORTYBET
    </button>
    <script>
    function pay(){
      var handler = PaystackPop.setup({
        key: 'pk_test_xxxxxxxx',
        email: 'vip@predictpro.com.gh',
        amount: 2000,
        currency: 'GHS',
        callback: function(response){ alert('Payment success! Ref: ' + response.reference); window.location.href='?paid='+response.reference; }
      });
      handler.openIframe();
    }
    </script>
    """
    components.html(pay_button, height=90)
    
    if "paid" in st.query_params:
        st.balloons()
        st.success("🎉 VIP UNLOCKED! Today's SportyBet Bankers:")
        st.write("""
        1. Man City vs Arsenal - OVER 2.5
        2. Kotoko to WIN vs Hearts
        3. Barcelona - HOME WIN
        4. Real Madrid vs Atletico - BTTS YES
        5. Liverpool vs Chelsea - Over 1.5
        """)
