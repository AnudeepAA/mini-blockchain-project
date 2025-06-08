# mining_simulation.py
# 🔢 Nonce Mining Simulation — Simulate Proof of Work by mining a block that meets a hash condition
import hashlib
import time

# Block class with timestamp, data, nonce and hash attributes
class Block:
    def __init__(self, data):
        self.timestamp = time.time()  # Current time as block creation time
        self.data = data  # Data stored in block
        self.nonce = 0  # Starts at 0, will be incremented until hash meets condition
        self.hash = self.calculate_hash()  # Initial hash

    # SHA-256 hash calculation of block content
    def calculate_hash(self):
        return hashlib.sha256(f"{self.timestamp}{self.data}{self.nonce}".encode()).hexdigest()

    # 🔁 mineBlock() — Finds a hash that starts with required number of zeros (difficulty)
    def mine_block(self, difficulty):
        target = "0" * difficulty  # Example: "0000"
        print(f"Mining block with difficulty {difficulty}...")
        start = time.time()  # Start timer

        # Loop until valid hash is found
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

        end = time.time()  # End timer
        print(f"✅ Block mined!\nNonce: {self.nonce}")
        print(f"Hash: {self.hash}")
        print(f"⏱ Time taken: {end - start:.4f} seconds\n")

# Test mining simulation with difficulty 4 (hash must start with 4 zeros)
block = Block("This is a mined block")
block.mine_block(difficulty=4)  # Can change difficulty to 5, 6 etc. to test effort
