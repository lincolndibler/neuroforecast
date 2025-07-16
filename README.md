# 🧠 NeuroForecast

NeuroForecast is a Python-based MMSE (Mini-Mental State Examination) predictor built with a user-facing UI using **Streamlit**, and deployed via **AWS EC2**. It supports both lean and full prediction models, with FastAPI integration for flexible back-end architecture.

---

## ⚙️ Features

- MMSE score prediction from structured input
- Lean and full model modes
- Streamlit UI interface (dashboard + splash screen)
- Deployed and tested on AWS EC2

---

## 🚀 Getting Started

Clone the repo and set up dependencies:

```bash
git clone https://github.com/lincolndibler/neuroforecast.git
cd neuroforecast
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧾 Sample Input

{
  "WORD3DL": 1,
  "MMYEAR": 2025,
  "MMREPEAT": 2,
  "MMMONTH": 7,
  "MMDATE": 16,
  "MMAREA": 1,
  "MMHOSPIT": 1,
  "MMDAY": 3,
  "WORD2DL": 1,
  "WORD1DL": 0,
  "MMFLOOR": 2,
  "MMSEASON": 3,
  "MMDRAW": 1
}

## 🎬 Demo Walkthrough
📹 [Download neuroforecastTutorial.mp4](https://github.com/lincolndibler/neuroforecast/blob/master/demo/neuroforecastTutorial.mp4)
