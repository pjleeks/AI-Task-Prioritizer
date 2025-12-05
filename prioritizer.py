# prioritizer.py
import pandas as pd

# =====================================
# AI Task Prioritizer - Logic Functions
# =====================================

def prioritize_tasks(tasks, model="LLM"):
    """
    Assign a priority score to each task and return a list of dicts.
    
    Args:
        tasks (list of str): List of task descriptions.
        model (str): 'LLM' or 'Local fallback' (currently placeholder).
        
    Returns:
        list of dicts: Each dict has keys:
            - task (str)
            - score (int 0-100)
            - priority (str: 'High', 'Medium', 'Low')
            - importance (str: 'Important', 'Medium', 'Low')
            - urgency (str: 'Urgent' or 'Not Urgent')
            - reasoning (str)
    """
    results = []
    for task in tasks:
        # Placeholder logic; replace with LLM scoring later
        score = 50  # Default mid-score
        if "urgent" in task.lower():
            score += 30
        if "report" in task.lower() or "deadline" in task.lower():
            score += 20

        score = min(score, 100)

        # Assign priority and importance based on score
        if score >= 70:
            priority = "High"
            importance = "Important"
        elif score >= 40:
            priority = "Medium"
            importance = "Medium"
        else:
            priority = "Low"
            importance = "Low"

        # Assign urgency based on keywords
        urgency = "Urgent" if "urgent" in task.lower() or "deadline" in task.lower() else "Not Urgent"

        results.append({
            "task": task,
            "score": score,
            "priority": priority,
            "importance": importance,
            "urgency": urgency,
            "reasoning": "Score based on keywords and placeholder logic."
        })
    return results


def eisenhower_matrix(prioritized_tasks):
    """
    Categorize tasks into an Eisenhower matrix.
    
    Args:
        prioritized_tasks (list of dicts): Output from prioritize_tasks.
        
    Returns:
        dict: Keys 'do_now', 'schedule', 'delegate', 'delete', each a list of task dicts.
    """
    matrix = {"do_now": [], "schedule": [], "delegate": [], "delete": []}

    for t in prioritized_tasks:
        # Determine urgency and importance for matrix placement
        urgency = t["urgency"]
        importance = t["importance"]

        if urgency == "Urgent" and importance == "Important":
            matrix["do_now"].append(t)
        elif urgency == "Not Urgent" and importance == "Important":
            matrix["schedule"].append(t)
        elif urgency == "Urgent" and importance != "Important":
            matrix["delegate"].append(t)
        else:
            matrix["delete"].append(t)

    return matrix
