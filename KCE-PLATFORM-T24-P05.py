def aggregate(records): 
    totals = {}     
    for r in records:         
        name = r["name"]         
        marks = r["marks"]         
        if name in totals: 
            totals[name] += marks         
        else:             
            totals[name] = marks     
    return totals 


def top_n_students(records, n):     
    totals = aggregate(records)     
    sorted_list = sorted(totals.items(), key=lambda x: (-x[1], x[0]))     
    return [name for name, _ in sorted_list[:n]] 


records = [ 
    {"name": "Alice", "marks": 50},     
    {"name": "Bob", "marks": 70}, 
    {"name": "Alice", "marks": 30}, 
    {"name": "Charlie", "marks": 80}, 
] 

totals = aggregate(records) 
top2 = top_n_students(records, 2) 

print("Aggregated Totals:", totals) 
print("Top 2 Students:", top2)
