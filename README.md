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
  "MMYEAR": 2024,
  "WORD3DL": 1,
  "MMREPEAT": 2,
  "VISSPATIAL": 1,
  "RECALL": 0,
  "ORIENT": 5
}
