import streamlit as st
import random
import pandas as pd
from PIL import Image

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="GyaniAutoMFG AI",
    layout="wide"
)

# ---------------------------------
# GLOBAL CSS (from HTML theme)
# ---------------------------------

st.markdown("""
<style>

body{
background:#050709;
color:#f0f4f8;
font-family:sans-serif;
}

.navbar{
display:flex;
justify-content:space-between;
padding:15px 40px;
background:#0a0d12;
border-bottom:1px solid rgba(255,255,255,0.1);
}

.logo{
font-weight:800;
font-size:20px;
color:#00f5d4;
}

.hero-title{
font-size:60px;
font-weight:800;
text-align:center;
}

.hero-sub{
color:#8a9bb5;
text-align:center;
max-width:600px;
margin:auto;
}

.stat{
text-align:center;
}

.stat-num{
font-size:28px;
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

# ---------------------------------
# NAVBAR
# ---------------------------------

st.markdown("""
<div class="navbar">
<div class="logo">GyaniAutoMFG AI</div>
<div>Vision | Analytics | Supply Chain</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------
# HERO
# ---------------------------------

st.markdown("""
<div class="hero-title">
Build <span style="color:#00f5d4">Smarter</span> Factories<br>
with <span style="color:#3b82f6">Deep Learning</span>
</div>

<p class="hero-sub">
Vision AI defect detection, blockchain supply chains,
and real-time analytics — all in one platform.
</p>
""", unsafe_allow_html=True)

# HERO STATS

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Accuracy","99.2%")

with c2:
    st.metric("Efficiency","4.7x")

with c3:
    st.metric("Latency","50ms")

with c4:
    st.metric("Partners","247+")

st.divider()

# ---------------------------------
# VISION AI SECTION
# ---------------------------------

st.header("Vision AI Manufacturing")

tab1,tab2,tab3,tab4 = st.tabs([
"Live Demo",
"Roboflow",
"Workflow",
"Model Output"
])

# ---------------------------------
# LIVE DEMO
# ---------------------------------

with tab1:

    st.subheader("Defect Detection")

    col1,col2 = st.columns([2,1])

    with col1:

        img = st.file_uploader("Upload Conveyor Image")

        if img:
            image = Image.open(img)
            st.image(image,use_container_width=True)

    with col2:

        st.subheader("Detections")

        det1=random.randint(70,95)
        det2=random.randint(50,85)
        det3=random.randint(5,30)

        st.write("Crack")
        st.progress(det1/100)
        st.write(det1,"%")

        st.write("Misalignment")
        st.progress(det2/100)
        st.write(det2,"%")

        st.write("Good Product")
        st.progress(det3/100)
        st.write(det3,"%")

        frame=random.randint(200,600)
        st.metric("Frames Processed",frame)

        toggle = st.toggle("Enable Detection")

        if toggle:
            st.success("Detection Active")
        else:
            st.warning("Detection Paused")

# ---------------------------------
# ROBOFLOW
# ---------------------------------

with tab2:

    st.subheader("Roboflow Integration")

    st.code("""

from roboflow import Roboflow

rf = Roboflow(api_key="API_KEY")
project = rf.workspace("gyani").project("converyor_detect")
model = project.version(2).model

prediction = model.predict("image.jpg")
print(prediction.json())

""")

# ---------------------------------
# WORKFLOW
# ---------------------------------

with tab3:

    st.subheader("Manufacturing AI Pipeline")

    steps=[
    "Camera captures conveyor frame",
    "Image preprocessing",
    "CNN inference",
    "Object detection",
    "Defect classification",
    "Production analytics"
    ]

    for s in steps:
        st.write("✔",s)

# ---------------------------------
# MODEL OUTPUT
# ---------------------------------

with tab4:

    log = st.text_area(
    "Output Log",
    value="Model initialized...\nWaiting for frame input..."
    )

# ---------------------------------
# ANALYTICS
# ---------------------------------

st.divider()
st.header("Production Analytics")

data = pd.DataFrame({
"hour":[1,2,3,4,5,6],
"production":[120,150,170,200,230,260],
"defects":[12,10,9,7,6,5]
})

c1,c2 = st.columns(2)

with c1:
    st.subheader("Production")
    st.line_chart(data.set_index("hour")["production"])

with c2:
    st.subheader("Defect Rate")
    st.bar_chart(data.set_index("hour")["defects"])

# ---------------------------------
# ALERT BOX
# ---------------------------------

st.divider()
st.header("System Alerts")

if random.random()>0.7:
    st.error("⚠ Defect threshold exceeded")
else:
    st.success("System running normally")

# ---------------------------------
# FOOTER
# ---------------------------------

st.divider()
st.caption("GyaniAutoMFG AI Platform")
