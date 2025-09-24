import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
def aggregate_events(file_path):
    agg = defaultdict(lambda: defaultdict(int))  # type -> hour -> count
    with open(file_path) as f:
        next(f)  # skip header
        for line in f:
            timestamp, type_ = line.strip().split(",")
            hour = datetime.fromisoformat(timestamp).hour
            agg[type_][hour] += 1
    return agg
agg = aggregate_events("events.csv")
print(agg)
for type_, hours in agg.items():
    hours_sorted = sorted(hours.items())
    x, y = zip(*hours_sorted)
    plt.plot(x, y, label=type_)
plt.xlabel("Hour")
plt.ylabel("Event Count")
plt.title("Events by Type per Hour")
plt.legend()
plt.show()
