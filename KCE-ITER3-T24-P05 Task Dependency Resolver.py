def schedule_tasks(file_path):
    tasks = []
    with open(file_path) as f:
        next(f)
        for line in f:
            parts = line.strip().replace('"','').split(",")
            if len(parts) != 3:
                continue
            task_id, duration, priority = parts
            tasks.append({"task_id": task_id, "duration": int(duration), "priority": int(priority)})
    tasks.sort(key=lambda x: x["duration"])
    current_time = 0
    for t in tasks:
        t["start_time"] = current_time
        t["end_time"] = current_time + t["duration"]
        current_time += t["duration"]
    return tasks
for task in schedule_tasks("tasks.csv"):
    print(task)
