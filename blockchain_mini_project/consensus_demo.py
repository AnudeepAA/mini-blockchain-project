# consensus_demo.py
# 🗳️ Simulates PoW, PoS, and DPoS consensus methods
import random

# 🪓 Proof of Work (PoW)
# Selects the miner with the highest computing power
def simulate_pow():
    miners = {
        "Miner1": random.randint(10, 100),
        "Miner2": random.randint(10, 100),
        "Miner3": random.randint(10, 100)
    }
    winner = max(miners, key=miners.get)
    print("[PoW] Miners and power:", miners)
    print("[PoW] Selected Validator:", winner)

# 💰 Proof of Stake (PoS)
# Selects the validator with the highest stake
def simulate_pos():
    stakers = {
        "Validator1": random.randint(10, 100),
        "Validator2": random.randint(10, 100),
        "Validator3": random.randint(10, 100)
    }
    winner = max(stakers, key=stakers.get)
    print("[PoS] Validators and stakes:", stakers)
    print("[PoS] Selected Validator:", winner)

# 🗳️ Delegated Proof of Stake (DPoS)
# Selects top 3 delegates based on most votes (like an election)
def simulate_dpos():
    delegates = ["Alice", "Bob", "Charlie"]
    votes = {
        "Alice": random.randint(0, 100),
        "Bob": random.randint(0, 100),
        "Charlie": random.randint(0, 100)
    }

    # Sort delegates by votes in descending order
    sorted_delegates = sorted(votes.items(), key=lambda x: x[1], reverse=True)

    # Select top 3 (or fewer if not available)
    top_delegates = sorted_delegates[:3]

    print("[DPoS] Votes:", votes)
    print("[DPoS] Selected Top Delegates:", [d[0] for d in top_delegates])

# 🧪 Run all simulations
print("=== Consensus Mechanism Simulation ===\n")
simulate_pow()
print()
simulate_pos()
print()
simulate_dpos()
