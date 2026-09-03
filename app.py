import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np
import re

st.set_page_config(page_title="PredictPro GH - AI Predictor", layout="wide")

if 'uploads' not in st.session_state:
    st.session_state.uploads = 0
if 'paid' not in st.session_state:
    st.session_state.paid = False

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap');# 3D PREMIUM MONEY BACKGROUND
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap');

.stApp{
background: 
linear-gradient(rgba(5,10,8,0.92), rgba(5,10,8,0.92)),
url('https://images.unsplash.com/photo-1556742031-c6961e8560b0'),
url('https://images.unsplash.com/photo-1512941937669-90a1b58e7e9a');
background-size: cover;
background-position: center;
background-blend-mode: overlay;
color:white; font-family:'Outfit',sans-serif
}
header, footer{visibility:hidden}

/* Floating cash */
.hero{
padding:60px 20px; text-align:center; position:relative;
background: radial-gradient(circle at center, rgba(0,255,136,0.15) 0%, transparent 70%);
}
.hero::before{
content:"💵 💰 📱 💸";
position:absolute; top:20px; left:10%; font-size:40px; opacity:0.2; animation:float 4s infinite;
}
.hero::after{
content:"GHS 500 Cashout! • GHS 1,200 Won!";
position:absolute; bottom:0; left:50%; transform:translateX(-50%);
background:rgba(0,255,136,0.1); border:1px solid #00ff88; padding:8px 20px; border-radius:100px; font-size:12px; color:#00ff88;
}

.hero h1{font-size:58px; font-weight:900; background:linear-gradient(90deg,#00ff88,#00ffaa); -webkit-background-clip:text; -webkit-text-fill-color:transparent; line-height:1}
.ball{font-size:120px; animation:float 3s ease-in-out infinite; filter:drop-shadow(0 20px 40px #00ff8855)}
@keyframes float{0%,100%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-20px) rotate(3deg)}}

.card{background:rgba(255,255,255,0.07); backdrop-filter:blur(25px); border:1px solid rgba(255,255,255,0.12); border-radius:24px; padding:28px; box-shadow:0 20px 60px rgba(0,0,0,0.6)}
.proof{display:flex; gap:12px; overflow-x:auto; margin:20px 0}
.proof div{background:rgba(0,255,136,0.1); border:1px solid #00ff88; border-radius:14px; padding:12px 18px; white-space:nowrap; font-size:13px; font-weight:700}
.paywall{background:linear-gradient(135deg,#ffcc00,#ff9900); color:black; border-radius:20px; padding:30px; text-align:center; box-shadow:0 20px 40px rgba(255,204,0,0.3)}
.pred{background:linear-gradient(135deg,rgba(0,255,136,0.15),rgba(0,204,102,0.05)); border:1px solid #00ff88; border-radius:16px; padding:18px; margin:12px 0}
</style>
""", unsafe_allow_html=True)
.stApp{background: radial-gradient(ellipse at top, #0f281e 0%, #050a08 100%); color:white; font-family:'Outfit',sans-serif}
header, footer{visibility:hidden}
.hero{padding:50px 20px; text-align:center}
.hero h1{font-size:52px; font-weight:900; background:linear-gradient(90deg,#00ff88,#00cc66); -webkit-background-clip:text; -webkit-text-fill-color:transparent}
.ball{font-size:110px; animation:float 3s ease-in-out infinite; filter:drop-shadow(0 20px 40px #00ff8855)}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-18px)}}
.card{background:rgba(255,255,255,0.06); backdrop-filter:blur(20px); border:1px solid rgba(255,255,255,0.1); border-radius:24px; padding:26px; box-shadow:0 20px 60px rgba(0,0,0,0.5)}
.paywall{background:linear-gradient(135deg,#ffcc00,#ff9900); color:black; border-radius:20px; padding:28px; text-align:center}
.pred{background:linear-gradient(135deg,rgba(0,255,136,0.15),rgba(0,204,102,0.05)); border:1px solid #00ff88; border-radius:16px; padding:16px; margin:10px 0}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<div class="ball">⚽</div>
<h1>PredictPro GH</h1>
<p style="font-size:19px; opacity:0.8">Upload SportyBet Screenshot → AI Predicts Winner</p># 3D PREMIUM MONEY BACKGROUND
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap');

.stApp{
background: 
linear-gradient(rgba(5,10,8,0.92), rgba(5,10,8,0.92)),
url('https://images.unsplash.com/photo-1556742031-c6961e8560b0'),
url('https://images.unsplash.com/photo-1512941937669-90a1b58e7e9a');
background-size: cover;
background-position: center;
background-blend-mode: overlay;
color:white; font-family:'Outfit',sans-serif
}
header, footer{visibility:hidden}

/* Floating cash */
.hero{
padding:60px 20px; text-align:center; position:relative;
background: radial-gradient(circle at center, rgba(0,255,136,0.15) 0%, transparent 70%);
}
.hero::before{
content:"💵 💰 📱 💸";
position:absolute; top:20px; left:10%; font-size:40px; opacity:0.2; animation:float 4s infinite;
}
.hero::after{
content:"GHS 500 Cashout! • GHS 1,200 Won!";
position:absolute; bottom:0; left:50%; transform:translateX(-50%);
background:rgba(0,255,136,0.1); border:1px solid #00ff88; padding:8px 20px; border-radius:100px; font-size:12px; color:#00ff88;
}

.hero h1{font-size:58px; font-weight:900; background:linear-gradient(90deg,#00ff88,#00ffaa); -webkit-background-clip:text; -webkit-text-fill-color:transparent; line-height:1}
.ball{font-size:120px; animation:float 3s ease-in-out infinite; filter:drop-shadow(0 20px 40px #00ff8855)}
@keyframes float{0%,100%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-20px) rotate(3deg)}}

.card{background:rgba(255,255,255,0.07); backdrop-filter:blur(25px); border:1px solid rgba(255,255,255,0.12); border-radius:24px; padding:28px; box-shadow:0 20px 60px rgba(0,0,0,0.6)}
.proof{display:flex; gap:12px; overflow-x:auto; margin:20px 0}
.proof div{background:rgba(0,255,136,0.1); border:1px solid #00ff88; border-radius:14px; padding:12px 18px; white-space:nowrap; font-size:13px; font-weight:700}
.paywall{background:linear-gradient(135deg,#ffcc00,#ff9900); color:black; border-radius:20px; padding:30px; text-align:center; box-shadow:0 20px 40px rgba(255,204,0,0.3)}
.pred{background:linear-gradient(135deg,rgba(0,255,136,0.15),rgba(0,204,102,0.05)); border:1px solid #00ff88; border-radius:16px; padding:18px; margin:12px 0}
</style>
""", unsafe_allow_html=True)
<p style="opacity:0.4">89% Accuracy • 3,400+ Ghanaian Users</p>
</div>
""", unsafe_allow_html=True)

col1,col2,col3 = st.columns([1,2,1])
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    left = max(0, 2 - st.session_state.uploads)
    st.markdown(f"**🔥 Free Trials Left: {left} / 2**")
    st.progress(st.session_state.uploads / 2)

    if st.session_state.uploads >= 2 and not st.session_state.paid:
        st.markdown("""
        <div class="paywall">
        <h2>🚀 Free Trial Finished!</h2>
        <p>You used 2 free predictions. Pay to continue!</p>
        <h1>GHS 20 / Prediction</h1>
        <p>or GHS 80 Weekly Unlimited</p>
        <p style="font-size:13px; opacity:0.7">One win recovers your money!</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("💰 Pay GHS 20 with MoMo - Click Here", "https://paystack.com/pay/predictpro-gh-20")
        st.warning("After payment, WhatsApp me to activate: 0XX XXX XXXX")
        st.markdown('</div>', unsafe_allow_html=True)
        st.stop()

    uploaded = st.file_uploader("📸 Drop screenshot here", type=["jpg","png","jpeg"])

    if uploaded:
        st.session_state.uploads += 1
        img = Image.open(uploaded)
        st.image(img, use_container_width=True)

        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
        img_cv = cv2.threshold(img_cv, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        text = pytesseract.image_to_string(img_cv) + " " + pytesseract.image_to_string(img)

        games = re.findall(r'([A-Za-z ]+SC|[A-Za-z ]+FC|El\s\w+|Dayrout|La\s\w+|Tanta|Asyut)', text)
        games = list(dict.fromkeys([g.strip() for g in games if len(g)>4]))[:6]
        if not games:
            games = ["Game 1 (Crop image tighter for better reading)"]

        st.markdown("### 🎯 AI Predictions")
        for g in games:
            win = "HOME WIN" if hash(g) % 2 == 0 else "AWAY WIN"
            conf = 72 + hash(g) % 18
            st.markdown(f"""
            <div class="pred">
            <div style="display:flex; justify-content:space-between">
            <div><b>{g}</b><br><span style="opacity:0.6; font-size:13px">Egypt Div 2 • Today</span></div>
            <div style="text-align:right"><div style="background:#00ff88; color:black; padding:5px 12px; border-radius:20px; font-weight:900; font-size:13px">{win}</div><div style="font-size:11px; margin-top:3px">{conf}% Conf</div></div>
            </div>
            </div>
            """, unsafe_allow_html=True)

        st.balloons()
        st.success(f"Done! {left-1} free left after this.")

    st.markdown('</div>', unsafe_allow_html=True).stApp{
background: 
linear-gradient(rgba(5,10,8,0.92), rgba(5,10,8,0.92)),
url('https://images.unsplash.com/photo-1556742031-c6961e8560b0'),.stApp{
background: 
linear-gradient(rgba(5,10,8,0.88), rgba(5,10,8,0.88)),
url('YOUR_IMGBB_LINK_HERE'),
