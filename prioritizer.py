# prioritizer.py
import random

# -----------------------------
# Prioritize Tasks (Mock Scoring)
# -----------------------------
def prioritize_tasks(tasks, model="LLM (GPT)"):
    """
    Simple mock scoring function for testing.
    Each task gets:
        - score (0-100)
        - urgency (0-1)
        - importance (0-1)
        - rationale
    """
    results = []
    for task in tasks:
        urgency = round(random.uniform(0.3, 1.0), 2)
        importance = round(random.uniform(0.3, 1.0), 2)
        score = round((urgency + importance) / 2 * 100)
        rationale = f"Mock rationale: urgency={urgency}, importance={importance}"

        results.append({
            "task": task,
            "urgency": urgency,
            "importance": importance,
            "score": score,
            "rationale": rationale
        })

    # Sort high → low score
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return results


# -----------------------------
# Eisenhower Matrix
# -----------------------------
def eisenhower_matrix(tasks):
    """
    Assign tasks to 4 quadrants based on importance and urgency
    Expects tasks to have 'urgency' and 'importance' keys (0-1)
    """
    matrix = {
        "do_now": [],
        "schedule": [],
        "delegate": [],
        "delete": []
    }

    for t in tasks:
        urgency = t.get("urgency", 0.5)
        importance = t.get("importance", 0.5)

        if importance >= 0.5 and urgency >= 0.5:
            matrix["do_now"].append(t)
        elif importance >= 0.5 and urgency < 0.5:
            matrix["schedule"].append(t)
        elif importance < 0.5 and urgency >= 0.5:
            matrix["delegate"].append(t)
        else:
            matrix["delete"].append(t)

    return matrix
