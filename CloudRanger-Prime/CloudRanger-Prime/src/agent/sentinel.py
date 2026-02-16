import time
import logging
from kubernetes import client, config, watch

# Configure "Hacker Style" Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [SENTINEL] - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("Sentinel")

# 1. Connect to the Cluster (The Body)
try:
    # This automatically finds your Minikube credentials
    config.load_kube_config()
    logger.info("🔌 Connected to CloudRanger Core Systems.")
except Exception as e:
    logger.error(f"❌ Connection Failed: {e}")
    exit(1)

v1 = client.CoreV1Api()

def kill_pod(pod_name, namespace):
    """ The Executioner: Deletes a compromised pod. """
    print(f"\n🚨 THREAT DETECTED: {pod_name}")
    print(f"⚔️  INITIATING TERMINATION PROTOCOL...")
    
    try:
        v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
        print(f"✅ TARGET NEUTRALIZED: {pod_name} deleted.")
        print(f"🔄 Auto-Healing sequence active (New pod starting)...\n")
    except Exception as e:
        logger.error(f"❌ FAILED TO NEUTRALIZE: {e}")

def monitor_logs():
    """ The Watcher: Tails logs in real-time. """
    print("🔭 Sentinel Agent is scanning financial streams...")
    
    w = watch.Watch()
    
    # Watch ALL pods with the label 'run=financial-ledger'
    for event in w.stream(v1.list_pod_for_all_namespaces, label_selector="run=financial-ledger"):
        pod = event['object']
        pod_name = pod.metadata.name
        namespace = pod.metadata.namespace
        
        # Only watch running pods
        if pod.status.phase == "Running":
            try:
                # Read the very last line of logs
                logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace, tail_lines=1)
                
                if "POISON DATA" in logs:
                    kill_pod(pod_name, namespace)
                elif "VALID" in logs:
                    # Print a dot for every valid transaction (Heartbeat)
                    print(f"[{pod_name}] Verified Hash...", end='\r')
                    
            except Exception:
                pass # Pod might be starting/dying, ignore temporary errors

if __name__ == "__main__":
    print("""
    =============================================
       CLOUDRANGER PRIME: SENTINEL ONLINE
    =============================================
    """)
    monitor_logs()
