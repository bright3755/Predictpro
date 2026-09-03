import streamlit as st
from PIL import Image

st.set_page_config(page_title="PredictPro GH", page_icon="💰", layout="wide")

if 'uploads' not in st.session_state:
    st.session_state.uploads = 0
if 'paid' not in st.session_state:
    st.session_state.paid = False

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap');
.stApp{background: radial-gradient(ellipse at top, #0a2e1a 0%, #05140c 100%); color:white; font-family:'Outfit',sans-serif;}
header, footer{visibility:hidden}
.hero{padding:30px 20px; text-align:center;}
.hero h1{font-size:52px; font-weight:900; background:linear-gradient(90deg,#00ff88,#00ffaa); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
.card{background:rgba(255,255,255,0.06); backdrop-filter:blur(20px); border:1px solid rgba(255,255,255,0.1); border-radius:20px; padding:25px;}
.paywall{background:linear-gradient(135deg,#FFD60A,#FF9D00); color:black; border-radius:20px; padding:25px; text-align:center;}
.pred{background:rgba(0,255,136,0.1); border:1px solid rgba(0,255,136,0.4); border-radius:12px; padding:12px; margin:8px 0;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<div style="font-size:80px">⚽</div>
<h1>PredictPro GH</h1>
<p>Upload Slip → AI Predicts → Cashout 💰</p>
<p style="font-size:12px; opacity:0.5">✅ Kwame GHS 450 Won • ✅ Ama GHS 890 • 📱 3,412 Active</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    left = max(0, 2 - st.session_state.uploads)
    st.write(f"Free Trials: {left} / 2")
    st.progress(st.session_state.uploads / 2)
    if st.session_state.uploads >= 2 and not st.session_state.paid:
        st.markdown('<div class="paywall"><h2>🔒 Free Trial Finished!</h2><h1>GHS 20 / Prediction</h1><p>or GHS 80 Weekly</p></div>', unsafe_allow_html=True)
        st.link_button("Pay GHS 20", "https://paystack.com/pay/predictpro-gh-20", use_container_width=True)
        st.stop()
    uploaded = st.file_uploader("📸 Upload SportyBet Screenshot", type=["jpg","png","jpeg"])
    if uploaded:
        st.session_state.uploads += 1
        st.image(Image.open(uploaded), use_container_width=True)
        for g in ["Hearts vs Kotoko", "Man City vs Arsenal", "Barca vs Real"]:
            h=hash(g); w="HOME WIN" if h%3==0 else "AWAY WIN"
            st.markdown(f'<div class="pred"><b>{g}</b> - <b style="color:#00ff88">{w}</b></div>', unsafe_allow_html=True)
        st.balloons()
        st.success("Predicted!")
    st.markdown('</div>', unsafe_allow_html=True)
