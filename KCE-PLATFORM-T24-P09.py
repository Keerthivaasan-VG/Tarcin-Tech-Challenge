import json
import os

class KeyValueStore:
    def __init__(self, filename="store.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({}, f)

    def read_store(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print("Error opening file:", e)
            return {}

    def write_store(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def put(self, key, value):
        store = self.read_store()
        store[key] = value
        self.write_store(store)

    def get(self, key, default=None):
        return self.read_store().get(key, default)

    def delete(self, key):
        store = self.read_store()
        if key in store:
            del store[key]
            self.write_store(store)
            return True
        return False

if __name__ == "__main__":
    kv = KeyValueStore("store.json")
    kv.put("name", "AAA")
    kv.put("Age", 20)
    print(kv.get("name"))   # AAA
    print(kv.get("Age"))    # 20
    kv.delete("Age")
    print(kv.get("Age", "Not Found"))
