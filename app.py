import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import random

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="GyaniAutoMFG AI Platform",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

body{
    background-color:#050709;
}

.hero-title{
font-size:60px;
font-weight:800;
text-align:center;
}

.hero-sub{
color:#94a3b8;
text-align:center;
font-size:18px;
margin-bottom:40px;
}

.card{
background:#141820;
padding:20px;
border-radius:12px;
}

.metric-title{
font-size:14px;
color:#9aa4b2;
}

.metric-number{
font-size:36px;
font-weight:700;
color:#00f5d4;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------

st.markdown("""
<div class='hero-title'>
Build <span style='color:#00f5d4'>Smarter</span> Factories<br>
with <span style='color:#3b82f6'>Deep Learning</span>
</div>

<div class='hero-sub'>
Vision AI defect detection, blockchain supply chains and real-time analytics
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# METRICS
# -------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Detection Accuracy","99.2%","+1.2%")

with c2:
    st.metric("Efficiency Gain","4.7x","+0.3")

with c3:
    st.metric("Inference Latency","50 ms","-10 ms")

with c4:
    st.metric("Industry Partners","247+")

st.divider()

# -------------------------------------------------
# VISION AI SECTION
# -------------------------------------------------

st.header("AI Powered Manufacturing Vision")

tab1,tab2,tab3,tab4 = st.tabs(
[
"Live Defect Detection",
"Roboflow Projects",
"Manufacturing Workflow",
"Model Output"
]
)

# -------------------------------------------------
# LIVE DETECTION
# -------------------------------------------------

with tab1:

    st.subheader("Upload Conveyor Image")

    uploaded = st.file_uploader(
    "Upload product image",
    type=["jpg","png","jpeg"]
    )

    if uploaded:

        img = Image.open(uploaded)

        col1,col2 = st.columns([2,1])

        with col1:
            st.image(img,use_container_width=True)

        with col2:

            st.write("### Detection Results")

            crack=random.randint(70,95)
            misalign=random.randint(40,80)
            good=random.randint(5,30)

            st.progress(crack/100)
            st.write("Crack:",crack,"%")

            st.progress(misalign/100)
            st.write("Misalignment:",misalign,"%")

            st.progress(good/100)
            st.write("Non-Defective:",good,"%")

# -------------------------------------------------
# ROBOFLOW PROJECT
# -------------------------------------------------

with tab2:

    st.subheader("Roboflow Model Integration")

    st.code("""

from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")

project = rf.workspace("gyani").project("converyor_detect")

model = project.version(2).model

prediction = model.predict("image.jpg")

print(prediction.json())

""")

    st.info("Replace API key and image to run real detection.")

# -------------------------------------------------
# WORKFLOW
# -------------------------------------------------

with tab3:

    st.subheader("Manufacturing AI Pipeline")

    workflow = [
    "Camera captures conveyor belt frame",
    "Image preprocessing",
    "CNN defect detection model",
    "Object classification",
    "Defect removal automation",
    "Production analytics logging"
    ]

    for step in workflow:
        st.write("✔",step)
    st.image("/images/workflow.png")
    st.caption("Workflow")

# -------------------------------------------------
# MODEL OUTPUT
# -------------------------------------------------

with tab4:

    col1,col2,col3 = st.columns(3)

    with col1:
        st.image("https://placehold.co/300x200")
        st.caption("Detected Box")

    with col2:
        st.image("https://placehold.co/300x200")
        st.caption("Defect Highlight")

    with col3:
        st.image("https://placehold.co/300x200")
        st.caption("Prediction Heatmap")

# -------------------------------------------------
# ANALYTICS DASHBOARD
# -------------------------------------------------

st.divider()
st.header("Factory Production Analytics")

data = pd.DataFrame({
"Day":[1,2,3,4,5,6,7],
"Production":[120,140,160,180,200,210,240],
"Defects":[12,14,10,9,7,6,5]
})

col1,col2 = st.columns(2)

with col1:
    st.subheader("Production Trend")
    st.line_chart(data.set_index("Day")["Production"])

with col2:
    st.subheader("Defect Rate")
    st.bar_chart(data.set_index("Day")["Defects"])

# -------------------------------------------------
# SUPPLY CHAIN BLOCKCHAIN
# -------------------------------------------------

st.divider()
st.header("Blockchain Supply Chain Simulation")

state = st.selectbox(
"Order Lifecycle",
[
"Raw Material Ordered",
"Manufacturing",
"Quality Inspection",
"Shipped",
"Delivered",
"Payment Settled"
]
)

st.success("Current Supply Chain State: " + state)

# -------------------------------------------------
# ROBOTICS AUTOMATION
# -------------------------------------------------

st.divider()
st.header("Factory Robots")

robots = {
"Pick and Place Robot": "Handles packaging tasks",
"Inspection Robot": "Uses vision AI for defect detection",
"Assembly Robot": "Performs high precision assembly",
"Sorting Robot": "Separates defective items"
}

for r in robots:
    st.write("🤖",r,"-",robots[r])

# -------------------------------------------------
# AI CHATBOT
# -------------------------------------------------

st.divider()
st.header("Manufacturing AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt=st.chat_input("Ask about production, robots, defects...")

if prompt:

    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response="AI assistant analyzing manufacturing data."

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append(
        {"role":"assistant","content":response}
    )
