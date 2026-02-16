import time
import logging
from kubernetes import client, config

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [SENTINEL] - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("Sentinel")

# 1. Connect to the Cluster
try:
    config.load_kube_config()
    logger.info("🔌 Connected to CloudRanger Core Systems.")
except Exception as e:
    logger.error(f"❌ Connection Failed: {e}")
    exit(1)

v1 = client.CoreV1Api()

def kill_pod(pod_name, namespace):
    """ The Executioner """
    print(f"\n🚨 THREAT DETECTED: {pod_name}")
    print(f"⚔️  INITIATING TERMINATION PROTOCOL...")
    try:
        v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
        print(f"✅ TARGET NEUTRALIZED: {pod_name} deleted.")
        print(f"🔄 Auto-Healing sequence active...\n")
    except Exception as e:
        logger.error(f"❌ FAILED TO NEUTRALIZE: {e}")

def monitor_logs():
    """ The Watcher: Polls logs every 2 seconds """
    print("🔭 Sentinel Agent is scanning financial streams...")
    
    while True:
        try:
            # Get all pods with the tag 'financial-ledger'
            pods = v1.list_pod_for_all_namespaces(label_selector="run=financial-ledger").items
            
            if not pods:
                print("⚠️  No Financial Node found. Waiting...", end='\r')
            
            for pod in pods:
                pod_name = pod.metadata.name
                namespace = pod.metadata.namespace
                
                if pod.status.phase == "Running":
                    try:
                        # Read the last line of logs
                        logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace, tail_lines=1)
                        
                        if "POISON DATA" in logs:
                            kill_pod(pod_name, namespace)
                            # Break loop to let K8s recover
                            time.sleep(5) 
                        elif "VALID" in logs:
                            # Print a live heartbeat
                            print(f"[{pod_name}] Verified Hash... {logs.strip()[-10:]}", end='\r')
                            
                    except Exception:
                        pass # Ignore temporary read errors
            
            # Wait 1 second before checking again
            time.sleep(1)
            
        except KeyboardInterrupt:
            print("\n🛑 Sentinel Deactivated.")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

if __name__ == "__main__":
    print("""
    =============================================
       CLOUDRANGER PRIME: SENTINEL V2 (ACTIVE)
    =============================================
    """)
    monitor_logs()
