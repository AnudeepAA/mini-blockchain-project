# blockchain_simulation.py
# Simulates a simple blockchain with 3 linked blocks and shows effect of tampering
import hashlib
import time

# Block class with required attributes: index, timestamp, data, previousHash, hash, nonce
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index  # Position in the chain
        self.timestamp = timestamp  # Time of block creation
        self.data = data  # Transaction or data stored in block
        self.previous_hash = previous_hash  # Link to previous block
        self.nonce = 0  # Number used to find correct hash
        self.hash = self.calculate_hash()  # Unique block hash

    # Generates SHA-256 hash using block data
    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Returns block info for display
    def __str__(self):
        return (f"Index: {self.index}\nTimestamp: {self.timestamp}\nData: {self.data}\n"
                f"Previous Hash: {self.previous_hash}\nNonce: {self.nonce}\nHash: {self.hash}\n")

# Create genesis block (first block)
blockchain = [Block(0, time.time(), "Genesis Block", "0")]

# Create and link 2 more blocks
for i in range(1, 3):
    prev_block = blockchain[-1]
    new_block = Block(i, time.time(), f"Block {i} Data", prev_block.hash)
    blockchain.append(new_block)

# Display original blockchain
print("\n=== Blockchain ===")
for block in blockchain:
    print(block)

# 🔄 Challenge: Tampering Block 1 and observing effect
print("\n--- Tampering Block 1 ---")
blockchain[1].data = "Tampered Data"  # Change block 1's data
blockchain[1].hash = blockchain[1].calculate_hash()  # Recalculate hash of tampered block

# Recalculate following blocks to maintain chain integrity
for i in range(2, len(blockchain)):
    blockchain[i].previous_hash = blockchain[i - 1].hash
    blockchain[i].hash = blockchain[i].calculate_hash()

# Display modified chain showing effect of tampering
print("\n=== Modified Blockchain ===")
for block in blockchain:
    print(block)
