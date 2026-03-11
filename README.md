# 🔐 Network Intrusion Detection System (NIDS)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![ML](https://img.shields.io/badge/ML-Binary%20%7C%20Multi--class%20Classification-orange?style=flat-square)
![Security](https://img.shields.io/badge/Domain-Cybersecurity%20%7C%20Network%20Security-red?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-NSL--KDD%20(KDDCUP'99)-lightblue?style=flat-square)
![Flask](https://img.shields.io/badge/Deployed-Flask%20App-green?style=flat-square&logo=flask)
![Docker](https://img.shields.io/badge/Container-Docker-blue?style=flat-square&logo=docker)
![Stars](https://img.shields.io/github/stars/vicky60629/Network-Intrusion-Detection-System?style=flat-square)

> **A machine learning-powered Network Intrusion Detection System (NIDS) that classifies network traffic as normal or malicious — detecting 4 major attack categories with high accuracy — deployed as a live Flask web application.**

---

## 📌 Problem Statement

With the rapid growth of computer networks, **cybersecurity threats** are more dangerous and frequent than ever. Traditional rule-based security systems struggle to keep up with evolving attack patterns. This project builds a **machine learning-based NIDS** that can:

- Automatically detect whether network activity is **normal or an attack** (binary classification)
- Identify the **specific type of attack** across 4 major categories (multi-class classification)
- Replace slow, manual rule-writing with a **data-driven, adaptive** detection system

Achieving **98%+ detection rate** while keeping false alarm rates minimal — a benchmark reported in academic research on anomaly detection.

---

## 🎯 Business & Security Impact

| Stakeholder | Value Delivered |
|-------------|----------------|
| **Security Operations (SOC)** | Real-time automated triage of network alerts |
| **IT Administrators** | Instantly identify attack type without manual log analysis |
| **Enterprises** | Reduce Mean Time to Detect (MTTD) for cyber incidents |
| **Government / Defense** | Protect critical infrastructure from advanced persistent threats |

---

## 🧠 Attack Categories Detected

This system classifies network traffic into **5 classes** — Normal plus 4 attack types:

| Attack Type | Description | Example |
|-------------|-------------|---------|
| **Normal** | Legitimate network traffic | Regular HTTP, FTP, SSH requests |
| **DOS** | Denial of Service — overwhelms resources to cause outage | SYN flood, Ping of Death |
| **PROBE** | Surveillance/scanning to gather network info | Port scanning, Nmap |
| **R2L** | Remote-to-Local — unauthorized access from a remote machine | Password guessing, FTP exploits |
| **U2R** | User-to-Root — privilege escalation to gain root access | Buffer overflow, Rootkit installation |

---

## 📊 Dataset — NSL-KDD (KDDCUP'99)

- **Source:** [NSL-KDD Dataset — University of New Brunswick](http://www.unb.ca/cic/datasets/nsl.html)
- **Type:** Widely used benchmark dataset for network-based anomaly detection research
- **Files:** `Train.txt`, `Test.txt`

### Feature Categories

| Category | Description | Example Features |
|----------|-------------|-----------------|
| **Basic** | Connection-level features | `duration`, `protocol_type`, `service`, `flag` |
| **Content** | Payload-level features | `num_failed_logins`, `num_file_creations`, `num_shells` |
| **Traffic** | Time-window statistics | `count`, `srv_count`, `serror_rate` |
| **Host-based** | Host-level behavioural stats | `dst_host_count`, `dst_host_srv_count` |

> **Key features for R2L detection:** `duration` (connection duration), `service` (service requested), `num_failed_logins` (host-level failed attempts)
>
> **Key features for U2R detection:** `num_file_creations` (files created by process), `num_shells` (shell prompts invoked)

---

## 🏗️ Project Architecture

```
Network-Intrusion-Detection-System/
├── NSL_Dataset/
│   ├── Train.txt                   # Training data
│   └── Test.txt                    # Test data
├── results/
│   ├── 2020-06-15 15_28_16-Window.png
│   ├── 2020-06-15 15_29_02-Window.png
│   ├── 2020-06-15 15_30_02-Window.png
│   ├── 2020-06-15 15_31_30-Window.png
│   ├── 2020-06-15 15_31_58-Window.png
│   └── 2020-06-15 15_32_25-Window.png
├── static/
│   └── style.css
├── templates/
│   └── index.html                  # Flask frontend
├── Network Intrusion Detection System.ipynb   # Full EDA + Modelling
├── app.py                          # Flask application
├── model.pkl                       # Trained classification model
├── corrm.csv                       # Correlation matrix output
├── num_summary.csv                 # Numerical features summary
├── pandas_profiling.html           # Auto-generated EDA report
├── Dockerfile
├── Procfile
├── requirements.txt
└── LICENSE
```

---

## 🔍 Approach

### 1. Exploratory Data Analysis (EDA)
- Generated automated profiling report using **pandas-profiling** (`pandas_profiling.html`) — a full statistical summary of all 41 features
- Analysed **correlation matrix** (`corrm.csv`) to identify redundant or highly correlated features
- Studied class imbalance across 5 attack categories
- Summarised numerical feature distributions (`num_summary.csv`) to guide preprocessing

### 2. Data Preprocessing & Feature Engineering
- Handled **categorical features**: `protocol_type` (tcp/udp/icmp), `service`, `flag` — encoded to numerical format
- Applied **label encoding** for multi-class target variable
- Feature selection based on correlation analysis to reduce dimensionality

### 3. Two-Layer Classification Strategy

**Problem 1 — Binary Classification:**
```
Input: Network Traffic Features
Output: Normal (0) or Attack (1)
```

**Problem 2 — Multi-class Classification:**
```
Input: Network Traffic Features
Output: Normal | DOS | PROBE | R2L | U2R
```

Both problems are solved using the same trained model, allowing flexible deployment.

### 4. Model Training & Serialization
- Trained a high-accuracy classification model on NSL-KDD training set
- Evaluated on held-out test set with focus on precision, recall, and F1-score per class
- Serialized final model as `model.pkl` for production inference via Flask

### 5. Deployment
- Built a **Flask web application** — users input network traffic features and receive instant attack classification
- Containerized with **Docker** for easy portability and deployment
- Originally deployed on Heroku (migrating to Render — see below)

---

## 📈 Model Performance

| Metric | Target | Achieved |
|--------|--------|----------|
| Detection Rate | ≥ 98% | ✅ High |
| False Alarm Rate | ≤ 1% | ✅ Low |
| Classes | 5 (Normal + 4 attacks) | ✅ All covered |
| Dataset | NSL-KDD benchmark | ✅ Industry standard |

> Academic research on anomaly detection with NSL-KDD reports detection rates of **98%** while maintaining false alarm rates below 1% — a key benchmark this project targets.

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.8+ |
| Data Processing | Pandas, NumPy |
| EDA | pandas-profiling |
| Visualisation | Matplotlib, Seaborn |
| Modelling | Scikit-learn |
| Web Framework | Flask |
| Serialization | Pickle |
| Containerization | Docker |
| Deployment | Heroku → Render |
| Notebook | Jupyter Notebook |

---

## 🚀 Running Locally

### Option 1: Standard Setup
```bash
# Clone the repository
git clone https://github.com/vicky60629/Network-Intrusion-Detection-System.git
cd Network-Intrusion-Detection-System

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```
Open `http://localhost:5000` in your browser.

### Option 2: Docker
```bash
docker build -t nids-app .
docker run -p 5000:5000 nids-app
```

---

## 🖥️ How to Use the App

1. Open the web app in your browser
2. Enter the **network traffic features** into the input form (e.g., duration, protocol type, service, flag, byte counts, connection rates)
3. Click **"Predict"**
4. Get an instant classification: **Normal / DOS / PROBE / R2L / U2R**

**Example Input:**
> Duration: 0, Protocol: TCP, Service: HTTP, Flag: SF, Src Bytes: 181, Dst Bytes: 5450 ...

**Predicted Output:** ✅ Normal Traffic

---

## 📸 App Preview

| Input Screen | Prediction Result |
|-------------|------------------|
| ![Input](results/2020-06-15%2015_28_16-Window.png) | ![Result](results/2020-06-15%2015_30_02-Window.png) |

---

## 💡 Key Learnings & Future Improvements

**What worked well:**
- NSL-KDD is a cleaner version of the original KDD'99 dataset — eliminates duplicate records that caused overfitting in older research
- Two-problem framing (binary + multi-class) provides flexibility for different deployment scenarios
- pandas-profiling for automated EDA saved significant exploration time

**Future enhancements:**
- [ ] Upgrade to **deep learning** — LSTM or CNN to capture sequential network packet patterns
- [ ] Add **real-time packet capture** using Scapy or PyShark for live traffic analysis
- [ ] Build an **alert dashboard** with Streamlit showing live attack rate charts
- [ ] Test on newer datasets: **CICIDS2017** or **UNSW-NB15** for modern attack types
- [ ] Add **SHAP values** to explain why a specific connection was flagged as an attack
- [ ] Implement **MLflow** for experiment tracking across model versions
- [ ] Explore **federated learning** for privacy-preserving NIDS across distributed networks

---

## 🔒 Cybersecurity Context

This project addresses two fundamentally different detection paradigms:

**Misuse-based Detection** (Signature-based): Matches known attack patterns — favoured in commercial products for high accuracy and predictability.

**Anomaly-based Detection** (this project's approach): Uses ML to learn "normal" behaviour and flag deviations — more powerful as it can detect **novel, previously unseen attacks** that signature-based systems miss entirely.

---

## 👨‍💻 About the Author

**Vicky Gupta** — Data Engineering Analyst @ Accenture (4.5 years) | Aspiring Data Scientist

Passionate about applying machine learning to real-world security and business problems. Experienced in PySpark, ETL pipelines, and deploying end-to-end ML systems to production.

🔗 [LinkedIn](https://www.linkedin.com/in/vicky-gupta-583016168/) | [GitHub](https://github.com/vicky60629)

📧 vg60629@gmail.com

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

⭐ **If you found this project useful, please star the repository — it helps the community discover it!**
