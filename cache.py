import json
import os
import time

CACHE_FILE = "cache.json"
CACHE_EXPIRY = 600  # 10 minutes in seconds

def get_cached(city):
    if not os.path.exists(CACHE_FILE):
        return None

    with open(CACHE_FILE) as f:
        cache = json.load(f)

    entry = cache.get(city.lower())

    if entry and time.time() - entry["timestamp"] < CACHE_EXPIRY:
        print("⚡  Loaded from cache (saved API call!)")
        return entry["data"]

    return None  # cache is stale or missing

def save_cache(city, data):
    cache = {}

    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            cache = json.load(f)

    cache[city.lower()] = {
        "data": data,
        "timestamp": time.time()
    }

    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)