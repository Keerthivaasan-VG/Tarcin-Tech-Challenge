import csv
TITLE = "Load Distributor"
DESCRIPTION = "Reads jobs.csv and distributes jobs across nodes to balance load."
def read_jobs(file_path):
    jobs = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            jobs.append({"JobID": row["JobID"], "Size": int(row["Size"])})
    return jobs
def distribute_jobs(jobs, num_nodes):
    
    nodes = [{"Node": i+1, "Jobs": [], "Load": 0} for i in range(num_nodes)]

    
    for job in jobs:
        target = min(nodes, key=lambda n: n["Load"])
        target["Jobs"].append(job)
        target["Load"] += job["Size"]

    return nodes
def main():
    print("=== " + TITLE + " ===")
    print(DESCRIPTION)
    print()

    file_path = input("Enter CSV file path (e.g., jobs.csv): ")
    num_nodes = int(input("Enter number of nodes: "))

    jobs = read_jobs(file_path)
    nodes = distribute_jobs(jobs, num_nodes)

    print("\n--- Distribution Result ---")
    for node in nodes:
        print(f"Node {node['Node']} (Total Load={node['Load']}): {[job['JobID'] for job in node['Jobs']]}")
if __name__ == "__main__":
    main()
output
