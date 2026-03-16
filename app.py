import streamlit as st
import time
import random
from PIL import Image

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="GyaniAutoMFG AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS (from your HTML theme)
# ---------------------------------------------------
st.markdown("""
<style>

body {
    background-color:#050709;
    color:white;
}

.hero-title{
    font-size:60px;
    font-weight:800;
}

.hero-subtitle{
    color:#8a9bb5;
    font-size:18px;
}

.stat-box{
    text-align:center;
}

.stat-number{
    font-size:36px;
    font-weight:800;
    color:#00f5d4;
}

.card{
    background:#141820;
    padding:20px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.markdown("""
<div style='text-align:center'>
<div class='hero-title'>
Build <span style='color:#00f5d4'>Smarter</span> Factories<br>
with <span style='color:#3b82f6'>Deep Learning</span>
</div>

<p class='hero-subtitle'>
Vision AI defect detection, blockchain supply chains, and real-time analytics — all in one platform.
</p>
</div>
""", unsafe_allow_html=True)


col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Detection Accuracy","99.2%")

with col2:
    st.metric("Efficiency Gain","4.7x")

with col3:
    st.metric("Inference Latency","50ms")

with col4:
    st.metric("Industry Partners","247+")

st.divider()

# ---------------------------------------------------
# VISION AI SECTION
# ---------------------------------------------------

st.header("AI Powered Defect Detection")

tab1,tab2,tab3,tab4 = st.tabs(
    ["Live Demo","Roboflow Projects","Workflows","Model Output"]
)

# ---------------------------------------------------
# LIVE DEMO
# ---------------------------------------------------

with tab1:

    st.subheader("Upload Conveyor Image")

    img = st.file_uploader("Upload Image",type=["jpg","png"])

    if img:

        image = Image.open(img)
        st.image(image,use_container_width=True)

        st.success("Model Running...")

        crack = random.randint(70,95)
        misalignment = random.randint(50,85)
        good = random.randint(5,30)

        st.write("### Detection Confidence")

        st.progress(crack/100)
        st.write("Crack:",crack,"%")

        st.progress(misalignment/100)
        st.write("Misalignment:",misalignment,"%")

        st.progress(good/100)
        st.write("Non Defective:",good,"%")

# ---------------------------------------------------
# ROBOFLOW PROJECTS
# ---------------------------------------------------

with tab2:

    st.subheader("Roboflow Model")

    st.markdown("""
Roboflow model can be embedded here or accessed using inference API.

Example:
