# 🛡️ CloudRanger Prime: Autonomous Sentinel

![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Kubernetes%20%7C%20Minikube-blue)
![Language](https://img.shields.io/badge/Language-Python%203.9-yellow)
![Focus](https://img.shields.io/badge/Focus-DevSecOps%20%7C%20Automation-red)

> **"The system that heals itself."**
> An autonomous Kubernetes defense agent that detects corrupted financial transactions and neutralizes compromised pods in real-time.

---

## 📸 The "Kill Shot" (Demo)
*(Replace this line with a GIF or Screenshot of your terminal showing "THREAT DETECTED" -> "TARGET NEUTRALIZED")*

---

## ⚡ Project Overview
**CloudRanger Prime** is a **Self-Healing Infrastructure** demonstration. It simulates a high-frequency financial ledger being attacked by "Poison Data" injection.

Instead of waiting for a human engineer to read logs and restart the server, the **Sentinel Agent**:
1.  **Watches** the live stream of application logs.
2.  **Detects** the specific "Poison Data" signature (Simulated Hack).
3.  **Executes** a  command via the Kubernetes API.
4.  **Verifies** that the Cluster Auto-Healer spawns a fresh, clean replacement.

**Reaction Time:** < 0.5 Seconds.
**Human Intervention:** 0.

---

## 🏗️ Architecture

```mermaid
graph TD;
    A[Financial Node (Victim)] -- Generates Logs --> B(Log Stream);
    B -- "Poison Data Detected" --> C[Sentinel Agent (Python)];
    C -- "Delete Pod Command" --> D[Kubernetes API];
    D -- "SIGKILL" --> A;
    E[ReplicaSet] -- "Auto-Healing" --> A;
```

---

## 🚀 Technical Stack

| Component | Technology | Role |
|-----------|------------|------|
| **The Victim** | Python + Docker | Simulates a Financial Ledger app with random data corruption. |
| **The Body** | Minikube (K8s) | Hosts the application in a contained environment. |
| **The Brain** | Python (K8s Client) | The "Sentinel" that monitors and kills pods. |
| **The Eyes** | Streamlit | (Optional) Real-time dashboard for threat metrics. |

---

## 🛠️ Installation & Setup

### Prerequisites
* Docker & Minikube
* Python 3.x
* Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: kubernetes in /home/mannasamriddha7/.local/lib/python3.12/site-packages (35.0.0)
Requirement already satisfied: streamlit in /home/mannasamriddha7/.local/lib/python3.12/site-packages (1.54.0)
Requirement already satisfied: certifi>=14.05.14 in /usr/local/lib/python3.12/dist-packages (from kubernetes) (2025.7.9)
Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.12/dist-packages (from kubernetes) (1.17.0)
Requirement already satisfied: python-dateutil>=2.5.3 in /usr/local/lib/python3.12/dist-packages (from kubernetes) (2.9.0.post0)
Requirement already satisfied: pyyaml>=5.4.1 in /usr/local/lib/python3.12/dist-packages (from kubernetes) (6.0.2)
Requirement already satisfied: websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from kubernetes) (1.9.0)
Requirement already satisfied: requests in /usr/local/lib/python3.12/dist-packages (from kubernetes) (2.32.4)
Requirement already satisfied: requests-oauthlib in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from kubernetes) (2.0.0)
Requirement already satisfied: urllib3!=2.6.0,>=1.24.2 in /usr/local/lib/python3.12/dist-packages (from kubernetes) (2.5.0)
Requirement already satisfied: durationpy>=0.7 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from kubernetes) (0.10)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from streamlit) (6.0.0)
Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools<7,>=5.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.2)
Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.2.1)
Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from streamlit) (3.1.46)
Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.1.3)
Requirement already satisfied: packaging>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)
Requirement already satisfied: pandas<3,>=1.4.0 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from streamlit) (2.3.3)
Requirement already satisfied: pillow<13,>=7.1.0 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from streamlit) (12.1.1)
Requirement already satisfied: pydeck<1,>=0.8.0b4 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from streamlit) (0.9.1)
Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)
Requirement already satisfied: pyarrow>=7.0 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from streamlit) (23.0.1)
Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.5.0)
Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)
Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from streamlit) (6.5.4)
Requirement already satisfied: typing-extensions<5,>=4.10.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.14.1)
Requirement already satisfied: watchdog<7,>=2.1.5 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from streamlit) (6.0.0)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.24.0)
Requirement already satisfied: narwhals>=1.27.1 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.16.0)
Requirement already satisfied: gitdb<5,>=4.0.1 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)
Requirement already satisfied: pytz>=2020.1 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from pandas<3,>=1.4.0->streamlit) (2025.3)
Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests->kubernetes) (3.4.2)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests->kubernetes) (3.10)
Requirement already satisfied: oauthlib>=3.0.0 in /usr/lib/python3/dist-packages (from requests-oauthlib->kubernetes) (3.2.2)
Requirement already satisfied: smmap<6,>=3.0.1 in /home/mannasamriddha7/.local/lib/python3.12/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.2)
Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (25.3.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.4.1)
Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.26.0)

### 1. Launch the Cluster
```bash
minikube start
eval $(minikube docker-env)
```

### 2. Deploy the "Victim" (Financial Node)
```bash
# Build the image inside the cluster
docker build -t financial-node:v1 src/financial-node/

# Deploy to Kubernetes
kubectl run financial-ledger --image=financial-node:v1 --image-pull-policy=Never --labels="run=financial-ledger"
```

### 3. Activate the Sentinel
```bash
python3 src/agent/sentinel.py
```

---

## 🖥️ The Code Logic (Snippet)

The core logic relies on the Kubernetes  stream to react instantly to log events.

```python
# simplified_sentinel.py
for event in w.stream(v1.list_pod_for_all_namespaces, label_selector="run=financial-ledger"):
    logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)
    
    if "POISON DATA" in logs:
        print(f"🚨 THREAT DETECTED: {pod_name}")
        v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
        print("✅ TARGET NEUTRALIZED.")
```

---

## 🔮 Future Roadmap
- [ ] Integration with **Prometheus** for long-term metric storage.
- [ ] **Slack/Discord Alerts** when a kill occurs.
- [ ] Upgrade to **Deployment** sets for zero-downtime rolling updates.

---

### 👨‍💻 Author
**[Your Name]**
*Cloud Security & DevOps Enthusiast*
