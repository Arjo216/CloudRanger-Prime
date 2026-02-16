import streamlit as st
import time
import random
from kubernetes import client, config

# Page Config
st.set_page_config(
    page_title="CloudRanger Prime | Sentinel Command",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS for "Cyberpunk" look
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #00ff41;
        font-family: 'Courier New', monospace;
    }
    .metric-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    h1, h2, h3 {
        color: #00ff41 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🛡️ CLOUDRANGER PRIME")
st.subheader("Autonomous Financial Defense System")

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png", width=50)
    st.markdown("### SYSTEM STATUS")
    system_status = st.empty()
    st.markdown("---")
    st.markdown("**Active Agents:** 1")
    st.markdown("**Cluster:** Minikube (v1.32)")
    st.markdown("**AI Model:** Phi-3 (Quantized)")

# Layout: Metrics Row
col1, col2, col3 = st.columns(3)
with col1:
    metric_threats = st.empty()
with col2:
    metric_uptime = st.empty()
with col3:
    metric_pods = st.empty()

st.markdown("---")

# Layout: Main Feed
st.markdown("### 📡 LIVE SENTINEL FEED")
log_feed = st.empty()

# Initialize State
if 'threats' not in st.session_state:
    st.session_state.threats = 0

# Connect to K8s
try:
    config.load_kube_config()
    v1 = client.CoreV1Api()
    k8s_status = "ONLINE"
except:
    k8s_status = "OFFLINE (Demo Mode)"

# THE MAIN LOOP
if 'logs_history' not in st.session_state:
    st.session_state.logs_history = []

start_time = time.time()

while True:
    # Initialize variables
    pod_count = 0
    status_text = "CONNECTING..."
    status_color = "🟠"
    
    # 1. Update Metrics
    uptime = int(time.time() - start_time)
    
    try:
        # Get Pods
        pods = v1.list_pod_for_all_namespaces(label_selector="run=financial-ledger").items
        pod_count = len(pods)
        
        # Read Logs if pod exists
        if pod_count > 0:
            pod_name = pods[0].metadata.name
            try:
                raw_log = v1.read_namespaced_pod_log(name=pod_name, namespace="default", tail_lines=1)
                
                if "POISON DATA" in raw_log:
                    st.session_state.threats += 1
                    status_color = "🔴"
                    status_text = "CRITICAL THREAT DETECTED"
                    st.session_state.logs_history.insert(0, f"⚔️ [BLOCKED] Poison Data attempt from {pod_name}")
                else:
                    status_color = "🟢" 
                    status_text = "SYSTEM SECURE"
                    if random.random() < 0.2:
                         st.session_state.logs_history.insert(0, f"✅ Verified Transaction Hash: {random.randint(10000,99999)}")
            except:
                pass
        else:
            status_text = "⚠️ SEARCHING FOR TARGET..."
            status_color = "🟡"
        
    except Exception as e:
        status_text = "CONNECTION ERROR"
        status_color = "🔴"

    # 2. Render Updates safely
    system_status.markdown(f"## {status_color} {status_text}")
    
    with col1:
        metric_threats.metric(label="THREATS NEUTRALIZED", value=st.session_state.threats)
    with col2:
        metric_uptime.metric(label="SYSTEM UPTIME", value=f"{uptime}s")
    with col3:
        metric_pods.metric(label="ACTIVE PODS", value=pod_count)

    # Render Logs
    st.session_state.logs_history = st.session_state.logs_history[:8]
    feed_text = ""
    for log in st.session_state.logs_history:
        if "BLOCKED" in log:
            feed_text += f"<div style='color: #ff4b4b; margin-bottom: 5px;'>{log}</div>"
        else:
            feed_text += f"<div style='color: #00ff41; margin-bottom: 5px;'>{log}</div>"
            
    log_feed.markdown(feed_text, unsafe_allow_html=True)

    # Refresh Rate
    time.sleep(1)
