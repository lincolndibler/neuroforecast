import streamlit as st
import requests
import json
import os
import base64

# ---- CONFIG ----
st.set_page_config(
    page_title="NeuroForecast",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": "NeuroForecast MMSE Predictor\nBuilt by Lincoln Dibler\nVersion 1.0",
        "Get Help": "https://your-help-link.com",
        "Report a bug": "https://your-bug-report-link.com"
    }
)

# ---- STYLE ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dengxian&display=swap');

html, body, [class*="css"] {
    font-family: 'Dengxian', sans-serif;
    background-color: #f4f8fc;
    color: #212529;
    overflow: hidden;
}
footer {
    position: fixed;
    bottom: 10px;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 12px;
    color: #777;
}
</style>
""", unsafe_allow_html=True)

# ---- SPLASH SCREEN ----
image_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")

query_params = st.query_params
if "entered" in query_params:
    st.session_state.entered = True

if not st.session_state.get("entered", False):
    # Load and encode image as base64
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    # Full-screen splash with overlay click area
    st.markdown(f"""
    <style>
    .splash-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        z-index: 1;
    }}
    .splash-img {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: 1;
    }}
    div[data-testid="stButton"] {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 10;
    }}
    div[data-testid="stButton"] button {{
        width: 100%;
        height: 100%;
        background: transparent;
        border: none;
        cursor: pointer;
    }}
    </style>
    <div class="splash-container">
        <img src="data:image/png;base64,{encoded}" class="splash-img"/>
    </div>
    """, unsafe_allow_html=True)

    # Invisible full-screen button
    if st.button(" "):
        st.session_state.entered = True

    # Add JS for key press or click anywhere to reload with entered=true param
    st.markdown("""
    <script>
    document.addEventListener("keydown", function() {
        fetch(window.location.pathname + "?entered=true").then(() => window.location.reload());
    });
    document.addEventListener("click", function() {
        fetch(window.location.pathname + "?entered=true").then(() => window.location.reload());
    });
    </script>
    """, unsafe_allow_html=True)

    st.markdown("<footer>Lincoln Dibler</footer>", unsafe_allow_html=True)
    st.stop()

# ---- MAIN DASHBOARD UI ----
st.title("NeuroForecast MMSE Predictor")

mode = st.radio("Choose prediction model:", ["Lean MMSE", "Full MMSE"])

raw_input = st.text_area(
    "Paste your input features (JSON format or list of numbers):",
    height=250,
    placeholder='e.g., {"WORD3DL": 1, "MMYEAR": 2024, "MMREPEAT": 2, ...}'
)

if st.button("Run Prediction"):
    try:
        payload = json.loads(raw_input)
        endpoint = (
            "http://18.226.165.205:8000/predict_lean"
            if mode == "Lean MMSE"
            else "http://18.226.165.205:8000/predict_full"
        )
        response = requests.post(endpoint, json=payload)
        st.success(f"Prediction: {response.json()}")
    except Exception as e:
        st.error(f"Input format error: {e}")

# ---- FOOTER ----
st.markdown("<footer>Lincoln Dibler</footer>", unsafe_allow_html=True)
