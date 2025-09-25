def merge_projects(records):
    project_scores = dict()
    for rec in records:
        team = rec[0].strip()
        project = rec[1].strip()
        score = float(rec[2])  # convert to number
        key = (team, project)
        if key not in project_scores:
            project_scores[key] = [0, 0]  # [sum, count]
        project_scores[key][0] += score
        project_scores[key][1] += 1

    # Calculate averages
    averages = dict()
    for key, value in project_scores.items():
        averages[key] = value[0] / value[1]
    return averages


def best_project(records, team_name):
    averages = merge_projects(records)
    best_proj = None
    best_score = -1
    for (team, project), avg in averages.items():
        if team == team_name and avg > best_score:
            best_proj = project
            best_score = avg
    return best_proj, best_score


# Example records
records = [
    ("TeamA", "Proj1", 80),
    ("TeamA", "Proj1", 90),
    ("TeamA", "Proj2", 70),
    ("TeamB", "Proj1", 85),
    ("TeamB", "Proj2", 95),
    ("TeamB", "Proj2", 75)
]

averages = merge_projects(records)
best = best_project(records, "TeamB")

print("Averages:", averages)
print("Best project for TeamB:", best)
