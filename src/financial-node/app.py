import time
import random
import logging

# Configure Logging (Standard Format)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("AEGIS-Node")

def generate_transaction():
    tx_id = random.randint(1000, 9999)
    
    # INCREASED HACK CHANCE (30%) - Better for demos
    if random.random() < 0.30:
        logger.error(f"CRITICAL: POISON DATA DETECTED IN BLOCK {tx_id}. INTEGRITY COMPROMISED.")
    else:
        logger.info(f"Block {tx_id}: Hash VALID")

if __name__ == "__main__":
    print("Starting Financial Ledger Node...")
    while True:
        generate_transaction()
        # Keep the readable 2-second delay
        time.sleep(2)
