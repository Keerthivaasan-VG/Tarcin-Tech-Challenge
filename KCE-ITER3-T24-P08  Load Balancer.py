def optimize_resources(file_path, budget):
    resources = []
    with open(file_path) as f:
        next(f)
        for line in f:
            rid, cost, value = line.strip().split(",")
            resources.append({
                "id": rid.strip(),
                "cost": float(cost),
                "value": float(value)
            })
   
    resources.sort(key=lambda x: x["value"]/x["cost"], reverse=True)
   
    selected = []
    total_cost = 0
   
    for r in resources:
        if total_cost + r["cost"] <= budget:
            selected.append(r)
            total_cost += r["cost"]
   
    return selected
if __name__ == "__main__":
   
    optimized = optimize_resources("resources.csv", budget=50)
    for r in optimized:
        print(r)
