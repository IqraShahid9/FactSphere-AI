import json
import os

MEMORY_FILE = "memory/long_term_memory.json"

def save_memory(query, summary):
    os.makedirs("memory", exist_ok=True)
    try:
        with open(MEMORY_FILE, "r") as f:
            mem = json.load(f)
    except:
        mem = {}
    mem[query] = summary
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}
