def summarize_logs(file_path):
    counts = {}  
    with open(file_path) as f:
        for line in f:
            parts = line.strip().split(maxsplit=2)  
            if len(parts) < 2:
                continue
            level = parts[1]
            counts[level] = counts.get(level, 0) + 1
    return counts
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    with open("logs.txt", "w") as f:
        f.write("2025-09-24 INFO Started process\n")
        f.write("2025-09-24 WARN Low memory\n")
        f.write("2025-09-24 ERROR Failed task\n")
        f.write("2025-09-24 INFO Process running\n")
        f.write("2025-09-24 WARN Disk space low\n")
    summary = summarize_logs("logs.txt")
    print("Log counts by level:", summary)
    levels = list(summary.keys())
    counts = list(summary.values())
    plt.bar(levels, counts, color=['green','orange','red'])
    plt.xlabel("Log Level")
    plt.ylabel("Count")
    plt.title("Log Summary")
    plt.show()
