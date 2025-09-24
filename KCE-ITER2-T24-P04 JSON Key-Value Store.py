STORE_FILE = "store.txt"
def load_store():
    store = {}
    try:
        with open(STORE_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if "=" in line:
                    key, value = line.split("=", 1)
                    store[key] = value
    except FileNotFoundError:
        pass
    return store
def save_store(store):
    try:
        with open(STORE_FILE, 'w') as f:
            for key, value in store.items():
                f.write(f"{key}={value}\n")
    except Exception as e:
        print("Error writing file:", e)
def put(key, value):
    store = load_store()
    store[key] = str(value)
    save_store(store)
    print(f"Saved {key} -> {value}")
def get(key):
    store = load_store()
    return store.get(key, None)
def delete(key):
    store = load_store()
    if key in store:
        del store[key]
        save_store(store)
        print(f"Deleted {key}")
    else:
        print(f"{key} not found!")
if __name__ == "__main__":
    put("name", "John Doe")
    put("age", 35)
    print("Get name:", get("name"))
    delete("age")
    print("Get age:", get("age"))
