README.md
# 🛡️ CloudRanger Prime: Autonomous Sentinel

![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge&logo=kubernetes)
![Platform](https://img.shields.io/badge/Platform-Kubernetes%20%7C%20Minikube-blue?style=for-the-badge&logo=linux)
![Language](https://img.shields.io/badge/Language-Python%203.9-yellow?style=for-the-badge&logo=python)
![Focus](https://img.shields.io/badge/Focus-DevSecOps%20%7C%20Automation-red?style=for-the-badge&logo=security-scorecard)

> **"The system that heals itself."**
>
> An autonomous Kubernetes defense agent that detects corrupted financial transactions and neutralizes compromised pods in real-time (< 0.5s reaction time).

---

## 📸 The "Kill Shot" (Demo)
*(Terminal showing "THREAT DETECTED" -> "TARGET NEUTRALIZED")*

---

## ⚡ Project Overview
**CloudRanger Prime** is a **Self-Healing Infrastructure** demonstration. It simulates a high-frequency financial ledger being attacked by "Poison Data" injection.

Instead of waiting for a human engineer to read logs and restart the server, the **Sentinel Agent**:
1.  **Watches** the live stream of application logs.
2.  **Detects** the specific "Poison Data" signature (Simulated Hack).
3.  **Executes** a `SIGKILL` command via the Kubernetes API.
4.  **Verifies** that the Cluster Auto-Healer spawns a fresh, clean replacement.

**Reaction Time:** < 0.5 Seconds.
**Human Intervention:** 0.

---

## 🏗️ Architecture

\`\`\`mermaid
graph TD;
    A[Financial Node (Victim)] -- Generates Logs --> B(Log Stream);
    B -- "Poison Data Detected" --> C[Sentinel Agent (Python)];
    C -- "Delete Pod Command" --> D[Kubernetes API];
    D -- "SIGKILL" --> A;
    E[ReplicaSet] -- "Auto-Healing" --> A;
\`\`\`

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
* `pip install kubernetes streamlit`

### 1. Launch the Cluster
\`\`\`bash
minikube start
eval \$(minikube docker-env)
\`\`\`

### 2. Deploy the "Victim" (Financial Node)
\`\`\`bash
# Build the image inside the cluster
docker build -t financial-node:v1 src/financial-node/

# Deploy to Kubernetes
kubectl run financial-ledger --image=financial-node:v1 --image-pull-policy=Never --labels="run=financial-ledger"
\`\`\`

### 3. Activate the Sentinel
\`\`\`bash
python3 src/agent/sentinel.py
\`\`\`

---

## 🖥️ The Code Logic (Snippet)

The core logic relies on the Kubernetes `watch` stream to react instantly to log events.

\`\`\`python
# simplified_sentinel.py
for event in w.stream(v1.list_pod_for_all_namespaces, label_selector="run=financial-ledger"):
    logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)
    
    if "POISON DATA" in logs:
        print(f"🚨 THREAT DETECTED: {pod_name}")
        v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
        print("✅ TARGET NEUTRALIZED.")
\`\`\`

---

## 🔮 Future Roadmap
- [ ] Integration with **Prometheus** for long-term metric storage.
- [ ] **Slack/Discord Alerts** when a kill occurs.
- [ ] Upgrade to **Deployment** sets for zero-downtime rolling updates.

---

### 👨‍💻 Author
**[Arjo216]**
*Cloud Security & DevOps Enthusiast*
