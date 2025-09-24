def filter_records(records, rule):
    filtered = []
    # Split rule by 'and'
    conditions = [r.strip() for r in rule.split("and")]
    
    for record in records:
        match = True
        for cond in conditions:
            if ">=" in cond:
                key, value = cond.split(">=")
                if int(record[key.strip()]) < int(value.strip()):
                    match = False
            elif ">" in cond:
                key, value = cond.split(">")
                if int(record[key.strip()]) <= int(value.strip()):
                    match = False
            elif "<=" in cond:
                key, value = cond.split("<=")
                if int(record[key.strip()]) > int(value.strip()):
                    match = False
            elif "<" in cond:
                key, value = cond.split("<")
                if int(record[key.strip()]) >= int(value.strip()):
                    match = False
            elif "==" in cond:
                key, value = cond.split("==")
                if str(record[key.strip()]) != value.strip():
                    match = False
            elif "!=" in cond:
                key, value = cond.split("!=")
                if str(record[key.strip()]) == value.strip():
                    match = False
        if match:
            filtered.append(record)
    return filtered


# Test data
records = [
    {"name": "Alice", "age": 20, "score": 55},
    {"name": "Bob", "age": 17, "score": 60},
    {"name": "Charlie"
